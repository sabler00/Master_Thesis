import matplotlib.pyplot as plt

file_path = 'density_ffield.dat'
with open(file_path, 'r') as file:
    lines = file.readlines()[2:]

data = [line.strip().split() for line in lines]
x_values = [float(entry[0]) for entry in data]
y_values = [float(entry[1]) for entry in data]

plt.plot(x_values, y_values)
plt.xlabel(r"frames / -")
plt.ylabel(r"$\rho$ / g cm⁻³")
plt.title('Water density at 30K using ffield.reax')
plt.grid(True)
plt.show()
