

# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma


def sum_of_numbers(list_of_numbers):
    total_numbers = 0
    for number in list_of_numbers:
        total_numbers += number

    return total_numbers


def average_counter(list_of_numbers):
    total_numbers = 0
    for number in list_of_numbers:
        total_numbers += number
    average = total_numbers / len(list_of_numbers)

    return average


def maximum_searcher(list_of_numbers):
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


def printing_bigger(list_of_numbers, x=23):
    bigger = []
    for number in list_of_numbers:
        if number > x:
            bigger.append(number)
    return bigger


def printing_first_bigger(list_of_numbers, x=160):

    for number in list_of_numbers:
        if number > x:
            return number


def biggers_sum(list_of_numbers, x=154):
    bigger = []
    for number in list_of_numbers:
        if number > x:
            bigger.append(number)

    return sum(bigger)


def how_many_bigger(list_of_numbers, x=154):
    bigger = []
    for number in list_of_numbers:
        if number > x:
            bigger.append(number)

    return len(bigger)


def printing_divisible(list_of_numbers, x=2):
    divisible = []
    for number in list_of_numbers:
        if number % x == 0:
            divisible.append(number)

    return divisible


def printing_first_divisible(list_of_numbers, x=2):

    for number in list_of_numbers:
        if number % x == 0:
            return number


def common_elements(list_of_numbers, list_of_numbers2):

    common_elements_var = []
    for number in list_of_numbers:
        if number in list_of_numbers2:
            common_elements_var.append(number)

    return  common_elements_var


def main():
    list_of_numbers = [155, 201, 65, 2, -8, 10, 20, 30, 40]
    list_of_numbers2 = [20, 89, 10, 47]

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
    print(printing_bigger(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 6")
    print(printing_first_bigger(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 7")
    print(biggers_sum(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 8")
    print(how_many_bigger(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 9")
    print(printing_divisible(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 10")
    print(printing_first_divisible(list_of_numbers))
    print(40 * "*")
    print("\n")

    print("Point 11")
    print(common_elements(list_of_numbers, list_of_numbers2))
    print(40 * "*")
    print("\n")

main()
