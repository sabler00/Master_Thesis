import matplotlib.pyplot as plt

def plot_data_from_file(file_path):
    datrow = []
    rdfcol2 = []

    with open(file_path, 'r') as file:
        lines_after_4 = file.readlines()[4:]
        for lines_after_4 in file:
            columns = lines_after_4.strip().split()
            rowval = float(columns[1])
            col2val = float(columns[2])
            datrow.append(rowval)
            rdfcol2.append(col2val)


    plt.plot(datrow, rdfcol2)
    plt.xlabel('r / Å')
    plt.ylabel('g(r) / -')
    plt.title('RDF Water with one Na atom')
    plt.show()

file_path = 'tmp_ffield_with_na.dat'
plot_data_from_file(file_path)
