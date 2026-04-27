spisok = list(map(int, input("Enter a shifted sorted list of numbers: ").split()))
element = int(input("Enter the element you are looking for: "))

left_border = 0
right_border = len(spisok) - 1

while left_border <= right_border:
    middle = (right_border + left_border) // 2

    # if left_border <=
    if element == spisok[middle]:
        print(f"Your element is at index {middle}")
        break
    elif spisok[left_border] <= spisok[middle]:
        if spisok[left_border] <= element < spisok[middle]:
            right_border = middle - 1
        else:
            left_border = middle + 1
    else:
        if spisok[middle] < element <= spisok[right_border]:
            left_border = middle + 1
        else:
            right_border = middle - 1
else:
    print("Element not found")
