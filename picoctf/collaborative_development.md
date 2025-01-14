Challenge Link: [Collaborative Development](https://play.picoctf.org/practice/challenge/410)

Download the challenge files, and navigate to the `.git` directory.

The `HEAD` file contains a path to another file inside `refs/heads/`. Navigating to `refs/heads/feature`, we have files called "part-1", "part-2", "part-3".
Each file contains a distinct commit ID.

Initialize the git repository and checkout each commit using the commands:

1. `git init <folder-name>`

2. `git checkout <commit-id>`

Once initialized, checkout each commit and print the contents of `flag.py` using the `cat` command.
Each time, a part of the flag is revealed in the code. Concatenating the three pieces gives the complete flag.
