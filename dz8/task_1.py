height = float(input("Enter your height(meters): "))
weight = float(input("Enter your weight(kilogram): "))


def body_mass_index(height: float, weight: float) -> tuple[float, str]:
    try:
        if weight < 2.5 or weight > 250:
            raise ValueError
        if height < 0.35 or height > 2.50:
            raise ValueError
        res = weight / pow(height, 2)

    except ValueError as e:
        print("Enter normal data separated by dot and don't lie.")
        raise e
    except ZeroDivisionError as e:
        print("There is no such thing as zero height. Enter your actual height.")
        raise e
    else:
        if res <= 16:
            category = "Severe thinness"
        elif res <= 18.5:
            category = "Underweight"
        elif res <= 24.99:
            category = "Normal weight"
        elif res <= 29.99:
            category = "Overweight (pre-obesity)"
        elif res <= 34.99:
            category = "Obesity class I"
        elif res <= 39.99:
            category = "Obesity class II"
        else:
            category = "Obesity class III"
    return res, category


result, category = body_mass_index(height, weight)
print(f"Your body mass index is {result:.2f}. This means {category}")
