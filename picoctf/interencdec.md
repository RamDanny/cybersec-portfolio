Challenge Link: [Interencdec](https://play.picoctf.org/practice/challenge/418)

Download the file and read its contents.

Looking at it might suggest base64 encoding. Decoding it gives a binary string. Reversing the binary gives another base64 string, and decoding that gives a string.

The string has a format similar to a flag, and suggests the use of a substitution cipher like caesar shift. Decoding with a shift of 19 gives the flag.
