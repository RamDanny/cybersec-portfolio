Challenge Link: [Verify](https://play.picoctf.org/practice/challenge/450)

Connect to the challenge's shell instance.

Run the SHA-256 hash on every file in the `files` directory and check if it matches the given checksum using `sha256sum files/* >> <filename>`.

Find the file corresponding to the given checksum using `grep '<checksum>' <filename>`.

Run `decypt.sh` on the file found using `./decrypt.sh files/<filename>`. This prints the flag to the shell.
