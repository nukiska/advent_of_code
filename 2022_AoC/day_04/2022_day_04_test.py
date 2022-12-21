day_04 = __import__('2022_day_04')

with open('2022_day_04_input_test.txt') as f:
    lines = f.read().splitlines()


def test_prirad_dvojici_ukol():
    assert day_04.prirad_dvojici_ukol(lines[0]) == ('2-4', '6-8')
    assert day_04.prirad_dvojici_ukol(lines[1]) == ('2-3', '4-5')


def test_rozdel_do_sekci():
    assert day_04.rozdel_do_sekci('2-8') == {2, 3, 4, 5, 6, 7, 8}
    assert day_04.rozdel_do_sekci('6') == {6}
    assert day_04.rozdel_do_sekci('10-11') == {10, 11}
    assert day_04.rozdel_do_sekci('20-22') == {20, 21, 22}


def test_odeber_spolecne_sekce():
    assert day_04.odeber_spolecne_sekce({2, 3, 4}, {8, 6, 7}) == ({2, 3, 4}, {8, 6, 7})
    assert day_04.odeber_spolecne_sekce({6}, {4, 5, 6}) == (set(), {4, 5})
    assert day_04.odeber_spolecne_sekce({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}) == ({2, 3}, {7, 8})
    assert day_04.odeber_spolecne_sekce({7, 8, 9, 10, 11}, {9, 10}) == ({7, 8, 11}, set())
    assert day_04.odeber_spolecne_sekce({10, 11}, {10, 11}) == (set(), set())


def test_existuje_pokryty_usek():
    assert day_04.existuje_pokryty_usek((set(), {4, 5})) == 1
    assert day_04.existuje_pokryty_usek((set(), set())) == 1
    assert day_04.existuje_pokryty_usek(({2, 3, 4}, {8, 6, 7})) == 0


def test_spocitej_pocet_pokrytych_useku():
    assert day_04.spocitej_pocet_pokrytych_useku(lines) == 2
