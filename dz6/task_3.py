from math import sqrt

number = int(input("Enter number: "))


def is_simple(number: int, divisor=3):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    limit = sqrt(number)
    if divisor > limit:
        return True
    elif number % divisor == 0:
        return False
    else:
        return is_simple(number, divisor + 2)


if is_simple(number):
    print("the number is prime")
else:
    print("the number is not prime")
