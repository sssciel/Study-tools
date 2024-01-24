#! /usr/bin/env python3

from sympy import sympify
from pyperclip import copy
from sys import argv

alphabet = "0123456789ABCDEF"

def dec_to_other(n, base):
    alphabet_ = alphabet[:base]
    
    result = ""
    
    while n > 0:
        result = alphabet_[n % base] + result
        n = n // base
        
    return result

if len(argv) > 1:
    input_ = argv[1::]
    old_base, new_base = map(int, input_[:2])
    input_number = input_[2]
else:
    old_base, new_base = map(int, input("Base numeral system and new system: ").split())
    input_number = input("Number or expression: ")
    
if (not input_number.isdigit()):
    input_number = str(sympify(input_number))
        
result = 0
input_number = int(input_number, old_base)
    
match new_base:
    case 2:
        result = bin(input_number)[2::]
    case 8:
        result = oct(input_number)
    case 16:
        result = hex(input_number) 
    case _:
        result = dec_to_other(input_number, new_base)
            
print("Result:", result)
copy(result)