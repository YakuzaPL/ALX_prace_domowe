def days_of_month_calculator(month_name, months):

    if month_name == "Luty":
        year = input("Proszę podać rok: ")
        if int(year) % 4 == 0:
            days = months[month_name][-1]
            return f"W roku {year}, {month_name} miał {days} dni."
        else:
            days2 = months[month_name][0]
            return f"W roku {year}, {month_name} miał {days2} dni."
    else:
        days3 = months[month_name]
        return f"{month_name} ma {days3} dni."


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
    answer = days_of_month_calculator(name_of_the_month.capitalize(), months)
    print(answer)


main()

