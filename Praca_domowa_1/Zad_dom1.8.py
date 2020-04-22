def user_data():
    dog_name = input("Podaj imię psa: ")
    dog_age = int(input("Podaj wiek psa: "))

    return dog_name, dog_age


def dog_to_human_age(dog_age):
    dog_to_human = dog_age * 5

    return dog_to_human


def main():
    from_user = user_data()
    dog_name = from_user[0]
    dog_age = from_user[-1]

    dog_to_human = dog_to_human_age(dog_age)

    if dog_name[-1] == "a":
        print(f"Gdyby {dog_name.capitalize()} była człowiekiem miałaby {dog_to_human} lat.")
    else:
        print(f"Gdyby {dog_name.capitalize()} był człowiekiem miałby {dog_to_human} lat.")


main()