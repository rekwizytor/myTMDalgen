#relax_pop_read.py
#opis dzialania: python3 relax_pop_read.py --help

from ase import io
from ase.io import Trajectory
import argparse
import os
import numpy as np
from pathlib import Path
from functions.calculator import get_calc


parser = argparse.ArgumentParser(description='Program relaksujący populację z podanego pliku .traj')
parser.add_argument('filename', type=str, help='Nazwa pliku z populacją')
parser.add_argument('n_atoms', type=int, help='Ilość atomów pomiędzy warstwami w wczytywanej populacji')
parser.add_argument('label', type=str, help='Etykietu plików oraz folderu, w którym zapisane zostaną pliki wyjściowe')
args = parser.parse_args()

calc = get_calc('MoS2')

population = Trajectory(args.filename, 'r')

folder_path = Path(f'{args.folder_name}')
folder_path.mkdir(parents=True, exist_ok=True)
original_directory = os.getcwd()
os.chdir(folder_path)

relaxed_traj = Trajectory(f'relaxed_{args.label}.traj', 'w')

for i, structure in enumerate(population):
    moments = [0] * (len(structure) - args.n_atoms) + [6.0] * args.n_atoms
    structure.set_initial_magnetic_moments(moments)
    label = f'structure{i+1}'
    tmp_folder_path = Path(f'{label}')
    tmp_folder_path.mkdir(parents=True, exist_ok=True)
    os.chdir(tmp_folder_path)

    try:
        structure.calc = calc
        pot_energy = structure.get_potential_energy()
        relaxed_structure = io.read('MoS2.XV')
        relaxed_structure.pbc = [True, True, False]
        relaxed_structure.info['pot_energy'] = np.round(pot_energy, 4)
        io.write(f'relaxed_{label}.xyz', relaxed_structure)
        relaxed_traj.write(relaxed_structure)
        with open(f'../energy_{args.label}.txt', 'a') as file:
            file.write(f'{i}\t{pot_energy}\n')
        print(f'Zrelaksowano strukturę nr. {i+1}')
    except Exception as e:
        print(f'Nie udało sie zrelaksować struktury {i+1}. Kod błędu: {e}')

    os.chdir(original_directory / folder_path)

os.chdir(original_directory)

print(f'Zakończono relaksację!')
