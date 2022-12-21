def rozdel_napul(obsah_batohu: str):
    n = len(obsah_batohu)
    prihradka1 = obsah_batohu[0:n // 2]
    prihradka2 = obsah_batohu[n // 2:]
    return prihradka1, prihradka2


def vrat_prioritu(pismeno):
    return ord(pismeno) - 96 if pismeno.islower() else ord(pismeno) - 38


def spocitej_prioritu_polozky(polozky_batohu):
    prihradka1, prihradka2 = rozdel_napul(polozky_batohu)
    polozka = (set(prihradka1) & set(prihradka2)).pop()
    priorita = vrat_prioritu(polozka)
    return priorita


def secti_priority_polozek(radky_souboru):
    soucet = 0
    for radek_s_polozkami in radky_souboru:
        soucet += spocitej_prioritu_polozky(radek_s_polozkami)
    return soucet


def secti_prioritu_polozek_3_batohu(batohy):
    soucet = 0
    for i in range(0, len(batohy), 3):
        spolecna_polozka = set(batohy[i]) & set(batohy[i + 1]) & set(batohy[i + 2])
        soucet += vrat_prioritu(spolecna_polozka.pop())
    return soucet


if __name__ == '__main__':
    with open('2022_day_03_input.txt') as f:
        lines = f.read().splitlines()

    # task 1
    print(secti_priority_polozek(lines))

    # task 2
    print(secti_prioritu_polozek_3_batohu(lines))
