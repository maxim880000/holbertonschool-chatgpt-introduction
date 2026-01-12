#!/usr/bin/python3
import sys

def factorial(n): # create factorial function 
    result = 1 # variable creation 
    while n > 1: #loops
        result *= n # result = result * n keep the new result
        n -= 1 # remove 1 to n (so that the program stops )
    return result

f = factorial(int(sys.argv[1]))
print(f) # On affiche le résultat à l'écran
