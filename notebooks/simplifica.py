#!/usr/bin/env python
# encoding: utf-8
"""
Script que lee un fichero, elimina espacios en blanco y símbolos de puntuación, y pone todo en minúsculas.
"""

import argparse
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="Fichero de entrada")
    args = parser.parse_args()
    filename = args.source_file

    with open(args.source_file, 'r') as f:
        for line in f:

            # Todos los caracteres en string.punctuation se mapean con un espacio en blanco
            line = line.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
            print(line.lower().strip())

if __name__ == '__main__':
    main()
