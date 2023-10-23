def shift_y_values(input_file, output_file, shift_value):
    try:
        with open(input_file, 'r') as input_data, open(output_file, 'w') as output_data:
            for line in input_data:
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        x_value = float(parts[0])
                        y_value = float(parts[1])
                        shifted_y = y_value + shift_value
                        output_data.write(f"{x_value} {shifted_y}\n")
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
                else:
                    print(f"Skipping line with incorrect format: {line}")
        print(f"Shifted y-values by {shift_value} and saved to {output_file}")
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    input_file = "input.dat"  # Replace with your input file name
    output_file = "output.dat"  # Replace with your output file name
    shift_value = 5.0  # Replace with the value by which you want to shift the y-values

    shift_y_values(input_file, output_file, shift_value)
