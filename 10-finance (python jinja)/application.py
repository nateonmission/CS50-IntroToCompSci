import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    portfolio = db.execute("SELECT symbol, sum(quantity) as 'quantity' FROM 'transactions' WHERE user_key = :user_key  AND symbol <> 'N/A' GROUP BY symbol;",
        user_key=session["user_id"])
    user = db.execute("SELECT * FROM users WHERE id = :user_key;", user_key=session["user_id"])
    currentCash = user[0]['cash']
    totalAssets = 0
    symbols = []
    currentQuote = []
    qty = []
    stockValues = []
    currentValues = []

    for symbol_i in range(0, len(portfolio)):
        symbols.append(portfolio[symbol_i]['symbol'])

    for quote_i in range(0, len(symbols)):
        currentQuote.append(lookup(symbols[quote_i])['price'])
        qXv = portfolio[quote_i]['quantity'] * currentQuote[quote_i]
        totalAssets += qXv
        currentValues.append(usd(qXv))
        qXv = 0
    totalAssets += currentCash
    totalAssets = usd(totalAssets)
    currentCash = usd(currentCash)

    return render_template("index.html", portfolio=portfolio, user=user, currentQuote=currentQuote, currentCash=currentCash, totalAssets=totalAssets, currentValues=currentValues)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Error Handling
        try:
            qty = request.form.get("shares")
            symbol = request.form.get("symbol")
            user_key = session["user_id"]
        except:
            return apology("I can't even...")
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)
        # Ensure password was submitted
        elif not request.form.get("shares"):
            return apology("must provide quantity to buy", 400)

        try:
            qty = int(qty)
        except:
            return apology("intiger", 400)
        if qty <= 0:
            return apology("positive", 400)

        # Gather information
        # Get current stock price info
        quoteDict = lookup(request.form.get("symbol"))
        # Ensure quote was received
        if not quoteDict:
            return apology("No Quote Received", 400)
        # Query database for username
        account = db.execute("SELECT * FROM users WHERE id = :user_key",
            user_key=session["user_id"])

        # Load Variable and Calculate
        accountBalance = account[0]['cash']
        buyPrice = quoteDict['price'] * -1
        totalCost = buyPrice * qty
        newBalance = accountBalance + totalCost
        transList = [user_key, 'buy', symbol, qty, buyPrice, totalCost, newBalance]
        transList1 = [user_key, 'buy', symbol, qty, usd(buyPrice), usd(totalCost), usd(newBalance)]

        # Can user afford it
        if totalCost > accountBalance:
            return apology("Insufficient Funds")

        # INSERT BUY transaction into TRANSACTIONS table
        result = db.execute("INSERT INTO transactions (user_key, trans_type, symbol, quantity, price) VALUES (:user_key, :trans_type, :symbol, :quantity, :price);",
                          user_key=transList[0], trans_type=transList[1], symbol=transList[2], quantity=transList[3], price=transList[5])
        if not result:
            return apology("DB Fail! Try Again [INSERT]", 403)
        result_update = db.execute("UPDATE users SET cash = :newBalance WHERE id = :user_key;", newBalance=float(transList[6]), user_key=transList[0])
        if not result_update:
            return apology("DB Fail! Try Again [UPDATE]", 403)

        # Success
        #render_template("buy_success.html", transList=transList)
        return  render_template("buy_success.html", transList1=transList1)

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT trans_key, trans_date, trans_type, symbol, quantity, price FROM transactions WHERE user_key = :user_key",
        user_key=session["user_id"])
    user = db.execute("SELECT * FROM users WHERE id = :user_key",
        user_key=session["user_id"])
    return render_template("history.html", transactions=transactions, user=user)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        quoteDict = lookup(request.form.get("symbol"))

        # Ensure symbol was submitted
        if not quoteDict:
            return apology("must provide valid stock symbol", 400)

        quoteList = [usd(float(quoteDict['price'])), quoteDict['symbol']]

        return render_template("quote_info.html", quoteList=quoteList)

    # Return user to QUOTE to try again
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password was submitted
        elif not request.form.get("confirmation"):
            return apology("must verify password", 400)

        # Ensure password was submitted
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password & verify password must match", 400)

        # Hash the password
        pswd_hash = generate_password_hash(request.form.get("password"))
        user = request.form.get("username")

        # Add username to database
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :pswd_hash)",
            username=request.form.get("username"), pswd_hash=pswd_hash)
        if not result:
            return apology("DB Fail! Try Again", 400)

        # Remember which user has logged in
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        toSell = request.form.get('symbol')
        sellQty = request.form.get('shares')

        try:
            sellQty = int(sellQty)
        except:
            return apology('number error', 400)

        portfolio = db.execute("SELECT symbol, sum(quantity) as 'quantity' FROM 'transactions' WHERE user_key = :user_key AND symbol = :toSell GROUP BY symbol;",
            user_key=session["user_id"], toSell=toSell)

        if not portfolio:
            return apology('DB Read Error  PORTFOLIO', 400)
        if portfolio[0]['quantity'] < sellQty:
            return apology('Do you have that many', 400)

        priceDict = lookup(toSell)
        price = priceDict['price']
        totalPrice = price * sellQty

        user = db.execute("SELECT cash FROM users WHERE id = :user_key;", user_key=session["user_id"])
        if not user:
            return apology('DB Read Error USER')

        newBalance = user[0]['cash'] + totalPrice

        # INSERT SELL transaction into TRANSACTIONS table
        result = db.execute("INSERT INTO transactions (user_key, trans_type, symbol, quantity, price) VALUES (:user_key, :trans_type, :symbol, :quantity, :price);", user_key=session["user_id"], trans_type='SELL', symbol=toSell, quantity=sellQty, price=totalPrice)
        if not result:
            return apology("DB Fail Try Again INSERT", 403)

        result_update = db.execute("UPDATE users SET cash = :newBalance WHERE id = :user_key;", newBalance=newBalance, user_key=session["user_id"])
        if not result_update:
            return apology("DB Fail Try Again UPDATE", 403)

        transList1 = [sellQty, toSell, usd(price), usd(totalPrice), usd(newBalance)]

        # Success
        return render_template("sell_success.html", transList1=transList1)

    else:
        portfolio = db.execute("SELECT symbol, sum(quantity) as 'quantity' FROM 'transactions' WHERE user_key = :user_key  AND symbol <> 'N/A' GROUP BY symbol;",
            user_key=session["user_id"])
        user = db.execute("SELECT * FROM users WHERE id = :user_key;", user_key=session["user_id"])
        currentCash = user[0]['cash']
        totalAssets = 0
        symbols = []
        currentQuote = []
        qty = []
        stockValues = []
        currentValues = []

        for symbol_i in range(0, len(portfolio)):
            symbols.append(portfolio[symbol_i]['symbol'])

        for quote_i in range(0, len(symbols)):
            currentQuote.append(lookup(symbols[quote_i])['price'])
            qXv = portfolio[quote_i]['quantity'] * currentQuote[quote_i]
            totalAssets += qXv
            currentValues.append(usd(qXv))
            qXv = 0
        totalAssets += currentCash
        totalAssets = usd(totalAssets)
        currentCash = usd(currentCash)

        return render_template("sell.html", portfolio=portfolio, user=user, currentQuote=currentQuote, currentCash=currentCash, totalAssets=totalAssets, currentValues=currentValues, symbols=symbols)


@app.route("/xfer", methods=["GET", "POST"])
@login_required
def xfer():
    """Transfer in or out an amout of cashk"""
    if request.method == "POST":

        # Error Handling
        try:
            routing = request.form.get("routing")
            bank_acct = request.form.get("account")
            amount = float(request.form.get("amount"))
            direction = request.form.get("direction")
        except:
            return apology("Just fill out the form...")

        # Query database for username
        account = db.execute("SELECT * FROM users WHERE id = :user_key",
            user_key=session["user_id"])

        # Load Variable and Calculate
        accountBalance = account[0]['cash']
        symbol = 'N/A'
        quantity = 1
        user_key = session["user_id"]

        if direction == 'Xfer-OUT':
            if amount > accountBalance:
                return apology("Yain't got no money")
            price = amount * -1
            trans_type = 'Xfer-OUT'
        else:
            price = amount
            trans_type = 'Xfer-IN'

        newBalance = accountBalance + price

        # INSERT BUY transaction into TRANSACTIONS table
        result = db.execute("INSERT INTO transactions (user_key, trans_type, symbol, quantity, price, bank_acct, routing) VALUES (:user_key, :trans_type, :symbol, :quantity, :price, :bank_acct, :routing);",
            user_key=user_key, trans_type=trans_type, symbol=symbol, quantity=quantity, price=price, bank_acct=bank_acct, routing=routing)
        if not result:
            return apology("DB Fail Try Again INSERT", 403)

        result_update = db.execute("UPDATE users SET cash = :newBalance WHERE id = :user_key;",
            newBalance=int(newBalance), user_key=user_key)
        if not result_update:
            return apology("DB Fail Try Again UPDATE", 403)

        return redirect('/')

    else:
        return render_template("xfer.html")


def errorhandler(e):
    """Handle error"""
    return apology(e)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
