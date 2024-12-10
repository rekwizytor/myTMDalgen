#relax_random.py
#opis dzialania: python3 relax_random.py --help

import argparse
from ase import io
from pathlib import Path
import os
import numpy as np
from functions.calculator import get_calc
from functions.gen_rand_struct import gen_rand_struct

parser = argparse.ArgumentParser(description='Program relaksujący losową dwuwarstwową strukturę o zadanych parametrach')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą wejściową (np. MoS2.xyz)')
parser.add_argument('size', type=str, help='Rozmiar generowanej struktury (np. 3x3)')
parser.add_argument('atom_symbol', type=str, help='Symbol dodowanego atomu (np. Mo, S)')
parser.add_argument('n_atoms', type=int, help='Ilość dodawanych atomów')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

calc = get_calc(args.label)

atoms = gen_rand_struct(args.filename, args.size, args.atom_symbol, args.n_atoms)
moments = [0] * (len(atoms)-args.n_atoms) + [6.0]*args.n_atoms
atoms.set_initial_magnetic_moments(moments)

folder_path = Path(f'{args.label}')
folder_path.mkdir(parents=True, exist_ok=True)
original_directory = os.getcwd()
os.chdir(folder_path)

io.write(f'random_{args.label}.xyz', atoms)

try:
    atoms.calc = calc
    pot_energy = atoms.get_potential_energy()
    relaxed_atoms = io.read(f'{args.label}.XV')
    relaxed_atoms.pbc = [True, True, False]
    relaxed_atoms.info['pot_energy'] = np.round(pot_energy, 4)
    io.write(f'relaxed_{args.label}.xyz', relaxed_atoms)
    print(f'Udało się zrelaksować wygenerowaną strukturę.')
except Exception as e:
        print(f'Nie udało się zrelaksować wygenerowanej struktury. Błąd: {e}')

os.chdir(original_directory)
