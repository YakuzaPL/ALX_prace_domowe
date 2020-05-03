
# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
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

def main():
    list_of_numbers = [155, 201, 65, 2, -8, 10, 20, 30, 40]
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

    print("Point 6")
    print(biggers_sum(list_of_numbers))
    print(40 * "*")
    print("\n")

main()
