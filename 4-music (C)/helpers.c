// Helper functions for music

#include <cs50.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // converts and loads chars into ints for calculation
    float numerator = (int) fraction[0] - 48;
    float denominator = (int) fraction[2] - 48;
    // performs the calculations
    int myNum = (numerator /  denominator) * 8;
    return myNum;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    char tone[3];
    tone[0] = (char) note[0];
    tone[1] = (char) note[strlen(note) - 1];
    char accedental[2];
    accedental[0] = (char) note[1];
    accedental[1] = '\0';
    char flat[2] = "b";
    char sharp[2] = "#";

    int i = 0;
    int a4 = 45;
    float distance = 0;
    char *cscale[100] =
    {
        "C1", "#", "D1", "#", "E1", "F1", "#", "G1", "#", "A1", "#", "B1",
        "C2", "#", "D2", "#", "E2", "F2", "#", "G2", "#", "A2", "#", "B2",
        "C3", "#", "D3", "#", "E3", "F3", "#", "G3", "#", "A3", "#", "B3",
        "C4", "#", "D4", "#", "E4", "F4", "#", "G4", "#", "A4", "#", "B4",
        "C5", "#", "D5", "#", "E5", "F5", "#", "G5", "#", "A5", "#", "B5",
        "C6", "#", "D6", "#", "E6", "F6", "#", "G6", "#", "A6", "#", "B6",
        "C7", "#", "D7", "#", "E7", "F7", "#", "G7", "#", "A7", "#", "B7",
        "C8", "#", "D8", "#", "E8", "F8", "#", "G8", "#", "A8", "#", "B8"
    };
// char homeKey[3] = "A4";
    float frqhz = 0;

    while ((i < 12 * 8) && strcmp(cscale[i], tone) != 0)    // Get index of tone
    {
        i++;
    }

    if (i <= a4)                                     // Going DOWN the scale
    {
        distance = a4 - i;                          // figures disatance between A4 and note

        if (strcmp(accedental, flat) == 0)           // add half-step if flat
        {
            distance++;
        }
        else if (strcmp(accedental, sharp) == 0)      // subtract half-step if sharp
        {
            distance--;
        }

        frqhz = round(440 / pow(2, (distance / 12)));           // calulate the frquency based on distance of note from A4
    }
    else                                                      // Going UP the scale
    {
        distance = i - a4;                                   // figures disatance between A4 and note

        if (strcmp(accedental, flat) == 0)                   // subtract half-step if flat
        {
            distance--;
        }
        else if (strcmp(accedental, sharp) == 0)            // add half-step if sharp
        {
            distance++;
        }

        frqhz = round(440 * pow(2, (distance / 12)));       // calulate the frquency based on distance of note from A4
    }

    return (int) frqhz;                                   // Returns the frquency of note in HZ
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, "") == 0)                         // Is the line blank
    {
        return true;
    }
    else
    {
        return false;
    }
}
