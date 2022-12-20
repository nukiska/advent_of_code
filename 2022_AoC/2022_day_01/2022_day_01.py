elves = []


def get_total_calories_maximum(data='2022_day_01_input.txt'):
    food_calories = 0
    with open(data, encoding='utf-8') as f:
        for line in f:
            if line.rstrip() != '':
                food_calories += int(line.rstrip())
            else:
                elves.append(food_calories)
                food_calories = 0
        elves.append(food_calories)
    return max(elves)


def get_3_max_calories_amount():
    sorted_total_calories = sorted(elves, reverse=True)[:3]
    return sum(i for i in sorted_total_calories)


if __name__ == '__main__':
    # task 1
    print(get_total_calories_maximum())
    # task 2
    print(get_3_max_calories_amount())
