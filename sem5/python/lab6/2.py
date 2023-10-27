def generate_pattern(n):
    matrix = []

    # Starting value for the first sub-array
    val = 0

    for i in range(n):
        row = []

        # Filling the row based on the starting value
        for j in range(n):
            row.append(val)
            val = 1 - val  # Toggles between 0 and 1

        matrix.append(row)

        # Switch the starting value for the next row
        val = 1 - val

    return matrix


def print_pattern(matrix):
    print("[", end="")
    for i, row in enumerate(matrix):
        if (i != len(matrix) - 1) and i != 0:
            print(" [", " ".join(map(str, row)), "]")
        elif i == 0:
            print("[", " ".join(map(str, row)), "]")
        else:
            print(" [", " ".join(map(str, row)), "]]")


if __name__ == "__main__":
    dimension = int(input("Enter dimension of the matrix (n x n): "))

    pattern_matrix = generate_pattern(dimension)
    print_pattern(pattern_matrix)
