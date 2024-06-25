import numpy as np
from statistics import mean

def read_xyz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_z_values(lines, atom_indices):
    z_values = []
    step_size = 1480
    header_lines = 3
    num_steps = len(lines) // 1483

    for step in range(num_steps):
            start = step * (step_size + header_lines)
            end = start + step_size + header_lines
            step_lines = lines[start:end]
            
            for index in atom_indices:
                if len(step_lines[index].split()) >= 4:
                    atom_data = step_lines[index].split()
                    try:
                        z_value = float(atom_data[2])
                        z_values.append(z_value)
                    except (IndexError, ValueError):
                        print(f"Error extracting z-value from line {index}: Invalid format or missing data.")
                else:
                    print(f"Warning: Line {index} does not have enough columns.")

    return z_values
  
def calculate_average_z(file_path, indices_surface, indices_substrate):
    lines = read_xyz(file_path)
    atom_indices = indices_surface + indices_substrate
    z_values = extract_z_values(lines, atom_indices)
    
    avg_z_surface = []
    avg_z_substrate = []

    avg_z_surface.append(mean(z_values[:288] ) )
    avg_z_substrate.append(mean(z_values[289:] ) )
    
    return avg_z_surface, avg_z_substrate

indices_surface = list(range(1153, 1440))
indices_substrate = list(range(1441, 1480)) 

# File path to the .xyz file
file_path = '/home/sal/qmcf_examples/graphite_qmmm_setup/graphite-md-02.xyz'

avg_z_surface, avg_z_substrate = calculate_average_z(file_path, indices_surface, indices_substrate)

print(f"Average z value for atoms 1152 to 1440: {avg_z_surface}")
print(f"Average z value for atoms 1441 to 1480: {avg_z_substrate}")