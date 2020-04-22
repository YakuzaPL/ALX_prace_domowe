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


