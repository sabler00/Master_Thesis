def shift_data(x_values, y_values, shift_amount):
    shifted_y_values = [y - shift_amount for y in y_values]
    return list(zip(x_values, shifted_y_values))

def read_data(input_file_path):
    with open(input_file_path, 'r') as file:
        next(file)
        data = [list(map(float, line.strip().split())) for line in file]
    return zip(*data)

def write_shifted_data(output_file_path, shifted_data):
    with open(output_file_path, 'w') as file:
        for data_point in shifted_data:
            file.write(" ".join(map(str, data_point)) + "\n")


# Example usage
input_file_path = 'soper_2007_H-H.dat'
output_file_path = 'soper_2007_H-H_shifted.dat'
shift_amount = 4.0024

# Read data from the input file
x_values, y_values = read_data(input_file_path)

# Shift the y-values by -4.0024
shifted_data = shift_data(x_values, y_values, shift_amount)

# Write the shifted data to the output file
write_shifted_data(output_file_path, shifted_data)