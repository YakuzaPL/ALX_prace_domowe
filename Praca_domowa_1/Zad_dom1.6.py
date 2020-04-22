def user_data():
    age = int(input("Proszę wprowadzić swój wiek: "))
    tickets_amount = int(input("Ile biletów chcesz kupić?: "))

    return age, tickets_amount


def ticke_price_calculator(age, amount):
    if age <= 6:
        print("Dzieci w wieku przedszkolnym podróżują bez biletów.")
    elif 7 <= age <= 17:
        tota_price = amount * 2.28

        return tota_price
    elif 18 <= age <= 64:
        tota_price = amount * 3.80

        return tota_price
    elif age >= 65:
        tota_price = amount * 1.90

        return tota_price


def main():
    user_info = user_data()
    age = user_info[0]
    amount = user_info[-1]

    ticket_price = ticke_price_calculator(age, amount)

    if amount == 1 and age > 6:
        print(f"Cena jednego biletu wynosi {ticket_price: .2f} PLN")
    elif amount > 1 and age > 6:
        print(f"Koszt {amount} biletów to: {ticket_price: .2f} PLN.")


main()