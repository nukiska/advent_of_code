day_03 = __import__('2022_day_03')


def test_rozdel_batoh_napul():
    assert day_03.rozdel_batoh_napul('vJrwpWtwJgWrhcsFMMfFFhFp') == ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')


def test_vrat_prioritu():
    assert day_03.vrat_prioritu('a') == 1
    assert day_03.vrat_prioritu('z') == 26
    assert day_03.vrat_prioritu('A') == 27
    assert day_03.vrat_prioritu('Z') == 52


def test_spocitej_prioritu_polozky():
    with open('2022_day_03_input_test.txt') as f:
        lines = f.read().splitlines()
        assert day_03.spocitej_prioritu_polozky(lines[0]) == 16
        assert day_03.spocitej_prioritu_polozky(lines[1]) == 38
        assert day_03.spocitej_prioritu_polozky(lines[2]) == 42
        assert day_03.spocitej_prioritu_polozky(lines[3]) == 22
        assert day_03.spocitej_prioritu_polozky(lines[4]) == 20
        assert day_03.spocitej_prioritu_polozky(lines[5]) == 19


def test_secti_priority_polozek():
    with open('2022_day_03_input_test.txt') as f:
        lines = f.read().splitlines()
        assert day_03.secti_priority_polozek(lines) == 157
