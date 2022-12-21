def spocitej_soucet_priorit_typu_polozek(data='2022_day_03_input.txt'):
    soucet = 0
    with open(data, encoding='utf-8') as f:
        for line in f:
            radek = line.rstrip()
            n = len(radek)
            if n % 2 == 0:
                prihradka1 = set(radek[0:n // 2])
                prihradka2 = set(radek[n // 2:])
                polozka = list(prihradka1.intersection(prihradka2))[0]
                if polozka.islower():
                    soucet += ord(polozka) - 96
                elif polozka.isupper():
                    soucet += ord(polozka) - 38
    return soucet


if __name__ == '__main__':
    # task 1
    print(spocitej_soucet_priorit_typu_polozek())
    # task 2

