import numpy as np

def read_xyz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_z_values(lines, atom_indices):
    z_values = []
    # Assuming the header has two lines and each step starts with a new set of atom data
    step_size = 1481  # Number of atoms per step
    header_lines = 2
    num_steps = len(lines) // (step_size + header_lines)
    
    for step in range(num_steps):
        start = step * (step_size + header_lines) + header_lines
        end = start + step_size
        step_lines = lines[start:end]
        
        for index in atom_indices:
            atom_data = step_lines[index-1].split()
            z_values.append(float(atom_data[3]))
    
    return z_values

def calculate_average_z(file_path, indices_group1, indices_group2):
    lines = read_xyz(file_path)
    atom_indices = indices_group1 + indices_group2
    z_values = extract_z_values(lines, atom_indices)
    
    avg_z_group1 = np.mean(z_values[:len(indices_group1)])
    avg_z_group2 = np.mean(z_values[len(indices_group1):])
    
    return avg_z_group1, avg_z_group2

# Indices of atoms
indices_group1 = list(range(1153, 1440))  # 1153 to 1440
indices_group2 = list(range(1441, 1480))  # 1441 to 1480

# File path to the .xyz file
file_path = '/home/sal/qmcf_examples/graphite_qmmm_setup/graphite-md-02.xyz'

# Calculate the average z values
avg_z_group1, avg_z_group2 = calculate_average_z(file_path, indices_group1, indices_group2)

print(f"Average z value for atoms 1153 to 1440: {avg_z_group1}")
print(f"Average z value for atoms 1441 to 1480: {avg_z_group2}")
