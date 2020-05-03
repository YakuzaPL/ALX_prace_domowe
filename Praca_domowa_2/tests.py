list_of_numbers = [50, 120, 60, 10, 20, 30, 40]

a = list_of_numbers[0]
for number in list_of_numbers:
    if number < a:
        a = number

print(a)