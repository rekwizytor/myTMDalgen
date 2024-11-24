#unique_structs
#funkcja zwracajaca liste unikalnych struktur wystepujacych w podanej jako argument populacji

from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.io.ase import AseAtomsAdaptor


def check_unique_structures(atoms_list):
    matcher = StructureMatcher()
    unique_structures = []
    unique_atoms = []

    for atoms in atoms_list:
        structure = AseAtomsAdaptor.get_structure(atoms)

        is_unique = True
        for unique_structure in unique_structures:
            if matcher.fit(structure, unique_structure):
                is_unique = False
                break

        if is_unique:
            unique_structures.append(structure)
            unique_atoms.append(atoms)

    return unique_atoms