try:
    x = float(input("Enter first num: "))
    y = float(input("Enter second num: "))
except ValueError:
    print("You did not enter a number")
    exit()

operation = input("Enter your operation (+, -, %, /, *, **, //): ")


def calc(x: float, y: float, operation: str) -> float | str:
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "%": lambda a, b: a % b,
        "/": lambda a, b: a / b,
        "*": lambda a, b: a * b,
        "//": lambda a, b: a // b,
        "**": lambda a, b: a**b,
    }

    try:
        if operation == "**" and (x > 1000 or y > 1000):
            raise ValueError

        if operation in operations:
            res = operations[operation](x, y)
        else:
            return f"Unknown operator: {operation}"

    except ZeroDivisionError as e:
        print("You can't divide by zero")
        raise e
    except ValueError as e:
        print("The numbers are too big for this action.")
        raise e
    except Exception as e:
        print(f"Unknown error: {e}")
        raise e

    return res


result = calc(x, y, operation)
print(f"Result: {result}")
