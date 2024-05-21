# Study tools

*to make the python files in this folder executable, use: ``chmod +x *.py`` in the terminal*\
*Python 3.10 or higher is required*

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
Hex mask: 0x21f1
Binary mask: 10000111110001
```

### Passwords generator
Generates a sample of a given length and a given quantity, or a standard quantity. Allows you to copy the selected password immediately, without highlighting.

**Some cases:**
```console
foo@bar:~$ ./passwordgen.py
1) yG2cam8[14duHYDO_1Eg+3.5@Sgr
2) Hm$U5sG%2vLo7_o]8TZT+$PdkG.a
3) lSNm7CeGOgh#8x1h=QmkDO-EHtyQ
4) .G71k-rZDRtdd5t2WvC$DpRw@h8l
5) xcT#MzEv!-#WTV!31%1eBMi1Y93[
6) 2QpguVggooxy0wngk4A4ufsuX2Qg
7) !wn[Un46he&r@BQyh2x=.f$vx%9D
8) .S9GxuSI]Zg4.p8lbBd1t+-[wk&5
9) qG%XZVqFbV!tr&HpOOqV4v!s0-$W
10) gw%FItv_=D2W$h3zKazu@URUdqV$
Input number of chosen password or ENTER: 5
```