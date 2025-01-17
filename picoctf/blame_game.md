Challenge Link: [Blame Game](https://play.picoctf.org/practice/challenge/405)

Download the challenge files. Notice the source file and the `.git` folder.

Inside the `.git` folder, we inspect the `config` file, which contains the statement `logallrefupdates = true`.
This means that all the updates to the repo are logged.

Naturally, inspecting the `logs` folder gives the answer. Both files `.git/logs/HEAD` and `.git/logs/refs/heads/master` contain an elaborate commit history.
The very second commit log contains the flag.
