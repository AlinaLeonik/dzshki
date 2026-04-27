spisok = list(input("Enter numbers or letters or smth by space: ").split())
check_spisok = []

for element in spisok:
    if element in check_spisok:
        continue

    i = spisok.count(element)

    if i > 1:
        check_spisok.append(element)
        print(f"count of element {element} is {i}")

if spisok != []:
    if check_spisok == []:
        print("All values are unique")
else:
    print("The list is empty")
