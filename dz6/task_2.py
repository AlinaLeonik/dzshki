def decimal_to_binary(element: int) -> str:
    if element < 2:  # 0 или 1, типо база
        return str(element)
    else:
        return decimal_to_binary(element // 2) + str(element % 2)


element = int(input("Enter element: "))
result = decimal_to_binary(element)
print(f"The number {element} is equal to the binary number {result}")
