#script prep_sctructure.py
#opis dzialania: python3 scripts/prep_structure_close.py --help

from ase import io
import argparse
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.prep_struct import prep_struct

parser = argparse.ArgumentParser(description='Program generujacy na podstawie pliku .xyz dwuwarstwową strukturę o zadanym rozmiarze.')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą (np. MoS2.xyz)')
parser.add_argument('size', type=str, help='Rozmiar generowanej struktury (np. 3x3)')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()


structure = prep_struct(args.filename, args.size)
io.write(f'{args.label}.xyz', structure)