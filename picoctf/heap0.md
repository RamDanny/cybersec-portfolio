Challenge Link [Heap 0](https://play.picoctf.org/practice/challenge/438)

Run the challenge instance and download the files.

Observing the source file, the flag is evidently printed when `check_win` is called, and the `safe_var` is set to some string other than "bico".
But `safe_var` is set to "bico" at the start of `main`.

But when the 'heap' is printed, the addresses of pointers to both `input_data` and `safe_var` are revealed.
Since allocated from the heap one after the other, `safe_var` has an address that comes after that of `input_data`.
This means that if a very large string is assigned as input to `input_data`, it overflows its bounds and keeps writing the subsequent addresses until the string is over.

Thus, if a string larger than the address difference between the variables is given as input, it will overwrite memory of even `safe_var`.
For example, if `input_data` is located at 20, and `safe_var` is located at 40, then an input of atleast 21 characters writes to `input_data`, overflows and
continues overwriting subsequent memory locations, finally stopping after reaching address 41. This has the effect of modifying one character of `safe_var`.
This ultimately means that `check_win` satisfies the condition, and prints the flag.
