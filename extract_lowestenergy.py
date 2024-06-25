import sys

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


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    lowest_y = extract_lowest_y(filename)

    if lowest_y is not None:
        print(f"Lowest x val: {lowest_y}")


if __name__ == "__main__":
    main()
