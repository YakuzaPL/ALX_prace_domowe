from Praca_domowa_2.Zad_dom_3_1 import foot_to_metre, which_is_bigger, average_counter, area_of_the_circle


def test_foot_to_metre():
    assert foot_to_metre(1) == 0.3048
    assert foot_to_metre(0.5) == 0.1524
    assert foot_to_metre(-5) == -1.52400
    assert foot_to_metre(2500) == 762
    assert foot_to_metre(69.4) == 21.15312

def test_which_is_bigger():
    assert which_is_bigger(1, 2) == 2
    assert which_is_bigger(2, 1) == 2
    assert which_is_bigger(2, 2) == "="
    assert which_is_bigger(1, 1.5) == 1.5
    assert which_is_bigger(1, 1.000001) == 1.000001


def test_average_counter():
    assert average_counter(1, 1) == 1
    assert average_counter(1, 2) == 1.5
    assert average_counter(3, 9) == 6
    assert average_counter(-2, 5) == 1.5


def test_area_of_the_circle():
    assert area_of_the_circle(2) == 12.566370614359172
    assert area_of_the_circle(0) == 0.0
    assert area_of_the_circle(23.4) == 1720.2104733996268
