#script struct_crossover.py
#opis dzialania: python3 scripts/struct_crossover.py --help

import argparse
from ase import io
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.crossover import crossover

parser = argparse.ArgumentParser(description='Program działający operatorem krzyżowania na struktury wczytane '
                                             'z dwóch podanych plików')
parser.add_argument('filenames', nargs=2, type=str, help='Nazwy dwoch plikow ze strukturami rodzicow')
parser.add_argument('n', type=int, help='Liczba atomów wymienianych podczas krzyżowania')
parser.add_argument('struct_filename', type=str, help='Nazwa/ścieżka do pliku z podstawową '
                                                      'strukturą dichalkogenka (np. MoS2.xyz)')
parser.add_argument('struct_size', type=str, help='Rozmiar struktur (np. 3x3)')
parser.add_argument('label', type=str, help='Etykieta pliku wyjściowego')
args = parser.parse_args()

parent1 = io.read(args.filenames[0])
parent2 = io.read(args.filenames[1])
child = crossover(parent1, parent2, args.n, args.struct_filename, args.struct_size)
io.write(f'{args.label}.xyz', child)