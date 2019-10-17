"""
Question-

This is a common problem with string encryption using the Caesar Cipher.
Caesar Cipher is done to shift all the charcaters ina string by a specified number of characters either in
forward direction or the reverse side.

For example-

ABC after a Caesar Cipher of +3 will shift to DEF.
ABC after a Caesar Cipher of -3 will shift to XYZ.

AbC after a Caesar Cipher of +3 will shift to DeF.
AbC after a Caesar Cipher of -3 will shift to XyZ.

Input will be - An integer number in positive and negative region between +1 to +25 and -1 to -25.
Works for all Alphanumeric strings.
"""


def CaesarCipher(Shift_index, String_to_convert):
    if Shift_index > 25 | Shift_index < -25:
        return String_to_convert + "Please enter shift value between +1 to +25 and -1 to -25."
    else:
        cipherText = ""
        for char in String_to_convert:
            pos = ord(char)
            if 48 <= pos <= 57:
                newpos = (pos - 48 + Shift_index) % 10 + 48
            elif 65 <= pos <= 90:
                newpos = (pos - 65 + Shift_index) % 26 + 65
            elif 97 <= pos <= 122:
                newpos = (pos - 97 + Shift_index) % 26 + 97
            else:
                newpos = pos
            cipherText += chr(newpos)
        return cipherText