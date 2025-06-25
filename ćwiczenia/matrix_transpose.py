EXAMPLE_MATRIX = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def pretty_print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def matrix_transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def main():
    print('Original matrix:')
    pretty_print_matrix(EXAMPLE_MATRIX)
    print('\nTransposed matrix:')
    pretty_print_matrix(matrix_transpose(EXAMPLE_MATRIX))


if __name__ == "__main__":
    main()