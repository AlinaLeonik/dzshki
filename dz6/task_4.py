# загуглила, там есть какой-то специальный алгоритм кого-то там,
# но решила не изменять ничего
def NOD(num_1: int, num_2: int, divisor: int) -> int:

    if num_1 % divisor == 0 and num_2 % divisor == 0:
        return divisor
    else:
        divisor -= 1
        return NOD(num_1, num_2, divisor)


num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

divisor = min(num_1, num_2)
result = NOD(num_1, num_2, divisor)
print(result)
