# evaluate critical Reynolds number for the primary instability of a circular
#cylinder
import subprocess
import numpy as np
import matplotlib.pyplot as plt

#preliminary
subprocess.Popen("mkdir -p Flows", shell=True)
subprocess.call("Echo. > Results.txt", shell = True)

#mesh generation
mesh_gen = "FreeFem++ mesh_gen.edp"
subprocess.call(mesh_gen, shell = True)

#selecting Reynolds number between 45 and 49 (instability appears at Re = 47)
Re_test = np.linspace(45.,49.,10)

#initial guess (Stokes's flow)
ig = "FreeFem++ initial_guess.edp"
subprocess.call(ig, shell = True)

#loop over Reynolds numbers
for i in Re_test:
    bf = "FreeFem++ baseflow.edp -Re "+ str(i)
    subprocess.call(bf, shell = True)
    ei = "mpirun -np 2 FreeFem++-mpi eig_eval.edp -Re "+ str(i)
    subprocess.call(ei, shell = True)
