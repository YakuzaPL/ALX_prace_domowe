from Praca_domowa_2.Zad_dom_3_1 import area_of_the_circle


def main():
    radius = int(input("Proszę podać średnicę koła: "))
    area = area_of_the_circle(radius)

    print(f"pole koła o średnicy {radius} to {area: .2f} m2")


main()