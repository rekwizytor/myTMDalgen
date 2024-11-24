#relax_read.py
#opis dzialania: python3 relax_read.py --help

from ase import io
import argparse
import os
import numpy as np
from pathlib import Path
from functions.calculator import get_calc


parser = argparse.ArgumentParser(description='Program relaksujący strukturę dwuwarstwową z podanego pliku')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą')
parser.add_argument('n_atoms', type=int, help='Ilość atomów pomiędzy warstwami w wczytywanej struktrze')
parser.add_argument('label', type=str, help='Etykieta plików i folderu, w którym zapisane zostaną pliki wyjściowe')
args = parser.parse_args()

calc = get_calc(args.label)

atoms = io.read(args.filename)
moments = [0] * (len(atoms)-args.n_atoms) + [6.0]*args.n_atoms
atoms.set_initial_magnetic_moments(moments)

folder_path = Path(f'{args.label}')
folder_path.mkdir(parents=True, exist_ok=True)
original_directory = os.getcwd()
os.chdir(folder_path)

try:
    atoms.calc = calc
    pot_energy = atoms.get_potential_energy()
    relaxed_atoms = io.read(f'{args.label}.XV')
    relaxed_atoms.pbc = [True, True, False]
    relaxed_atoms.info['pot_energy'] = np.round(pot_energy, 4)
    io.write(f'relaxed_{args.label}.xyz', relaxed_atoms)
except Exception as e:
        print(f'Nie udało się zrelaksować wczytanej struktury. Błąd: {e}')

os.chdir(original_directory)
