def extract_lowest_y(filename):
    lowest_y = None
    corresponding_x = None

    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                x, y = map(float, line.split())
                if lowest_y is None or y < lowest_y:
                    lowest_y = y
                    corresponding_x = x

    return corresponding_x

filename = "evsframe.dat"
lowest_x = extract_lowest_y(filename)
print(lowest_x)
