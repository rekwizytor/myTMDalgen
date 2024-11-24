#script fdf_random.py
#opis dzialania: python3 scripts/fdf_random.py --help

import argparse
from ase import io
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.gen_rand_struct import gen_rand_struct
from functions.prep_fdf import prep_fdf


parser = argparse.ArgumentParser(description='Program tworzący plik (label).fdf na podstawie dwuwarstwowej struktury o zadanych parametrach')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą (np. MoS2.xyz)')
parser.add_argument('size', type=str, help='Rozmiar generowanej struktury (np. 3x3)')
parser.add_argument('atom_symbol', type=str, help='Symbol dodowanego atomu (np. Mo, S)')
parser.add_argument('n_atoms', type=int, help='Ilość dodawanych atomów')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

atoms = gen_rand_struct(args.filename, args.size, args.atom_symbol, args.n_atoms)
io.write(f'{args.label}.xyz',atoms)
prep_fdf(atoms,args.label)