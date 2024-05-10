#! /usr/bin/env python3

import random
from pyperclip import copy
from sys import argv

passwords = []
passcount = 10
passlen = 28
alphabet = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!_-#$%@+=*&.[]"

def getpass():
    try:
        chosen = int(input("Input number of chosen password or ENTER: "))
        copy(passwords[chosen - 1])
    except:
        exit(0) 

if __name__ == "__main__":
    if len(argv) > 1:
        input_ = argv[1::]
        passlen, passcount = map(int, input_[:2])
        
    for i in range(1, passcount + 1):
        passTMP = ""
        
        for j in range(passlen):
            passTMP += random.choice(alphabet)
            
        passwords.append(passTMP)
        print(i, ") ", passTMP, sep = "")

    while (True):
        getpass()