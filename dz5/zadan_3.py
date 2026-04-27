n = int(input("Enter count of numbers: "))

first_num = 1
second_num = 1
print(first_num, second_num, end=" ")
for i in range(n - 2):
    new_num = first_num + second_num
    print(new_num, end=" ")
    first_num = second_num
    second_num = new_num
