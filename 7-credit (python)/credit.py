import cs50

cardNumber = 0
number = 0
numArray = list()
cardCount = 16
cardType = ""
bala = 0
balaa = 0
balb = 0
balc = 0
balaArray = list()

cardNumber = cs50.get_int("Card Number: ")
number = cardNumber

# CARD TYIPNG
# 13-digit  4# = VISA
if cardNumber > 4000000000000 and cardNumber < 4999999999999:
    cardType = "VISA"
    cardCount = 13
# 15-digit 34#   = AMEX
elif cardNumber > 340000000000000 and cardNumber < 350000000000000:
    cardType = "AMEX"
    cardCount = 15
# 15-digit 37#   = AMEX
elif cardNumber > 370000000000000 and cardNumber < 380000000000000:
    cardType = "AMEX"
    cardCount = 15
# 16-digit 51# 52# 53# 54# 55# = MC
elif cardNumber > 5100000000000000 and cardNumber < 5599999999999999:
    cardType = "MASTERCARD"
    cardCount = 16
# 16-digit 4# = VISA
elif cardNumber > 4000000000000000 and cardNumber < 4999999999999999:
    cardType = "VISA"
    cardCount = 16
else:
    cardType = "INVALID"
    cardCount = 0

# arrays the card number
for digit in range(0, cardCount - 1):
    numArray.append(int(number % 10))
    number = number / 10

# EVEN vs ODD card number length
if cardCount % 2 == 0:
    for j in range(cardCount - 2, 0, -2):
        if numArray[j] < 5:
            bala += numArray[j] * 5
        else:
            balaa = numArray[j] * 2
            for m in range(0, 2):
                balaArray.append(balaa % 10)
                balaa = balaa / 10
            bala = bala + balaArray[0] + balaArray[1]
    for k in range(cardCount - 2, 0, -2):
        balb += numArray[k]
else:
    for j in range(cardCount - 2, 0, -2):
        if numArray[j] < 5:
            bala += numArray[j] * 2
    else:
        balaa = numArray[j] * 2
        for m in range(0, 2):
            balaArray.append(balaa % 10)
            balaa = balaa / 10
        bala = bala + balaArray[0] + balaArray[1]
    for k in range(cardCount - 2, 0, -2):
        balb += numArray[k]

# Sum the sums
blac = bala + balb

# Validate
if balc % 10 == 0:
    print(cardType)
else:
    print("INVALID")