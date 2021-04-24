# evaluate critical Reynolds number for the primary instability of a circular
#cylinder
import subprocess
import numpy as np
import matplotlib.pyplot as plt

#preliminary
subprocess.Popen("mkdir -p Flows", shell=True)
subprocess.run("Echo. > Results.txt", shell = True)

#mesh generation
mesh_gen = "FreeFem++ FF++solvers/mesh_gen.edp"
subprocess.run(mesh_gen, shell = True)

#selecting Reynolds number between 45 and 49 (instability appears at Re = 47)
Re_test = np.linspace(45.,49.,10)

#initial guess (Stokes's flow)
ig = "FreeFem++ FF++solvers/initial_guess.edp"
subprocess.run(ig, shell = True)

#loop over Reynolds numbers
for i in Re_test:
    bf = "FreeFem++ FF++solvers/baseflow.edp -Re "+ str(i)
    subprocess.run(bf, shell = True)
    ei = "mpirun -np 1 FreeFem++-mpi FF++solvers/eig_eval.edp -Re "+ str(i)
    subprocess.run(ei, shell = True)

# plotting the Results
#read the Eigenvalues
results = open("Results.txt", 'r')
lines = results.readlines()

la_im = []
la_re = []

for i in lines:
    la_re.append(float(i.split(' ')[1]))
    la_im.append(float(i.split(' ')[2]))

results.close

#building the figure
fig, (re, im) = plt.subplots(2,1)

fig.suptitle("Eigenvalues - Reynolds")
re.plot(Re_test, la_re)

re.set(ylabel = 'Real(lambda)')
re.grid()

im.plot(Re_test, la_im)

im.set(xlabel = 'Re', ylabel = 'Imag(lambda)')
im.grid()

#save the figure
fig.savefig("Results.png")
