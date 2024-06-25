import sys

def read_energy_from_dat_file(file_path):
    energy_values = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) >= 2:
                try:
                    energy = float(columns[1])
                    energy_values.append(energy)
                except ValueError:
                    pass 

    return energy_values


def calculate_ensemble_average(energy_values):
    if not energy_values:
        return None

    total_energy = sum(energy_values)
    ensemble_average = total_energy / len(energy_values)
    return ensemble_average

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    energy_values = read_energy_from_dat_file(filename)

    ensemble_average_energy = calculate_ensemble_average(energy_values)

    if ensemble_average_energy is not None:
        print(f"Average Energy (kcal/mol): {ensemble_average_energy:.16f}")


if __name__ == "__main__":
    main()