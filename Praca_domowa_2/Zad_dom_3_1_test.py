from Praca_domowa_2.Zad_dom_3_1 import foot_to_metre, which_is_bigger


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

