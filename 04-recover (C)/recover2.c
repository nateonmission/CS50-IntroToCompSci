// Recovers JPGs from memory file.

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 512


int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover datafile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[1];
    unsigned char buffer[512];
    char theFilename[8];
    int headerFound = 0;
    int isOpen = 0;
    int foundFiles = 0;
    int mainLoop = 1;
    FILE *inptr = NULL;
    FILE *outptr = NULL;


    // open input file
    inptr = fopen(infile, "r");

    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    while (!feof(inptr))
    {
        fread(buffer, 512, 1, inptr);                      // read infile

        if                                                 //looks for JPG signature
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

        if (headerFound == 0 && isOpen != 0)       // No Header - File Open - 2
        {
            if (sizeof(buffer) < 512)                       // when EOF is reached - 1
            {
                fwrite(buffer, sizeof(buffer), 1, outptr);
                fclose(inptr);
                fclose(outptr);
                mainLoop = 0;
                return 0;
            }
            else
            {
                fwrite(buffer, 512, 1, outptr);            // write buffer to JPG file
            }
        }

        else if (headerFound == 1 && isOpen == 0)           // Header found - No file open - 3
        {
            sprintf(theFilename, "%03i.jpg", foundFiles);   // creates name
            outptr = fopen(theFilename, "w");                // opens file for writing
            isOpen++;                                       // toggle isOpen to non-0
            fwrite(buffer, 512, 1, outptr);                  // write buffer to JPG file
            foundFiles++;                                   // increments number of files found
            headerFound = 0;
        }

        else if (headerFound == 1 && isOpen != 0)               // Header found - File open - 4
        {
            fclose(outptr);                                     // close prev file
            sprintf(theFilename, "%03i.jpg", foundFiles);       // creates name
            outptr = fopen(theFilename, "w");                   // opens file for writing
            isOpen++;                                           // toggle isOpen to non-0
            fwrite(buffer, 512, 1, outptr);                     // write buffer to JPG file
            foundFiles++;                                       // increments number of files found
            headerFound = 0;

        }

//fseek(inptr, 512, SEEK_CUR);

    }   // close loop



}   // close Main


/*
    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // iterate over pixels in scanline
        for (int j = 0; j < bi.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // write RGB triple to outfile
            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }

        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);

        // then add it back (to demonstrate how)
        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
*/