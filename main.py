# evaluate critical Reynolds number for the primary instability of a circular
#cylinder
import subprocess
import numpy as np
import matplotlib.pyplot as plt

subprocess.call("Echo. > Results.txt", shell = True)
#selecting Reynolds number between 45 and 49 (instability appears at Re = 47)
Re_test = np.linspace(45.,49.,10)

for i in Re_test:
    string = "FreeFem++ input_test.edp -Re "+ str(i)
    print(string)
    subprocess.call(string, shell = True)
