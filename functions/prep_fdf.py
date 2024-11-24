#prep_fdf.py
#funkcja generujaca plik .fdf na podstawie przekazanego obiektu Atoms i etykiety pliku
#prep_fdf(obiekt_atoms, etykieta_pliku)


def prep_fdf(atoms, label):
    symbols = sorted(set(atoms.get_chemical_symbols()))
    species = {symbol: (index + 1, atoms[symbols.index(symbol)].number) for index, symbol in enumerate(symbols)}

    fdf_inside = f"""SystemName      {label}
SystemLabel     {label}
    
NumberOfAtoms          {len(atoms)}
NumberOfSpecies        {len(symbols)}
    
%block ChemicalSpeciesLabel
"""
    for element, (number, atomic_number) in species.items():
        fdf_inside += f"{number}\t{atomic_number}\t{element}\n"
    fdf_inside +="""%endblock ChemicalSpeciesLabel

LatticeConstant     1.0000 Ang 
%block LatticeVectors
"""
    cell = atoms.get_cell()
    fdf_inside += f"\t{cell[0][0]:.6f} {cell[0][1]:.6f} {cell[0][2]:.6f}\n"
    fdf_inside += f"\t{cell[1][0]:.6f} {cell[1][1]:.6f} {cell[1][2]:.6f}\n"
    fdf_inside += f"\t{cell[2][0]:.6f} {cell[2][1]:.6f} {cell[2][2]:.6f}\n"
    fdf_inside += "%endblock LatticeVectors\n\n"

    fdf_inside += "AtomicCoordinatesFormat Ang\n%block AtomicCoordinatesAndAtomicSpecies\n"
    for i, atom in enumerate(atoms):
        fdf_inside += f"\t{atom.position[0]:.6f}\t{atom.position[1]:.6f}\t{atom.position[2]:.6f}\t{species[atom.symbol][0]}\t{i + 1}\t{atom.symbol}\n"
    fdf_inside += "%endblock AtomicCoordinatesAndAtomicSpecies\n"

    fdf_inside += """
PAO.BasisSize           SZP
XC.functional           GGA
XC.authors              PBE
MeshCutoff              200.0 Ry
Spin                    polarized  

%block kgrid_Monkhorst_Pack
   8   0   0  0.0
   0   8   0  0.0
   0   0   1  0.0
%endblock Kgrid_Monkhorst_Pack

MaxSCFIterations        500
DM.NumberPulay          6                        
DM.NumberBroyden        0                        
DM.MixingWeight         0.1000000000             
DM.OccupancyTolerance   0.1000000000E-11         
DM.NumberKick           0                        
DM.KickMixingWeight     0.5000000000             
DM.Tolerance            0.1000000000E-03  
DM.UseSaveDM            .true.
DM.UseSaveXV            .true.

SolutionMethod          Diagon

MD.NumCGsteps           250                      
MD.TypeOfRun            CG                       
MD.VariableCell         F                        
MD.MaxCGDispl           0.2000000000  Bohr       
MD.MaxForceTol          0.05 eV/Ang

WriteMullikenPop        1      
WriteDenchar            .true.      
WriteKpoints            .true.      
WriteForces             .true.      
WriteDM                 .true.      
WriteXML                .true.      
WriteEigenvalues        .false.      
WriteCoorStep           .true.      
WriteMDhistory          .true.      
WriteMDXmol             .true.      
WriteCoorXmol           .true.   
"""

    with open(f'{label}.fdf', 'w') as fdf_file:
        fdf_file.write(fdf_inside)
