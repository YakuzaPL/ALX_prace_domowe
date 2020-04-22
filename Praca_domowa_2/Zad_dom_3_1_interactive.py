from Praca_domowa_2.Zad_dom_3_1 import bmi_calc


def main():
    weight = int(input("Proszę podać wagę w kilogramch: "))
    hight = int(input("Proszę podać swój wzrost w centymetrach: "))
    your_bmi = bmi_calc(weight, hight)
    print(f"twoje BMI to {your_bmi}")


main()