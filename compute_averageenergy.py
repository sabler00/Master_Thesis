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


if __name__ == "__main__":
    fold = input("system: ")
    dat_file_path = "npt_stack_energy_300K/ffield/" + fold + "/energy.dat"

    energy_values = read_energy_from_dat_file(dat_file_path)

    ensemble_average_energy = calculate_ensemble_average(energy_values)

    if ensemble_average_energy is not None:
        print(f"Ensemble Average Energy: {ensemble_average_energy:.4f}")
    else:
        print("Error: No valid energy values found in the file.")
