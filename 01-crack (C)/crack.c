// HEADER FILES
#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>
#include <stdbool.h>
#include <crypt.h>
#include <unistd.h>
#define _XOPEN_SOURCE

char hashIn[15];
char hashOut[15];
char salt[15];
char ab[52] =
{
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

};
char testWord[5];
char cryptWord[15];
int counter = 1;


int main(int argc, string argv[])                                       // DECLARE MAIN & accept command-line KEY
{
    if (argc != 2)
    {
        printf("ERROR: Please, enter one command-line argument.\n");    // If argument is NULL
        return 1;
    }

    strcpy(hashIn, argv[1]);                                            // Take argv, put [0] & [1] into salt
    salt[0] = hashIn[0];
    salt[1] = hashIn[1];

// generate all possible a-zA-Z combinations into pswd

    for (int q1 = 0; q1 < 52; q1++)                                     // 1-letter pswds
    {
        testWord[0] = ab[q1];
        testWord[1] = '\0';
        testWord[2] = '\0';
        testWord[3] = '\0';
        testWord[4] = '\0';
        if (strcmp(hashIn, crypt(testWord, salt)) == 0)               // Does it match?
        {
            printf("%s \n ", testWord);
            return 0;
        }
    }


    for (int p2 = 0; p2 < 52; p2++)                                     // 2-letter pswds
    {
        for (int p1 = 0; p1 < 52; p1++)
        {
            testWord[0] = ab[p2];
            testWord[1] = ab[p1];
            testWord[2] = '\0';
            testWord[3] = '\0';
            testWord[4] = '\0';
            if (strcmp(hashIn, crypt(testWord, salt)) == 0)             // Does it match?
            {
                printf("%s \n ", testWord);
                return 0;
            }
        }
    }

    for (int n3 = 0; n3 < 52; n3++)                                     // 3-letter pswds
    {
        for (int n2 = 0; n2 < 52; n2++)
        {
            for (int n1 = 0; n1 < 52; n1++)
            {
                testWord[0] = ab[n3];
                testWord[1] = ab[n2];
                testWord[2] = ab[n1];
                testWord[4] = '\0';
                if (strcmp(hashIn, crypt(testWord, salt)) == 0)         // Does it match?
                {
                    printf("%s \n ", testWord);
                    return 0;
                }
            }
        }
    }


    for (int m4 = 0; m4 < 52; m4++)                                     // 4-letter pswds
    {
        for (int m3 = 0; m3 < 52; m3++)
        {
            for (int m2 = 0; m2 < 52; m2++)
            {
                for (int m1 = 0; m1 < 52; m1++)
                {
                    testWord[0] = ab[m4];
                    testWord[1] = ab[m3];
                    testWord[2] = ab[m2];
                    testWord[3] = ab[m1];
                    testWord[4] = '\0';
                    if (strcmp(hashIn, crypt(testWord, salt)) == 0)     // Does it match?
                    {
                        printf("%s \n ", testWord);
                        return 0;
                    }
                }
            }
        }
    }

// 5-letter pswds
    for (int l5 = 0; l5 < 52; l5++)
    {
        for (int l4 = 0; l4 < 52; l4++)
        {
            for (int l3 = 0; l3 < 52; l3++)
            {
                for (int l2 = 0; l2 < 52; l2++)
                {
                    for (int l1 = 0; l1 < 52; l1++)
                    {
                        testWord[0] = ab[l5];
                        testWord[1] = ab[l4];
                        testWord[2] = ab[l3];
                        testWord[3] = ab[l2];
                        testWord[4] = ab[l1];
                        if (strcmp(hashIn, crypt(testWord, salt)) == 0)     // Does it match?
                        {
                            printf("%s \n ", testWord);
                            return 0;
                        }
                    }
                }
            }
        }
    }

// If no Match is Found
    return 1;
}