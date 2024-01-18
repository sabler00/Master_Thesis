import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('soper_2007_O-H.dat')
plt.figure(figsize=(8, 6))


plt.plot(data[:, 0], data[:, 1], label='Simulation Data', color='black', linestyle='-', linewidth=2)
plt.xlabel('r / Å', fontsize = 14)
plt.ylabel('g(r) / -', fontsize = 14)
plt.title('Comparision of Data from Experiment with Simulation (CHOLi.ff, 300K, 1 atm)', fontsize = 18)
plt.legend()
plt.grid(True)
plt.show()