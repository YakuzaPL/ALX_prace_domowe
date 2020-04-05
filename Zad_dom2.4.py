import random


def number_generator():
    number = int(random.randint(0, 999))

    return number


def takeing_user_answer():

    answer = int(input("\nJaką liczbę mam na myśli?\n"))

    return answer


def engine(number, answer, shoot=0):

    while number != answer:
        if number > answer:
            print("Podałeś za małą liczbę!")
            answer = int(input("\nJaką liczbę mam na myśli?\n"))
            shoot += 1

        elif number < answer:
            print("Podałeś za dużą liczbę!")
            answer = int(input("\nJaką liczbę mam na myśli?\n"))
            shoot += 1

    print(f"Zagdłeś!"
          f"Zajęło ci to {shoot} prób.")


def main():
    print("Mam na mysli liczbę z przedziału 0 do 999 . \nZgadniesz jaka to liczba?")
    misterious_number = number_generator()
    user_answer = takeing_user_answer()
    engine(misterious_number, user_answer)


main()