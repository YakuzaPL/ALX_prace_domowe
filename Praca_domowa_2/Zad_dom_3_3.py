
def sum_of_numbers(list_of_numbers):
    total_numbers = 0
    if len(list_of_numbers) == 0:
        return total_numbers

    for number in list_of_numbers:
        total_numbers += number

    return total_numbers


def average_counter(list_of_numbers):
    total_numbers = 0
    if len(list_of_numbers) == 0:
        return total_numbers

    for number in list_of_numbers:
        total_numbers += number
    average = total_numbers / len(list_of_numbers)

    return average


def maximum_searcher(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0

    max_number = list_of_numbers[0]

    for number in list_of_numbers:
        if number > max_number:
            max_number = number

    return max_number


def minmax_difference(list_of_numbers):
    if len(list_of_numbers) == 0:
        difference = 0
    else:
        difference = max(list_of_numbers) - min(list_of_numbers)

    return difference


def printing_bigger(list_of_numbers, x):
    bigger = []
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number > x:
            bigger.append(number)
    return bigger


def printing_first_bigger(list_of_numbers, x):
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number > x:
            return number


def biggers_sum(list_of_numbers, x):
    bigger = []
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number > x:
            bigger.append(number)

    return sum(bigger)


def how_many_bigger(list_of_numbers, x):
    bigger = []
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number > x:
            bigger.append(number)

    return len(bigger)


def printing_divisible(list_of_numbers, x=2):
    divisible = []
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number % x == 0:
            divisible.append(number)

    print(divisible)
    return


def printing_first_divisible(list_of_numbers, x=2):
    if len(list_of_numbers) == 0:

        return 0

    for number in list_of_numbers:
        if number % x == 0:
            print(number)

    return


def common_elements(list_of_numbers, list_of_numbers2):

    common_elements_var = []
    if len(list_of_numbers) == 0:
        return 0

    for number in list_of_numbers:
        if number in list_of_numbers2:
            common_elements_var.append(number)

    return  common_elements_var


def main():
    list_of_numbers = [156, 5, 10, 85, 596, -8, 20, 30, 51, 60]
    list_of_numbers2 = [20, 89, 10, 47]
    x = 154

    print("Point 1")
    print(sum_of_numbers(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 2")
    print(average_counter(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 3")
    print(maximum_searcher(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 4")
    print(minmax_difference(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 5")
    print(printing_bigger(list_of_numbers, x))
    print(40 * "*")
    print("\n")

    print("Point 6")
    print(printing_first_bigger(list_of_numbers, x))
    print(40 * "*")
    print("\n")

    print("Point 7")
    print(biggers_sum(list_of_numbers, x))
    print(40 * "*")
    print("\n")

    print("Point 8")
    print(how_many_bigger(list_of_numbers, x))
    print(40 * "*")
    print("\n")

    print("Point 9")
    printing_divisible(list_of_numbers)
    print(40 * "*")
    print("\n")

    print("Point 10")
    printing_first_divisible(list_of_numbers)
    print(40 * "*")
    print("\n")

    print("Point 11")
    print(common_elements(list_of_numbers, list_of_numbers2))
    print(40 * "*")
    print("\n")

main()
