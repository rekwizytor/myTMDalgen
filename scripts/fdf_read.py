#script fdf_read.py
#opis dzialania: python3 scripts/fdf_read.py --help

from ase import io
import argparse
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.prep_fdf import prep_fdf


parser = argparse.ArgumentParser(description='Program tworzący plik (label).fdf na podstawie przekazanego pliku ze strukturą (filename)')
parser.add_argument('filename', type=str, help="Nazwa pliku ze strukturą")
parser.add_argument('label', type=str, help="Etykieta pliku wyjściowego")
args = parser.parse_args()

prep_fdf(io.read(args.filename), args.label)
