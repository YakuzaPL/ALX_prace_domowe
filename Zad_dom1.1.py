""" Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)

Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za pięć kilo ziemniaków.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
"""



def costs_calculator(price_for_kg, quantity):
    total_cost = float(price_for_kg) * float(quantity)

    return total_cost


def user_input_price():
    price = float(input("Proszę wprowadzić cenę za kilogram: "))

    return price


def user_input_quantity():
    quant = float(input("Proszę wprowadzić ilość kilogramów: "))

    return quant


def what_is_more(bread, banana):
    if bread > banana:
        print("Więcej zapłacisz za chleb!")
    elif banana > bread:
        print("Więcej zapłacisz za banany!")
    else:
        print("Oba produkty są w tej samej cenie.")

    return


def main():
    # bread priceing
    print("Przystępujesz do zakupu chleba.\n")
    price_kg_bread = user_input_price()
    quantity_bread = user_input_quantity()
    costs_bread = costs_calculator(price_kg_bread, quantity_bread)

    # bananas priceing
    print("\n\nPrzystępujesz do zakupu bananów.\n")
    price_kg_banana = user_input_price()
    quantity_banana = user_input_quantity()
    costs_banana = costs_calculator(price_kg_banana, quantity_banana)

    print(f"\nCałkowity koszt zakupu {int(quantity_bread)} kilogramów chleba to {costs_bread} PLN.\n")
    print(f"Całkowity koszt zakupu {int(quantity_banana)} kilogramów babanów to {costs_banana} PLN.\n")

    what_is_more(costs_bread, costs_banana)




main()
