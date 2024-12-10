import argparse
from functions.gen_random_pop import gen_random_pop
from functions.prep_gen import prep_gen
from functions.calculator import get_calc


parser = argparse.ArgumentParser(description='Program ewolujący zadaną ilość pokoleń na podstawie początkowej populacji z pliku .traj')
parser.add_argument('n_generations', type=int, help='Liczba pokoleń')
parser.add_argument('pop_size', type=int, help='Ilość osobników w populacji')
parser.add_argument('n_best', type=int, help='Ilość najlepszych osobnikow z poprzedniego pokolenia, ktorzy trafia do nowego pokolenia')
parser.add_argument('n_child', type=int, help='Ilość nowych osobników tworzonych poprzez krzyzowanie')
parser.add_argument('n_mut', type=int, help='Ilość nowych osobników tworzonych poprzez mutację')
parser.add_argument('struct_filename', type=str, help='Nazwa pliku ze strukturą dichalkogenka')
parser.add_argument('size', type=str, help='Rozmiar struktur w populacji (np. 3x3)')
parser.add_argument('n_atoms', type=int, help='Ilość atomów miedzy warstwami w strukturach w populacji')
parser.add_argument('n_change', type=int, help='Ilość atomów wymienianych podczas krzyżowania')
parser.add_argument('atom_symbol', type=str, help='Symbol atomów między warstwami')
parser.add_argument('mag_moment', type=float, help='Początkowy moment magnetyczny nadawany atomom między warstwami')
parser.add_argument('label', type=str, help='Etykieta nadawana plikom kalkulatora Siesta (np. MoS2)')
args = parser.parse_args()

#ustawienie kalkulatora wykorzystywanego do obliczen
calc = get_calc(args.label)

#wygenerowanie populacji poczatkowej
gen_random_pop(args.pop_size, args.struct_filename, args.size, args.n_atoms, args.atom_symbol,
               args.calc, args.mag_moment, args.label, 'pop0')

#przygotowanie kolejnych pokolen
for i in range(args.n_generations-1):
    prep_gen(f'sorted_pop{i}.traj', args.pop_size, args.n_best, args.n_child, args.n_mut,
                    args.struct_filename, args.size, args.n_atoms, args.n_change, args.atom_symbol,
                    calc, args.mag_moment, args.label, f'pop{i+1}')