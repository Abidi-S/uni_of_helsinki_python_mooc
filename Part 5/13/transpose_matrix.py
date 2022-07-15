# Write your solution here
def transpose(matrix: list):
    matrix_copy = []
    for i in range(0, len(matrix)):
        #row = matrix[i]
        new_row = []
        for row in matrix:
            #column = row[j]
            new_row.append(row[i])
        matrix_copy.append(new_row)
    matrix[:] = matrix_copy