def read_matrix():
    """
    Read number of rows and columns of a matrix.
    Then, read each element and store it in a matrix.
    Return the read-in matrix
    :params Nothing
    :return 2D-list contains the matrix
    """
    row = int(input("Input #rows? "))
    col = int(input("Input #columns? "))
    matrix = []
    for i in range (row):
        lst = []
        for j in range (col):
            element = int(input(f"Input element[{i+1}][{j+1}]: "))
            lst.append(element)
        matrix.append(lst)
    print(matrix)
    return matrix


def print_matrix(matrix):
    """
    Display a matrix, where each number is displayed in 5 spaces and right-aligned.
    :params a 2D-list contains a matrix
    :return Nothing
    """
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            print(f"{matrix[i][j]:>5}",end='')
        print("")
    


matrix = read_matrix()
print("Matrix A is")
print_matrix(matrix)