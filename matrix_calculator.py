def matrix():
    """
    A matrix 3x3 former, it receive 9 inputs, and return a callable list in input order.
    (element 11, element 12, element 13, element  21....)
    :return: a callable list with 9 integer numbers
    """
    matrix = [[], [], []]
    for line in range(0, 3):
        for column in range(0, 3):
            while True:
                locale = str(input(f'Type the [{line + 1} x {column + 1}] element: '))
                if locale.strip() == '' or locale.isalpha():
                    print('Invalid integer number, try again.')
                else:
                    matrix[line].append(int(locale))
                    break
    print('Matrix successfully created!')
    return matrix


def printmatrix(matrix):
    """
    Just a better looking print for a matrix in 3x3 style. Requires a 9 elements list.
    :param matrix: a list with 9 integer numbers.
    """
    for line in range(0, 3):
        if line != 0:
            print()
        for column in range(0, 3):
            print(f'[ {str(matrix[line][column]).center(5)} ]', end='')


def matrixmultip(matrix_a, matrix_b):
    """
    A function that multiplies two matrices, and return a callable list with the result.
    :param matrix_a: First matrix to be added at the multiplication;
    :param matrix_b: Second matrix to be added at the multiplication;
    :return: A callable list containing 9 elements (3x3 matrix).
    """
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def determinant(matrix):
    """
    Prints the determinant of a matrix right ahead.
    :param matrix: The matrix to be used.
    """
    positive = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] * matrix[2][1])
    negative = (matrix[2][0] * matrix[1][1] * matrix[0][2]) + (matrix[2][1] * matrix[1][2] * matrix[0][0]) + (matrix[2][2] * matrix[1][0] * matrix[0][1])
    result = positive - negative
    print(f'The determinant is: {result}')
