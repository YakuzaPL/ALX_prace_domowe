# użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, # ile trzeba zapłacić. Zasady są takie:
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# ​
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
# czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.


def user_data():
    age = int(input("Proszę wprowadzić swój wiek: "))
    stay_lenght = int(input("Ile nocy planujesz spoędzić w hotleu?: "))

    return age, stay_lenght


def costs_calculator(age, stay_lenght):
    if age < 18:
        one_night = 100

        return one_night
    elif 18 <= age <= 65:
        if stay_lenght == 1:
            one_night = 200

            return one_night
        elif 2 <= stay_lenght < 5:
            one_night = 180

            return one_night
        elif stay_lenght >= 5:
            one_night = 150

            return one_night
    elif age > 65:
        if stay_lenght == 1:
            one_night = 200*(1 - 0.1)

            return one_night
        elif 2 <= stay_lenght < 5:
            one_night = 180*(1 - 0.1)

            return one_night
        elif stay_lenght >= 5:
            one_night = 150*(1 - 0.1)

            return one_night


def main():
    age_and_stay = user_data()
    days = age_and_stay[1]
    day_cost = costs_calculator(age_and_stay[0], age_and_stay[1])
    cost_calc = costs_calculator(age_and_stay[0], age_and_stay[1])*days
    print(f"Zostając {days} dzień/dni, zapłacisz za noc {day_cost: .2f} PLN, czyli cały koszt to: "
          f"{cost_calc: .2f} PLN.")


main()