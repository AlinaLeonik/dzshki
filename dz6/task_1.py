def binar_rec(sorted_list: list, element: int, left=0, right=None) -> int:

    if right is None:
        right = len(sorted_list) - 1

    if left > right:  # типо базовый случай
        return -1

    middle = (right + left) // 2

    if element == sorted_list[middle]:
        return middle
    elif element < sorted_list[middle]:
        right = middle - 1
        return binar_rec(sorted_list, element, left, right)
    else:
        left = middle + 1
        return binar_rec(sorted_list, element, left, right)


sorted_list = list(map(int, input("Enter a sorted list of numbers by space: ").split()))
element = int(input("Enter the element you are looking for: "))

result = binar_rec(sorted_list, element)

if result == -1:
    print("This element is not from the list")
else:
    print(f"Your element is at index {result}")
