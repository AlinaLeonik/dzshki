phone_cost = float(input("Enter the price of the phone: "))
everyday_amount = float(input("Enter the amount you save daily: "))

day_counter = 0
total_amount = 0
while total_amount < phone_cost:
    day_counter += 1
    if day_counter % 7 == 0:
        continue
    total_amount += everyday_amount

print(f"Congratulations! You can buy a phone in {day_counter} days!")
