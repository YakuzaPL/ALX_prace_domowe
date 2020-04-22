import math


def foot_to_metre(foot):
    return foot * 0.3048


def which_is_bigger(num_1, num_2):
    if num_1 > num_2:
        return num_1
    elif num_2 > num_1:
        return num_2
    else:
        return "="


def average_counter(num_1 = float, num_2 = float):
    average = (num_1 + num_2) / 2
    return average


def area_of_the_circle(radius):
    area = math.pi * (radius ** 2)
    return area


def bmi_calc(weight, hight):
    hight_m = hight / 100
    hight_square = hight_m **2
    bmi = weight / hight_square
    return round(bmi, 2)


def herons(side_a, side_b, side_c):
    side_sum = side_a + side_b + side_c
    area = 0.5 * side_sum
    equasion_one = area * (area - side_a) * (area - side_b) * (area - side_c)
    herons_s = math.sqrt(equasion_one)
    return round(herons_s, 2)


def kilometre_to_mile(kilometre):
    mile = kilometre * 0.621371192
    return round(mile, 2)


def mile_to_kilometre(mile):
    kilometre = mile * 1.6093
    return round(kilometre, 2)

