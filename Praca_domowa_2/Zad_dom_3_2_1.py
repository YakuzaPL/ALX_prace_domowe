def days_of_month_calculator(month_name, months):

    days_num = months[month_name]
    return days_num


def february_calculator(month_name, months, year):

    if month_name == "Luty":

        if int(year) % 4 == 0:
            days1 = months[month_name][-1]
            return days1
        else:
            days = months[month_name][0]
            return days


def main():
    months= {
        "Styczeń" : 31,
        "Luty" : [28, 29],
        "Marzec" : 31,
        "Kwiecień" : 30,
        "Maj" : 31,
        "Czerwiec" : 30,
        "Lipiec" : 31,
        "Sierpień" : 30,
        "Wrzesień" : 31,
        "Październik" : 30,
        "Listopad" : 31,
        "Grzudzień" : 30
        }

    name_of_the_month = input("Proszę wprowadzić nazwę miesiąca: ")
    if name_of_the_month.capitalize() == "Luty":
        year = int(input("Proszę podać rok: "))
        days = february_calculator(name_of_the_month.capitalize(), months, year)
        print(f"W roku {year}, {name_of_the_month} ma {days} dni.")
    else:
        days = days_of_month_calculator(name_of_the_month.capitalize(), months)
        print(f"{name_of_the_month} ma {days} dnia.")


main()

