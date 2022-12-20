day_02 = __import__('2022_day_02')


def test_spocitej_skore_bez_znalosti_strategie():
    assert day_02.spocitej_skore_bez_znalosti_strategie('2022_day_02_input_test.txt') == 15


def test_skoncit_ocekavanym_vysledkem():
    assert day_02.skoncit_ocekavanym_vysledkem('A', 'prohra') == 3
    assert day_02.skoncit_ocekavanym_vysledkem('B', 'remiza') == 2
    assert day_02.skoncit_ocekavanym_vysledkem('C', 'vyhra') == 1


def test_spocitej_skore_se_znalosti_strategie():
    assert day_02.spocitej_skore_se_znalosti_strategie('2022_day_02_input_test.txt') == 12
