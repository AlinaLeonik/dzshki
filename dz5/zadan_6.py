spisok = list(map(int, input("Enter a sorted list of numbers by space: ").split()))
element = int(input("Enter the element you are looking for: "))

left_border = 0
right_border = len(spisok) - 1

while True:
    middle = (right_border + left_border) // 2
    if element == spisok[middle]:
        print(f"Your element is at index {middle}")
        break
    elif element < spisok[middle]:
        right_border = middle - 1
    else:
        left_border = middle + 1

    if left_border > right_border:
        print("The item is not in the list")
        break
