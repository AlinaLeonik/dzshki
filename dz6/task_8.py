import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))


def matrix(rows: int, cols: int) -> list:
    matrix_result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = random.randint(1, 100)
            row.append(element)
        matrix_result.append(row)

    for row in matrix_result:
        print(row)

    counter_for_min = matrix_result[0][0]
    counter_for_max = matrix_result[0][0]

    i_min_index = j_min_index = i_max_index = j_max_index = 0

    for i in range(rows):
        for j in range(cols):
            if counter_for_min > matrix_result[i][j]:
                counter_for_min = matrix_result[i][j]
                i_min_index = i
                j_min_index = j
            if counter_for_max < matrix_result[i][j]:
                counter_for_max = matrix_result[i][j]
                i_max_index = i
                j_max_index = j

    print(f"Min el is: {counter_for_min}. Its index is [{i_min_index}][{j_min_index}]")
    print(f"Max el is: {counter_for_max}. Its index is [{i_max_index}][{j_max_index}]")


matrix(rows, cols)
