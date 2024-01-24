# Study tools

*to make the python files in this folder executable, use: ``chmod +x *.py`` in the terminal*

### Numeral systems converter
Converts your number from old_base to new_base and copy to clipboard. Minimum base is 2, maximum 16. Supports expressions and input through console args.
**Some cases:**

```console
foo@bar:~$ ./numeralsystems.py 10 16 "50 * 2 + 50"
Result: 0x96
```

```console
foo@bar:~$ ./numeralsystems.py
Base numeral system and new system: 2 16
Number or expression: 10010
Result: 0x12
```

### Mask generator
Generates a mask with the specified positions in the hexadecimal system and copies it to the clipboard. The character count starts from the end. Supports the input of the interval through "-".

**Some cases:**
```console
foo@bar:~$ ./maskgenerator.py
Enter the positions: 1 5-9 14
Mask: 0x21f1 // binary representation "10000111110001"
```