import math

n = int(input("Enter n: "))
x = int(input("Enter x: "))

# 1a
sin_x = 0

for i in range(n):
    sin_x += pow(-1, i) * pow(x, 2 * i + 1) / math.factorial(2 * i + 1)

sin_x_real = math.sin(x)

print(f"Sin(x) by formula: {sin_x}\nReal sin(x): {sin_x_real}")


# 1b
cos_x = 0

for i in range(n):
    cos_x += pow(-1, i) * pow(x, 2 * i) / math.factorial(2 * i)

cos_x_real = math.cos(x)

print(f"Cos(x) by formula: {cos_x}\nReal cos(x): {cos_x_real}")
