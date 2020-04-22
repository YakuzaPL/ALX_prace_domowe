def user_data_input(days_of_the_week):
    while True:
        day = input("Proszę podać dzień w którym buty oddano do naprawy: ")
        if day in days_of_the_week:
            number_of_days = int(input("Proszę podać ile będzie trwała naprawa: : "))
        else:
            print("""Proszę wybrać:\n"
                  "Poniedziałek"
                  "Wtorek"
                  "Środa"
                  "Czwartek"
                  "Piątek"
                  "Sobota"
                  "Niedziela""")
            continue

        return day, number_of_days


def days_of_the_week_counter(day, numbers_of_days,days_of_the_week):
    day_number = days_of_the_week.index(day)
    pick_up_day_num = (day_number + numbers_of_days) % 7
    pick_up_day_name = days_of_the_week[pick_up_day_num]

    return pick_up_day_name


def main():
    days_of_the_week = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
    from_user = user_data_input(days_of_the_week)
    days_calc = days_of_the_week_counter(from_user[0], from_user[1],days_of_the_week)
    print(days_calc)

    return


main()

