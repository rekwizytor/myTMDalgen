#sort_pop.py
#funkcja sortujaca podana populacje w kolejnosci od najnizszej energi do najwyzszej
#sort_population(obiekt_z_populacja)

def sort_pop(population):
    sorted_structures = sorted(population, key=lambda atoms: atoms.info['pot_energy'])
    return sorted_structures
