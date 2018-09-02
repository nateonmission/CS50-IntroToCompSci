#include <stdio.h>
#include <cs50.h>
#include <string.h>

long long int cardNumber;
long long int number;
int cardCount = 16;
char cardType[12];
int bala = 0;
int balaa = 0;
int balaArray[2] = {0};
int balb = 0;
int balc = 0;
int numberArray[16] = {0};

int main(void)
{
    cardNumber = get_long_long("Card Number: ");
    number = cardNumber;

    // CARD TYIPNG
    // 13-digit  4# = VISA
    if (cardNumber > 4000000000000 && cardNumber < 4999999999999)
    {
        strcpy(cardType, "VISA");
        cardCount = 13;
    } // 15-digit 34#   = AMEX
    else if (cardNumber > 340000000000000 && cardNumber < 350000000000000)
    {
        strcpy(cardType, "AMEX");
        cardCount = 15;
    }  // 15-digit 37#   = AMEX
    else if (cardNumber > 370000000000000 && cardNumber < 380000000000000)
    {
        strcpy(cardType, "AMEX");
        cardCount = 15;
    } // 16-digit 51# 52# 53# 54# 55# = MC
    else if (cardNumber > 5100000000000000 && cardNumber < 5599999999999999)
    {
        strcpy(cardType, "MASTERCARD");
        cardCount = 16;
    } //16-digit 4# = VISA
    else if (cardNumber > 4000000000000000 && cardNumber < 4999999999999999)
    {
        strcpy(cardType, "VISA");
        cardCount = 16;
    }
    else
    {
        strcpy(cardType, "INVALID");
        cardCount = 0;
    }

    // arrays the card number
    for (int i = 0; i < cardCount; i++)
    {
        numberArray[i] = number % 10;
        number = number / 10;
    }

    // IF for even and odd card numbers
    if (cardCount % 2 == 0)
    {
        // doubles and sums odd-indexed numbers
        for (int j = cardCount-1; j >= 0; j = j - 2)
        {
            if (numberArray[j] < 5)
            {
                bala += numberArray[j] * 2;
            }
            else
            {
                balaa = numberArray[j] * 2;
                for (int m = 0; m < 2; m++)
                {
                    balaArray[m] =  balaa % 10;
                    balaa = balaa / 10;
                } // for m
                bala = bala + balaArray[0] + balaArray[1];
            } // elsecheck
        } // for j

        // sums the even-indexed numbers
        for (int k = cardCount-2; k >= 0; k = k - 2)
        {
            balb += numberArray[k];
        }
    }
    else
    {
        // doubles and sums even-indexed numbers
        for (int j = cardCount-2; j >= 0; j = j - 2)
        {
            if (numberArray[j] < 5)
            {
                bala += numberArray[j] * 2;
            }
            else
            {
                balaa = numberArray[j] * 2;
                for (int m = 0; m < 2; m++)
                {
                    balaArray[m] =  balaa % 10;
                    balaa = balaa / 10;
                } // for m
                bala = bala + balaArray[0] + balaArray[1];
            } // elsecheck
        } // for j

        // sums the odd-indexed numbers
        for (int k = cardCount-1; k >= 0; k = k - 2)
        {
            balb += numberArray[k];
        }
    }

    // sums the sums
    balc = bala + balb;

    // validation
    if (balc % 10 == 0)
    {
        printf("%s\n", cardType);
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
} // Close Main