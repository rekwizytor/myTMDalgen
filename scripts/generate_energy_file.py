#script generate_energy_file.py
#opis dzialania: python3 scripts/generate_energy_file.py --help

import argparse
import sys, os
from ase.io import Trajectory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.gen_energy_file import gen_energy_file

parser = argparse.ArgumentParser(description='Program generujący plik (.txt) z energiami struktur z pliku .traj')
parser.add_argument('filename', type=str, help='Nazwa pliku .traj')
parser.add_argument('out_filename', type=str, help='Nazwa pliku wyjściowego')
args = parser.parse_args()

traj = Trajectory(args.filename, 'r')
gen_energy_file(traj, args.out_filename)