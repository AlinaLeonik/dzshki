import random

rows = int(input("Enter number of lines: "))
cols = int(input("Enter the number of columns: "))


def matrix_sum(rows: int, cols: int) -> list:
    matrix_result = []
    sum_of_el: int = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            element = random.randint(1, 100)
            row.append(element)
            sum_of_el += element
        matrix_result.append(row)

    for row in matrix_result:
        print(row)
    print(f"Sum of elements: {sum_of_el}")

    for i in range(cols):
        column_sum: int = 0
        for j in range(rows):
            column_sum += matrix_result[j][i]
        percent = round(column_sum / sum_of_el * 100, 1)
        print(f"Column {i+1} is {percent}% of the total amount")


matrix_sum(rows, cols)
