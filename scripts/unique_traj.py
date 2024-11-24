#script unique_traj.py
#opis dzialania: python3 unique_traj.py --help

import argparse
from ase.io import Trajectory
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.unique_structs import check_unique_structures


parser = argparse.ArgumentParser('Program sprawdzający ile jest niepowtarzających się struktur '
                                 'w populacji z pliku .traj')
parser.add_argument('filename', type=str, help='Ścieżka do pliku z populacją .traj')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

traj = Trajectory(args.filename,'r')
unique_list = check_unique_structures(traj)
print(f'Ilość unikalnych struktur w populacji: {len(unique_list)}')
unique_traj = Trajectory(f'{args.label}.traj','w')
for struct in unique_list:
    unique_traj.write(struct)