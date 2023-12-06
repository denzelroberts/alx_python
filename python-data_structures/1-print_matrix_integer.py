def print_matrix_integer(matrix=[[]]):
        # Loop over each row
    for i in range(len(matrix)):
        # Loop over each column in the current row
        for j in range(len(matrix[i])):
            # Print element at row i, column j
            print("{:d}".format(matrix[i][j]),end=' ')
        # Print a new line after each row
        print()
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]