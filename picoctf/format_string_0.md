Challenge Link: [Format String 0](https://play.picoctf.org/practice/challenge/433)

Download the source file, binary, and run the problem instance to connect to the challenge.

The source runs two functions, `serve_patrick` and `serve_bob`, each requiring the user to enter from one of three choices provided in the menu.
No options outside the menu work.

The flag is revealed when a specific option from each menu is chosen. To understand why, the code must be understood further.

```
void serve_patrick() {
    ...
    char choice1[BUFSIZE];
    scanf("%s", choice1);
    char *menu1[3] = {"Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe"};
    if (!on_menu(choice1, menu1, 3)) {
        printf("%s", "There is no such burger yet!\n");
        fflush(stdout);
    } else {
        int count = printf(choice1);
        if (count > 2 * BUFSIZE) {
            serve_bob();
        } else {
            ...
}
```

Inside `serve_patrick`, there is a condition `count > 2 * BUFSIZE` that has to be satisfied for `serve_bob` to run.
This means that the size of the input `choice1` written into `count` must be greater than 2 * `BUFSIZE`, i.e. greater than 64.
But none of the menu options "Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe" seem to exceed 64 just by looking.

But "Gr%114d_Cheese" works, since it contains the format specifier `%114d`.
This is because when `printf` reads this string, it interprets that there is a placeholder for a 114-digit number.
This placeholder is usually followed by an argument while printing, but since it's absent here, 114 characters of garbage can be plugged by the compiler.
Ultimately, this has the effect of exceeding the a string length of 64, satisfying the condition to trigger `serve_bob`.

```
void serve_bob() {
    printf("\n%s %s\n%s %s\n%s %s\n%s",
            "Good job! Patrick is happy!",
            "Now can you serve the second customer?",
            "Sponge Bob wants something outrageous that would break the shop",
            "(better be served quick before the shop owner kicks you out!)",
            "Please choose from the following burgers:",
            "Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak",
            "Enter your recommendation: ");
    fflush(stdout);
    char choice2[BUFSIZE];
    scanf("%s", choice2);
    char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};
    if (!on_menu(choice2, menu2, 3)) {
        printf("%s", "There is no such burger yet!\n");
        fflush(stdout);
    } else {
        printf(choice2);
        fflush(stdout);
    }
```

Inside `serve_bob`, there seems to be no condition that prints the flag. This can seem puzzling until the rest of the code is analyzed.
Neither of "Pe%to_Portobello"or "$outhwest_Burger" work, but "Cla%sic_Che%s%steak" works. This is because of the three `%s` format specifiers present in the string.
This means `printf` reads `choice2`, interpreting that there is a placeholder for a string argument.
Since no argument is provided, it might try to access an arbitrary memory address, which leads to a segmentation fault.
This would normally crash a program, but the line `signal(SIGSEGV, sigsegv_handler);` holds the key.
Unix-like OSes use `SIGSEGV` as the ID for signalling a segmentation fault.
In this case, this triggers the handler `sigsegv_handler`, which subsequently prints the flag.
