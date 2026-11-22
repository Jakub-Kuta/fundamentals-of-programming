###
# Identity matrices
#
def identity_matrix(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()

for n in [3, 5, 8]:
    print_matrix(identity_matrix(n))
    print()
