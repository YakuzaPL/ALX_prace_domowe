def user_data():
    goods = input("Co chcesz kupić? ")
    amount = int(input("Ile sztuk? "))
    price = float(input("Ile kosztuje? "))

    return goods, amount, price


def price_calculator(amount, price):
    cost = amount * price

    return cost


def main():
    from_user = user_data()

    goods = from_user[0]
    amount = from_user[1]
    price = from_user[-1]

    total = price_calculator(amount, price)

    print(f"Za {goods} zapłacisz {total: .2f} PLN.")


main()