#script struct_mutation.py
#opis dzialania: python3 scripts/struct_mutation.py --help

import argparse
from ase import io
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.mutation import mutation

parser = argparse.ArgumentParser(description='Program działający operatorem mutacji na strukturę wczytaną z podanego pliku')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

atoms = io.read(args.filename)
mutation_atoms = mutation(atoms)
io.write(f'{args.label}.xyz', mutation_atoms)