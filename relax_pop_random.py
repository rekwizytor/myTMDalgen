#relax_pop_random.py
#opis dzialania: python3 relax_pop_random.py --help

import argparse
from ase import io
from ase.io import Trajectory
from pathlib import Path
import os
import numpy as np
from functions.calculator import get_calc
from functions.gen_rand_struct import gen_rand_struct

parser = argparse.ArgumentParser(description='Program przygotowujący populację zrelaksowanych struktur o zadanych parametrach.')
parser.add_argument('pop_size', type=int, help='Rozmiar populacji')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą wejściową (np. MoS2.xyz)')
parser.add_argument('size', type=str, help='Rozmiar struktur (np. 3x3)')
parser.add_argument('atom_symbol', type=str, help='Symbol dodowanego atomu (np. Mo, S)')
parser.add_argument('n_atoms', type=int, help='Ilość dodawanych atomów')
parser.add_argument('label', type=str, help='Etykieta plików i folderu, w którym zostaną zapisane pliki wyjściowe')
args = parser.parse_args()

calc = get_calc('MoS2')

folder_path = Path(f'{args.label}')
folder_path.mkdir(parents=True, exist_ok=True)
original_directory = os.getcwd()
os.chdir(folder_path)

not_relaxed_traj = Trajectory(f'not_relaxed_{args.label}.traj', 'w')
relaxed_traj = Trajectory(f'relaxed_{args.label}.traj', 'w')

candidates_counter = 0
relax_counter = 0

while len(relaxed_traj) < args.pop_size:
    tmp_struct = gen_rand_struct(f'{original_directory}/{args.filename}', args.size, args.atom_symbol, args.n_atoms)
    #moments = [0] * (len(tmp_struct) - args.n_atoms) + [6.0] * args.n_atoms
    #tmp_struct.set_initial_magnetic_moments(moments)
    not_relaxed_traj.write(tmp_struct)
    candidates_counter += 1
    label = f'cand{candidates_counter}'
    tmp_folder_path = Path(f'{label}')
    tmp_folder_path.mkdir(parents=True, exist_ok=True)
    os.chdir(tmp_folder_path)

    try:
        tmp_struct.calc = calc
        pot_energy = tmp_struct.get_potential_energy()
        relax_counter += 1
        relaxed_atoms = io.read('MoS2.XV')
        relaxed_atoms.pbc = [True, True, False]
        relaxed_atoms.info['pot_energy'] = np.round(pot_energy, 4)
        io.write(f'relaxed_{label}.xyz', relaxed_atoms)
        relaxed_traj.write(relaxed_atoms)
        with open(f'../energy_{args.label}.txt', 'a') as file:
            file.write(f'{relax_counter}\t{pot_energy}\n')
        print(f'Zrelaksowano kandydata nr. {candidates_counter}')
    except Exception as e:
        print(f'Nie udało sie zrelaksować kandydata {candidates_counter}. Kod błędu: {e}')

    os.chdir(original_directory / folder_path)

os.chdir(original_directory)

print(f'Zakończono! Liczba zrelaksowanych struktur: {relax_counter}')
