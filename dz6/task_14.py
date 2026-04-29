import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))


def matrix_diagonals_sum(rows: int, cols: int):
    orig_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = random.randint(0, 1)
            row.append(element)
        orig_matrix.append(row)

    print(f"Original matrix: ")
    for row in orig_matrix:
        print(row)

    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            row_sum += orig_matrix[i][j]
        # думаю стоило присвоить старую матрицу в новую переменную
        # и изменять уже ее (для вайба),
        # но подумала я об этом после того как сделала так что менять леннь
        if row_sum % 2 == 1:
            orig_matrix[i].append(1)
        else:
            orig_matrix[i].append(0)

    print(f"Matrix with even row sum: ")
    for row in orig_matrix:
        print(row)


matrix_diagonals_sum(rows, cols)
