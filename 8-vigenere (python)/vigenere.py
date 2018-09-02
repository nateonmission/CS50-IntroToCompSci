# Import Libraries
import cs50
import sys

if len(sys.argv) != 2:                          # Usage Error
    sys.exit("ERROR: Usage: vigenere CODEWORD")

# Variables
key = str(sys.argv[1])
keyLen = len(sys.argv[1])
keyArray = list()
cipherArray = list()
cipherText = ""
k = 0

for letter in key:                              # Array the key
    if letter.isalpha():
        keyArray.append(ord(letter.upper()) - 65)
    else:
        sys.exit("ERROR: Usage: CODEWORD must only be letters")

plainText = cs50.get_string("plaintext: ")      # Get the plaintext from user

for pt_char in plainText:
    if pt_char.isalpha():
        if ord(pt_char) >= 97 and ord(pt_char) <= 122:              # Lowercase letters
            if ord(pt_char) + keyArray[k % len(key)] > 122:
                cipherArray.append(chr(ord(pt_char) + keyArray[k % len(key)] - 26))
                k += 1
            else:
                cipherArray.append(chr(ord(pt_char) + keyArray[k % len(key)]))
                k += 1
        if ord(pt_char) >= 65 and ord(pt_char) <= 90:               # Uppercase letters
            if ord(pt_char) + keyArray[k % len(key)] > 90:
                cipherArray.append(chr(ord(pt_char) + keyArray[k % len(key)] - 26))
                k += 1
            else:
                cipherArray.append(chr(ord(pt_char) + keyArray[k % len(key)]))
                k += 1
    else:                                                           # Non-letters
        cipherArray.append(pt_char)

cipherText = "".join(cipherArray)                                   # Array to String

print("ciphertext:", cipherText)                                    # Print it out