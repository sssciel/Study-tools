#! /usr/bin/env python3

from sympy import sympify
from pyperclip import copy
from sys import argv

alphabet = "0123456789ABCDEF"

# Not standart converter from 10 to base. Max base is 16.
def dec_to_other(n, base):
    alphabet_ = alphabet[:base]
    
    result = ""
    
    while n > 0:
        result = alphabet_[n % base] + result
        n = n // base
        
    return result

# Converter from n to k.
def system_converter(old_base, new_base, n):
    if (not n.isdigit()):
        n = str(sympify(n))
            
    result = 0
    n = int(n, old_base)
        
    match new_base:
        case 2:
            result = bin(n)[2::]
        case 8:
            result = oct(n)
        case 16:
            result = hex(n) 
        case _:
            result = dec_to_other(n, new_base)
    return result

if __name__ == "__main__": 
    if len(argv) > 1:
        input_ = argv[1::]
        old_base, new_base = map(int, input_[:2])
        input_number = input_[2]
    else:
        old_base, new_base = map(int, input("Base numeral system and new system: ").split())
        input_number = input("Number or expression: ")
    result = system_converter(old_base, new_base, input_number)
    print("Result:", result)
    copy(result)