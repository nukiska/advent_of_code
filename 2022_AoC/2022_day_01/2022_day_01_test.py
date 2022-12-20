day_01 = __import__('2022_day_01')


def test_get_total_calories_maximum():
    assert day_01.get_total_calories_maximum('2022_day_01_input_test.txt') == 24000


def test_get_3_max_calories_amount():
    assert day_01.get_3_max_calories_amount() == 45000
