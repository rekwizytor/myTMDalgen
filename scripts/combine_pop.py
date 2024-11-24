#script combine_pop.py
#opis dzialania: python3 scripts/combine_pop.py --help

from ase.io import Trajectory
from ase import io
import glob
import argparse


parser = argparse.ArgumentParser(description='Program łączący struktury z rożnych plików .traj lub .xyz w jeden plik .traj.')
parser.add_argument('folderpath', type=str, help='Ścieżka do pliku z strukturami')
parser.add_argument('filename', type=str, help='Nazwa pliku wyjściowego')
args = parser.parse_args()

combined_traj = Trajectory(f'{args.filename}.traj','w')
files = glob.glob(f'{args.folderpath}/*')

for file in files:
    if file.split('.')[1] == 'xyz':
        tmp_struct = io.read(file)
        combined_traj.write(tmp_struct)
    if file.split('.')[1] == 'traj':
        tmp_traj = Trajectory(file, 'r')
        for elem in tmp_traj:
            combined_traj.write(elem)
