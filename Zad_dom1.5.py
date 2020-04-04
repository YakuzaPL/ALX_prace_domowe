from math import sqrt


def side_info():
    give_side_a = int(input("Proszę podać długość pierwszego boku: "))
    give_side_b = int(input("Proszę podać długość drugiego boku: "))
    give_side_c = int(input("Proszę podać długość trzeciego boku: "))

    return give_side_a, give_side_b, give_side_c


def triangle_checker(a, b, c):
    sides = [a, b, c]
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b > c:
        return
    else:
        print("Z takich boków nie da się zbudować trójkata.")
        exit()


def tirangle_field_calc(side_a, side_b, side_c):
    p = (side_a + side_b + side_c) / 2
    field_value = sqrt(p * ((p - side_a) * (p - side_b) * (p - side_a)))

    return field_value


def main():
    ask_user = side_info()
    a = ask_user[0]
    b = ask_user[1]
    c = ask_user[2]
    field = tirangle_field_calc(a, b, c)
    print(f"Pole powierzchni trójkąta o podanych bokach to: {field: .2f} cm2.")


main()
