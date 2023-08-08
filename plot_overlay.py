import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('processed_file_O-O_rdf.dat')
data2 = np.loadtxt('soper_2007_O-O.dat')

plt.figure(figsize=(8, 6))

plt.plot(data1[:, 0], data1[:, 1], label='Simulation Data', color='black', linestyle='-', linewidth=2)

plt.plot(data2[:, 0], data2[:, 1], label='Soper 2007 O-O RDF', color='red', linestyle='-', linewidth=2)

plt.xlabel('r / Å', fontsize = 14)
plt.ylabel('g(r) / -', fontsize = 14)
plt.title('Comparision of Data from Experiment with Simulation (CHOLi.ff, 300K, 1 atm)', fontsize = 18)
plt.legend()

plt.grid(True)
plt.show()