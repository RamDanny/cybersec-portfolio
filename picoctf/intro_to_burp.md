Challenge Link: [Intro To Burp](https://play.picoctf.org/practice/challenge/419)

Connecting to the challenge leads to a webpage form. Any combo of non-empty inputs load the next screen for the next form.

This form contains one OTP field. Sending any input generates an error message.

Use Burpsuite to intercept the form submit request. It contains the input OTP under the `otp` field. Remove this header field and forward the request.
This bypasses the check and prints the flag on the page.
