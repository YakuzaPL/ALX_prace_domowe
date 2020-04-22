from Praca_domowa_2.Zad_dom_3_1 import foot_to_metre


def test_foot_to_metre():
    assert foot_to_metre(1) == 0.3048
    assert foot_to_metre(0.5) == 0.1524
    assert foot_to_metre(-5) == -1.52400
    assert foot_to_metre(2500) == 762
    assert foot_to_metre(69.4) == 21.15312

