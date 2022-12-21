def rozdel_batoh_napul(obsah_batohu: str):
    n = len(obsah_batohu)
    prihradka1 = obsah_batohu[0:n // 2]
    prihradka2 = obsah_batohu[n // 2:]
    return prihradka1, prihradka2


def vrat_prioritu(pismeno):
    if pismeno.islower():
        return ord(pismeno) - 96
    elif pismeno.isupper():
        return ord(pismeno) - 38


def spocitej_prioritu_polozky(polozky):
    prihradka1, prihradka2 = rozdel_batoh_napul(polozky)
    polozka = list(set(prihradka1) & set(prihradka2))[0]
    priorita = vrat_prioritu(polozka)
    return priorita


def secti_priority_polozek(radky_souboru):
    soucet = 0
    for radek_s_polozkami in radky_souboru:
        soucet += spocitej_prioritu_polozky(radek_s_polozkami)
    return soucet


# data='2022_day_03_input_test.txt'
# def spocitej_soucet_priorit_typu_predmetu(data='2022_day_03_input.txt'):
#     soucet = 0

# with open(data, encoding='utf-8') as f:
#     for line in f:
#         neco = set(line.rstrip())
# print(radek)
# predmet = list(prihradka1.intersection(prihradka2))[0]
# soucet += spocitej_prioritu(predmet)

# return radek


if __name__ == '__main__':
    with open('2022_day_03_input.txt') as f:
        lines = f.read().splitlines()

    # task 1
    print(secti_priority_polozek(lines))

#     # task 2
#     print(spocitej_soucet_priorit_typu_predmetu())
