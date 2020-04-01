def user_data():
    weight = float(input("Proszę wprowadzić swój wagę: "))
    height = float(input("Proszę wprowadzić swoją wzrost: "))

    return weight, height


def bmi_calc(weight, height):
    bmi = weight / (height/100)**2

    return float(bmi)


def bmi_interpreter(bmi):
    if bmi < 16:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to wygłodzenie.")
    elif 16 <= bmi <= 16.99:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to wychudzenie.")
    elif 17 <= bmi <= 18.48:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to niedowagę.")
    elif 18.5 <= bmi <= 24.99:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to wartość prawidłową.")
    elif 25 <= bmi <= 29.99:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to nadwagę.")
    elif 30 <= bmi <= 34.99:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to I stopień otyłości.")
    elif 35 <= bmi <= 39.99:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to II stopień otyłości.")
    elif bmi >= 40:
        return print(f"Twoje BMI to {bmi: .2f}, oznacza to otyłość skrajną.")


def main():
    from_user = user_data()
    print(bmi_interpreter(bmi_calc(from_user[0], from_user[1])))


main()
