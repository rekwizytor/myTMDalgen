#script prep_population.py
#opis dzialania: python3 scripts/prep_population.py --help

import sys, os
import argparse
from ase.io.trajectory import Trajectory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.gen_rand_struct import gen_rand_struct


parser = argparse.ArgumentParser(description='Program generujący populację struktur o zadanych parametrach.')
parser.add_argument('pop_size', type=int, help='Ilość obiektów w populacji')
parser.add_argument('filename', type=str, help='Nazwa pliku ze strukturą (np. MoS2.xyz)')
parser.add_argument('size', type=str, help='Rozmiar struktur (np. 3x3)')
parser.add_argument('atom_symbol', type=str, help='Symbol dodowanego atomu (np. Mo, S)')
parser.add_argument('n_atoms', type=int, help='Ilość dodawanych atomów')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

def prep_population(pop_size, structure_file_name, size, atom_symbol, n_atoms, label):
    new_population = Trajectory(f'{label}.traj', 'w')
    for i in range(pop_size):
        new_population.write(gen_rand_struct(structure_file_name, size, atom_symbol, n_atoms))
    return 0


prep_population(args.pop_size, args.filename, args.size, args.atom_symbol, args.n_atoms, args.label)
