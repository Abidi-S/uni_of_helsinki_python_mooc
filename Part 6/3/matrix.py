# write your solution here
def matrix_sum():
    total = 0
    with open("matrix.txt") as matrix_file:
        elements = string_to_int(matrix_file)
        for element in elements:
            total += element
    return total

def matrix_max():
    with open("matrix.txt") as matrix_file:
        elements = string_to_int(matrix_file)
        largest = max(elements)
    return largest

def row_sums():
    elements_sum = []
    with open("matrix.txt") as matrix_file:
        for row in matrix_file:
            row = row.replace("\n", "")
            elements = (row.split(","))
            summ = 0
            for element in elements:
                element = int(element)
                summ += element
            elements_sum.append(summ)
    return (elements_sum)

def string_to_int(matrix_file):
    int_elements = []
    for row in matrix_file:
            row = row.replace("\n", "")
            elements = (row.split(","))
            for element in elements:
                int_elements.append(int(element))
    return (int_elements)
