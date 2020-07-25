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
                    matrix[line].append(locale)
                    break
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
            print(f'[ {matrix[line][column]} ]', end='')





