# Questions

## What's `stdint.h`?

According to C Programming at Wikibooks, this header file defines types of intigers with fixed widths.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

By specifying fixed sized units, compatibility is improved across machines.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE    1B or 8b
DWORD   4B or 32b
LONG    4B or 32b
WORD    2B or 16b

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x424d, which is BM in ASCII.

## What's the difference between `bfSize` and `biSize`?

biSize is the size of the BITMAPINFOHEADER within the file and is fixed at 40. bfSize is the size of the whole file, including all headers.

## What does it mean if `biHeight` is negative?

It means the image date is "right-side up". That is to say the code for the top of the top of the image starts immediately after the headers.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

BiBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If the named file is not in the current directory, then NULL will be returned.

## Why is the third argument to `fread` always `1` in our code?

It is always 1 because we're look at 1 element at a time.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

It will be 3 in order to get to a multiple of 4.

## What does `fseek` do?

It moves the file position indicator for the file stream relative to offset.

## What is `SEEK_CUR`?

Defines offset relative to current position of indicator.

## Who, indeed, did do it?

PROFESSOR PLUM WITH THE CANDLESTICK IN THE LIBRARY!
