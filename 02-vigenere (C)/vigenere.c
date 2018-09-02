// HEADER FILES
#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>

// DECLARE VARIABLES
int keyLength = 0;
char key[100];
int keyShift[100];
int k = 0;
char cipherText[100];


int main(int argc, string argv[])                          // DECLARE MAIN & accept command-line KEY
{
    if (argc < 2)
    {
        printf("ERROR: Please, enter one command-line argument.\n");    // If argument is NULL
        return 1;
    }
    else
    {
    strcpy(key, argv[1]);
    }

    if (argc == 2)
    {
        keyLength = strlen(argv[1]);                        // check length of KEY and set it at KEYLEN
        for (int i = 0; i < keyLength; i++)
        {
            keyShift[i] = ((int) toupper(key[i]))-65;       // toupper the KEY, convert to number and subtract 65
            if (!isalpha(key[i]))                           // ISALPHA() - throw error if KEY is non-alphabetic, exit and return 0
            {
                printf("ERROR: Please enter only alphabetic keys.\n");
                return 1;
            }
        }

    }
    else
    {
    printf("ERROR: Please, enter one command-line argument.\n");
    return 1;
    }

    string plainText = get_string("plaintext: ");           // prompt user for input - plaintext

    for (int j = 0; j < strlen(plainText); j++)             // encodes (shifts) alpha characters
    {
        if (!isalpha(plainText[j]))
        {
            cipherText[j] = plainText[j];                   // if plaintext[i] is non-alphabetic add char unchanged to cipherText
        }
        else                                                //(char) ((int) plainText[j] + keyShift[k % strlen(key)]) ;
        {
            if((int) plainText[j] >= 97 && (int) plainText[j] <= 122)                              // LOWERCASE LETTERS
            {
                if (122 < (int) plainText[j] + keyShift[k % strlen(key)])                         // Lower passes z to wrap
                {
                    cipherText[j] = (char)((int) plainText[j] + keyShift[k % strlen(key)]-26) ;
                    k++;
                }
                else
                {
                    cipherText[j] = (char)((int) plainText[j] + keyShift[k % strlen(key)]) ;
                    k++;
                }
            }
            if ((int) plainText[j] >= 65 && (int) plainText[j] <= 90)                              // UPPERCASE LETTERS
            {
                if (90 < (int) plainText[j] + keyShift[k % strlen(key)])
                {
                    cipherText[j] = (char)((int) plainText[j] + keyShift[k % strlen(key)]-26) ;    // Upper passes z to wrap
                    k++;
                }
                else
                {
                    cipherText[j] = (char)((int) plainText[j] + keyShift[k % strlen(key)]) ;
                    k++;
                }
            }
        }
    }
    printf("ciphertext: %s\n", cipherText);                 // print "ciphertext: [ciphertext]"
    return 0;
}   // CLOSE MAIN