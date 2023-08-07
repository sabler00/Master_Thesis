import matplotlib.pyplot as plt

def read_and_parse_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            for _ in range(4):
                next(input_file)
            
            data_columns = []
            
            for line in input_file:
                columns = line.strip().split()
                data_columns.append(columns[1:3])
            
            with open(output_filename, 'w') as output_file:
                for columns in data_columns:
                    output_line = ' '.join(columns) + '\n'
                    output_file.write(output_line)
            
            print(f"Parsed data written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Input file '{input_filename}' not found.")
    except Exception as e:
        print("An error occurred:", e)

input_filename = 'Na-O.dat'
output_filename = 'processed_file_' + input_filename + '.dat'
read_and_parse_file(input_filename, output_filename)

    
def plot_data_from_file(file_path):
        x = []
        y = []

        with open(file_path, 'r') as file:
            for line in file:
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

        plt.plot(x, y)
        plt.xlabel('r / Å')
        plt.ylabel('g$_{Na-O}$(r) / - ')
        plt.title('Sodium Solvation Shells')
        plt.show()

file_path = output_filename
plot_data_from_file(file_path)
