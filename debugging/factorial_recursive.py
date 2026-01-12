#!/usr/bin/python3
import sys

def factorial(n):
    # Fonction qui calcule la factorielle d'un entier n >= 0 de manière récursive
    # Paramètre n : entier non négatif
    # Retour : entier correspondant à n!
    
    if n == 0:              # Cas de base : la factorielle de 0 est 1
        return 1
    else:                   # Cas récursif : n! = n * (n-1)!
        return n * factorial(n-1)

# Récupère le nombre passé en argument au script et le convertit en entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat
print(f)
