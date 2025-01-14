Challenge Link: [CanYouSee](https://play.picoctf.org/practice/challenge/408)

Download the files and get the image. The image itself doesn't seem to reveal anything, nor does its file system metadata.
Nothing useful found in using `ls -la` command either.

But using external metadata tools reveals more information. The `attribution_url` field contains a base64 encoded string, which upon decoding gives the flag.
