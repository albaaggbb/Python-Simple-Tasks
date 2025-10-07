import os
import numpy as np
import scipy.spatial

def read_atom_coordinates(line):
    """Extracts the coordinates from a line of a PDB file starting with ATOM."""
    if line.startswith("ATOM  "):
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        return [x, y, z]

def get_coordinates(pdb_filename):
    """Reads a PDB file and returns the atomic coordinates as a NumPy array."""
    base_path = os.path.join(os.path.dirname(__file__), "files")  # ensures path relative to script
    pdb_file = os.path.join(base_path, pdb_filename)
    
    if not os.path.isfile(pdb_file):
        raise FileNotFoundError(f"{pdb_file} does not exist. Make sure the file is in bioinformatics/files/")
    
    coords = []
    with open(pdb_file) as f:
        for line in f:
            atom = read_atom_coordinates(line)
            if atom:
                coords.append(atom)
    return np.array(coords)

# Load coordinates from PDB files
coords_A = get_coordinates("1PPE_rec.pdb")
coords_B = get_coordinates("1PPE_lig.pdb")

# Compute all pairwise distances
distances = scipy.spatial.distance.cdist(coords_A, coords_B)

# Find atoms within 5 Å
indices_within_5 = np.where(distances <= 5)

# Count unique atoms in contact
atoms_A_in_contact = len(set(indices_within_5[0]))
atoms_B_in_contact = len(set(indices_within_5[1]))

print("Atoms of A in contact with B:", atoms_A_in_contact)
print("Atoms of B in contact with A:", atoms_B_in_contact)
print("Total atoms in contact:", atoms_A_in_contact + atoms_B_in_contact)
