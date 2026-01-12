#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):
# On commence à 1 pour **ignorer le nom du fichier**
# len(sys.argv) = nombre total d'éléments (nom du fichier + arguments)
	print(sys.argv[i])
	# Affiche l'argument numéro i