spisok = list(input("Enter numbers separated by space: ").split())

print(spisok)

summa_elem = 0
for element in spisok:
    summa_elem += int(element)

print(f"The sum of the elements is {summa_elem}")

max_el = 0
for item in spisok:
    if max_el < int(item):
        max_el = int(item)

print(f"Max el is: {max_el}")


min_el = int(spisok[0])
for item in spisok:
    if min_el > int(item):
        min_el = int(item)

print(f"Min el is: {min_el}")
