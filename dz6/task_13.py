import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))


def matrix_diagonals_sum(rows: int, cols: int):
    orig_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = random.randint(1, 10)
            row.append(element)
        orig_matrix.append(row)

    print(f"Original matrix: ")
    for row in orig_matrix:
        print(row)

    sum_main = 0
    sum_secondary = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum_main += orig_matrix[i][j]
            if j == cols - 1 - i:
                sum_secondary += orig_matrix[i][j]
    return sum_main, sum_secondary


main, secondary = matrix_diagonals_sum(rows, cols)

print(f"Sum of the elements on the main diagonal: {main}")
print(f"The sum of the elements on the secondary diagonal: {secondary}")
