import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))


def summed_matrix(rows: int, cols: int):
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

    selected_row = int(input("Select a row to sum(counting from zero): "))
    if selected_row < 0 or selected_row >= rows:
        print(
            f"There are {rows} rows in total, the selected row does not exist. Try again."
        )
        return

    matrix_result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            new_elem = orig_matrix[i][j] + orig_matrix[selected_row][j]
            row.append(new_elem)
        matrix_result.append(row)

    print(f"Summed matrix: ")
    for row in matrix_result:
        print(row)


summed_matrix(rows, cols)
