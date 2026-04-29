import random

rows = int(input("enter count of rows: "))
cols = int(input("enter count of cols: "))


def matrix(rows: int, cols: int) -> list:
    random_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num_i_j = random.randint(1, 100)
            row.append(num_i_j)
        random_matrix.append(row)
    return random_matrix


result = matrix(rows, cols)
for row in result:
    print(row)
