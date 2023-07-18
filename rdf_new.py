import math
import matplotlib.pyplot as plt

def calculate_distance(coord1, coord2):
    """Calculates the distance between two coordinates."""
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

    # Find the oxygen atom indices
    oxygen_indices = []
    for i, atom in enumerate(coordinates):
        if atom[0] == 'O':
            oxygen_indices.append(i)
            num_oxygen += 1

    # Calculate RDF for O-O pairs
    for i in range(num_oxygen):
        for j in range(i + 1, num_oxygen):
            atom1 = coordinates[oxygen_indices[i]][1:]
            atom2 = coordinates[oxygen_indices[j]][1:]
            distance = calculate_distance(atom1, atom2)
            if distance < max_distance:
                bin_index = int(distance / bin_size)
                rdf[bin_index] += 2  # Count both directions

    # Normalize RDF
    normalization_factor = 4 * math.pi * num_oxygen / (3 * (num_oxygen - 1) * bin_size**3)
    rdf = [value / normalization_factor for value in rdf]

    return rdf

def read_xyz_file(file_path):
    """Reads an XYZ format file and returns a list of coordinates."""
    coordinates = []
    with open(file_path, 'r') as file:
        num_atoms = int(file.readline())
        file.readline()  # Skip the comment line
        for _ in range(num_atoms):
            line = file.readline().split()
            atom = line[0]
            x, y, z = map(float, line[1:4])
            coordinates.append((atom, x, y, z))
    return coordinates

def write_rdf_file(rdf, bin_size, file_path):
    """Writes the RDF values to a file."""
    with open(file_path, 'w') as file:
        for i, value in enumerate(rdf):
            distance = (i + 0.5) * bin_size
            file.write(f'{distance:.3f} {value}\n')

def main():
    xyz_file = 'wat_dump.xyz'  # Replace with your input file
    bin_size = 0.1  # Distance bin size
    max_distance = 10.0  # Maximum distance to consider
    rdf_file = 'rdf.txt'  # Output file for RDF

    # Read XYZ file
    coordinates = read_xyz_file(xyz_file)

    # Calculate RDF for O-O pairs
    rdf = calculate_rdf(coordinates, bin_size, max_distance)

    # Write RDF to file
    write_rdf_file(rdf, bin_size, rdf_file)

    print("RDF calculation completed.")

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

    print("RDF calculation completed.")

    file_path = 'rdf.txt'  # Replace with your file path
    plot_data_from_file(file_path)

if __name__ == '__main__':
    main()
