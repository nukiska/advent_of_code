def prirad_dvojici_ukol(radek_seznamu_ukolu):
    ukol = radek_seznamu_ukolu.split(',')
    return ukol[0], ukol[1]


def rozdel_do_sekci(id_ukolu):
    sekce = set()
    id_ukolu = id_ukolu.split('-')
    for i in range(int(id_ukolu[0]), int(id_ukolu[-1])+1):
        sekce.add(i)
    return sekce


def odeber_spolecne_sekce(sekce1, sekce2):
    spolecne_sekce = sekce1 & sekce2
    if spolecne_sekce:
        zbyle_sekce1 = sekce1 - spolecne_sekce
        zbyle_sekce2 = sekce2 - spolecne_sekce
        return zbyle_sekce1, zbyle_sekce2
    else:
        return sekce1, sekce2


def existuje_pokryty_usek(useky):
    return 1 if set() in useky else 0


def spocitej_pocet_pokrytych_useku(radky_ukolu):
    pocet_pokrytych_useku = 0
    for radek_ukolu in radky_ukolu:
        ukol1, ukol2 = prirad_dvojici_ukol(radek_ukolu)
        sekce_elfa1 = rozdel_do_sekci(ukol1)
        sekce_elfa2 = rozdel_do_sekci(ukol2)
        zbyle_sekce = odeber_spolecne_sekce(sekce_elfa1, sekce_elfa2)
        if existuje_pokryty_usek(zbyle_sekce):
            pocet_pokrytych_useku += 1
    return pocet_pokrytych_useku


if __name__ == '__main__':
    with open('2022_day_04_input.txt') as f:
        lines = f.read().splitlines()

    # task 1
    print(spocitej_pocet_pokrytych_useku(lines))
