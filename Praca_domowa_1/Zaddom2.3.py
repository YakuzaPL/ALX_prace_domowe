def from_user():
    users_numbers = []
    proceed = " "
    while proceed != "NIE":
        question = input("Czy chcesz poda liczbę? 'TAK' / 'NIE': ")
        proceed = question.upper()
        if proceed != "TAK" and proceed != "NIE":
            print("Podałeś niewłaściwą wartość! Wpisz 'TAK' lub 'NIE'")
            question = input("Czy chcesz kontynuować? 'TAK' / 'NIE': ")
            proceed = question.upper()
            if proceed != "TAK" and proceed != "NIE":
                print("Podałeś niewłaściwą wartość! Wpisz 'TAK' lub 'NIE'")
                question = input("Czy chcesz kontynuować? 'TAK' / 'NIE': ")
                proceed = question.upper()
                if proceed == "NIE":
                    break

        if proceed == "NIE":
            break

        user_data = int(input("Podaj dowolną liczbę: "))
        users_numbers.append(user_data)

        if proceed != "TAK" and proceed != "NIE":
            print("Podałeś niewłaściwą wartość! Wpisz 'TAK' lub 'NIE'")
            question = input("Czy chcesz kontynuować? 'TAK' / 'NIE': ")
            proceed = question.upper()
            if proceed == "NIE":
                break

    return users_numbers


def average(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number

    avrage_of_num = sum_of_numbers // len(numbers)

    return avrage_of_num


x = from_user()
y = average(x)

print(x, y)
