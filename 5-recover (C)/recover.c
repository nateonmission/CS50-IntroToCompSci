// Recovers JPGs from memory file.

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 512


int main(int argc, char *argv[])
{
    if (argc != 2)                                              // error handler - usage
    {
        fprintf(stderr, "Usage: recover datafile\n");
        return 1;
    }

    char *infile = argv[1];
    unsigned char buffer[BUFFER_SIZE];
    char theFilename[8];
    int headerFound = 0;
    int isOpen = 0;
    int foundFiles = 0;
    FILE *inptr = NULL;
    FILE *outptr = NULL;

    // open input file
    inptr = fopen(infile, "r");

    if (inptr == NULL)                                          // error handler - can't open file
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    while (fread(buffer, BUFFER_SIZE, 1, inptr) == 1)           // read infile and loop until EOF
    {
        if                                                      //looks for JPG signature
        (
            buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0
        )
        {
            headerFound = 1;
        }
        else
        {
            headerFound = 0;
        }

        if (headerFound == 0 && isOpen != 0)                    // No Header - File Open - 1
        {
            fwrite(buffer, BUFFER_SIZE, 1, outptr);             // write buffer to JPG file
        }

        else if (headerFound == 1 && isOpen == 0)               // Header found - No file open - 2
        {
            sprintf(theFilename, "%03i.jpg", foundFiles);       // creates name
            outptr = fopen(theFilename, "w");                   // opens file for writing
            isOpen++;                                           // toggle isOpen to non-0
            fwrite(buffer, BUFFER_SIZE, 1, outptr);             // write buffer to JPG file
            foundFiles++;                                       // increments number of files found
            headerFound = 0;
        }

        else if (headerFound == 1 && isOpen != 0)               // Header found - File open - 3
        {
            fclose(outptr);                                     // close prev file
            sprintf(theFilename, "%03i.jpg", foundFiles);       // creates name
            outptr = fopen(theFilename, "w");                   // opens file for writing
            isOpen++;                                           // toggle isOpen to non-0
            fwrite(buffer, BUFFER_SIZE, 1, outptr);             // write buffer to JPG file
            foundFiles++;                                       // increments number of files found
            headerFound = 0;

        }

    }   // close loop

    fclose(inptr);
    fclose(outptr);

    return 0;
}   // close Main