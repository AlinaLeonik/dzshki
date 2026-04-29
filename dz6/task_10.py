import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))

# если я правильно пон условие,
# то столбец К тоже надо умножать на самого себя ,
# а не пропускать его , поэтому несколько строк закомментила,
# тк изначально подумала что столбец К трогать не надо


def multipl_matrix(rows: int, cols: int):
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

    selected_column = int(input("Select a column to multiply(counting from zero): "))
    if selected_column < 0 or selected_column >= cols:
        print(
            f"There are {cols} columns in total, the selected column does not exist. Try again."
        )
        return

    matrix_result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # if j == selected_column:
            #     new_elem = orig_matrix[i][j]
            #     row.append(new_elem)
            # else:
            new_elem = orig_matrix[i][j] * orig_matrix[i][selected_column]
            row.append(new_elem)
        matrix_result.append(row)

    print(f"Multiplied matrix: ")
    for row in matrix_result:
        print(row)


multipl_matrix(rows, cols)
