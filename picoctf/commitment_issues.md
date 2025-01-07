Challenge Link [Commitment Issues](https://play.picoctf.org/practice/challenge/411)

Download and extract the challenge zip file. Inside is the `.git` folder that contains git repository information.

Initialize a local repo using git. Then navigate to the `.../.git/logs/HEAD` file.
It contains the commit ID for both the old version (which is the one with flag info in it) and new version.

Use this commit ID to load the commit. Use the command `git checkout <commit-id>`. Once done, `message.txt` contains the flag.
