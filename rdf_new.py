import math
import matplotlib.pyplot as plt

def calculate_distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    return distance

def calculate_rdf(coordinates, bin_size, max_distance):
    num_oxygen = 0
    num_bins = int(max_distance / bin_size)
    rdf = [0] * num_bins

    oxygen_indices = []
    for i, atom in enumerate(coordinates):
        if atom[0] == 'O':
            oxygen_indices.append(i)
            num_oxygen += 1

    for i in range(num_oxygen):
        for j in range(i + 1, num_oxygen):
            atom1 = coordinates[oxygen_indices[i]][1:]
            atom2 = coordinates[oxygen_indices[j]][1:]
            distance = calculate_distance(atom1, atom2)
            if distance < max_distance:
                bin_index = int(distance / bin_size)
                rdf[bin_index] += 2

    normalization_factor = 4 * math.pi * num_oxygen / (3 * (num_oxygen - 1) * bin_size**3)
    rdf = [value / normalization_factor for value in rdf]

    return rdf

def read_xyz_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        num_atoms = int(file.readline())
        file.readline()
        for _ in range(num_atoms):
            line = file.readline().split()
            atom = line[0]
            x, y, z = map(float, line[1:4])
            coordinates.append((atom, x, y, z))
    return coordinates

def write_rdf_file(rdf, bin_size, file_path):
    with open(file_path, 'w') as file:
        for i, value in enumerate(rdf):
            distance = (i + 0.5) * bin_size
            file.write(f'{distance:.3f} {value}\n')

def main():
    xyz_file = 'wat_dump.xyz'
    bin_size = 0.1
    max_distance = 10.0
    rdf_file = 'rdf.txt'

    coordinates = read_xyz_file(xyz_file)

    rdf = calculate_rdf(coordinates, bin_size, max_distance)

    write_rdf_file(rdf, bin_size, rdf_file)

    def plot_data_from_file(file_path):
        x = []
        y = []

        with open(file_path, 'r') as file:
            for line in file:
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

        plt.plot(x, y)
        plt.xlabel('r (Å)')
        plt.ylabel('g$_{O-O}$(r)')
        plt.title('RDF Water')
        plt.show()

    file_path = 'rdf.txt' 
    plot_data_from_file(file_path)

    print("RDF calculation completed.")

if __name__ == '__main__':
    main()
