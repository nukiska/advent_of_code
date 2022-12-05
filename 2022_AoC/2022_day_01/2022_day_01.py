elves = {}


def get_total_calories_maximum():
    food_calories = 0
    elf_num = 1

    with open('2022_day_01_input.txt', encoding='utf-8') as f:
        for line in f:
            if line.rstrip() != '':
                food_calories += int(line.rstrip())
            else:
                elves[elf_num] = food_calories
                food_calories = 0
                elf_num += 1
        elves[elf_num] = food_calories

    elf_with_max_calories = max(elves, key=elves.get)
    max_total_calories = elves[elf_with_max_calories]
    return max_total_calories


def get_3_max_calories_amount():
    sorted_total_calories = sorted(elves, key=elves.get, reverse=True)[:3]
    return sum(elves[i] for i in sorted_total_calories)


if __name__ == '__main__':
    # task 1
    print(get_total_calories_maximum())
    # task 2
    print(get_3_max_calories_amount())
