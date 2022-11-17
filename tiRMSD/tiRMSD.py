NUMBER = 10
PDB_PATH = "pdb/trp-cage/"
import numpy as np
import MDAnalysis
from MDAnalysis.analysis import align, rms

pre = MDAnalysis.Universe(PDB_PATH + "x00000.pdb")

for i in range(NUMBER - 1):
  i2 = i + 1
  pdb = MDAnalysis.Universe(PDB_PATH+"x{:05d}.pdb".format(i2))
  pre_CA = pre.select_atoms("name CA")
  pdb_CA = pdb.select_atoms("name CA")
  pre0 = pre_CA.positions - pre_CA.center_of_mass()
  pdb0 = pdb_CA.positions - pdb_CA.center_of_mass()
  R, rmsd = align.rotation_matrix(pre0, pdb0)
  print (rmsd)
  pre = pdb
