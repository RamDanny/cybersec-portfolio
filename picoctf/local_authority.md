Challenge Link: [Local Authority](https://play.picoctf.org/practice/challenge/278)

Go to the challenge website. Open developer tools, then enter any credentials.
Inspect the source code that shows the password being compared to a hash.

To find the password behind the hash, go to the network tab and find the `secret.js` file. Inside it reveals the password needed, and the admin username.
Use these credentials to enter the website, where the flag is revealed.
