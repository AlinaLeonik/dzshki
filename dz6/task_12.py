import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))
n = int(input("Enter the n number: "))


def n_matrix(rows: int, cols: int, n_num: int):
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

    have_n = []
    dont_have_n = []

    for j in range(cols):
        for i in range(rows):
            if orig_matrix[i][j] == n:
                have_n.append(j)
                break
        else:
            dont_have_n.append(j)

    print(f"Columns {have_n} contain {n_num}")
    print(f"Columns {dont_have_n} don't contain {n_num}")


n_matrix(rows, cols, n)
