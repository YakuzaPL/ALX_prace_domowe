def sum_of_numbers(list_of_numbers):
    total_numbers = 0
    if len(list_of_numbers) == 0:
        return total_numbers

    for number in list_of_numbers:
        total_numbers += number

    return total_numbers


list_of_numbers = []

print(sum_of_numbers(list_of_numbers))