from __future__ import print_function

import numpy as np

import cellconstructor as CC
import cellconstructor.Phonons


import sys, os
total_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(total_path)



T = 100

# Load a simple dynamical matrix
dyn = CC.Phonons.Phonons("../TestSymmetriesSupercell/Sym.dyn.", 3)

# Get the upsilon matrix for the supercell
superdyn = dyn.GenerateSupercellDyn(dyn.GetSupercell())
ups1 = superdyn.GetUpsilonMatrix(T)
ups2 = dyn.GetUpsilonMatrix(T)

delta = np.max(np.abs( (ups1 - ups2)))
assert delta < 1e-7

