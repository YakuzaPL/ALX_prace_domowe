# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# odaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
# Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
import random


def number_gen():
    first_number = random.randrange(0, 100)
    seckond_number = random.randrange(0,100)
    sum_of_a_and_b = first_number + seckond_number

    return first_number, seckond_number, sum_of_a_and_b


def adding_two_numbers(num_a, num_b):
    sum_of_a_and_b = num_a + num_b

    return sum_of_a_and_b


def the_riddler(num_a, num_b):
    answer = int(input(f"Podaj rozwiązanie następującego równania {num_a} + {num_b} = "))

    return answer


def main():
    num_gen = number_gen()
    num_a = num_gen[0]
    num_b = num_gen[1]
    sum_of_a_and_b = adding_two_numbers(num_a, num_b)

    answer = the_riddler(num_a, num_b)
    while answer != sum_of_a_and_b:
        if answer != sum_of_a_and_b:
            print("Błędny wynik!")
            num_gen = number_gen()
            num_a = num_gen[0]
            num_b = num_gen[1]
            sum_of_a_and_b = num_gen[-1]
            answer = the_riddler(num_a, num_b)

    print("Zgadza się!")


main()




