#script sort_pop.py
#opis dzialania: python3 scripts/sort_pop.py --help

import argparse
from ase.io import Trajectory
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.sort_pop import sort_pop


parser = argparse.ArgumentParser(description='Program sortujący populację z pliku .traj.')
parser.add_argument('folderpath', type=str, help='Ścieżka do pliku z populacją .traj')
parser.add_argument('filename', type=str, help='Nazwa pliku wyjściowego')
args = parser.parse_args()

traj = Trajectory(args.folderpath, 'r')
sorted_population = sort_pop(traj)
sorted_traj = Trajectory(f'{args.filename}.traj', 'w')
for struct in sorted_population:
    sorted_traj.write(struct)
