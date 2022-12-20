kamen_papir_nuzky = {'X': 1, 'Y': 2, 'Z': 3}
vysledek_kola = {'prohra': ('A Z', 'B X', 'C Y'), 'remiza': ('A X', 'B Y', 'C Z'), 'vyhra': ('A Y', 'B Z', 'C X')}


def spocitej_skore_bez_znalosti_strategie():
    skore = 0
    with open('2022_day_02_input.txt', encoding='utf-8') as f:
        for line in f:
            tah = line.rstrip()
            skore += kamen_papir_nuzky[tah[2]]
            match [tah in stav_kola for stav_kola in vysledek_kola.values()].index(True):
                case 1:
                    skore += 3
                case 2:
                    skore += 6
    return skore


def skoncit_ocekavanym_vysledkem(volba_soupere, ocekavany_vysledek):
    pocet_bodu = 0
    for prvek in vysledek_kola[ocekavany_vysledek]:
        if volba_soupere in prvek:
            pocet_bodu += kamen_papir_nuzky[prvek[2]]
    return pocet_bodu


def spocitej_skore_se_znalosti_strategie():
    nove_skore = 0
    with open('2022_day_02_input.txt', encoding='utf-8') as f:
        for line in f:
            tah = line.rstrip()
            match tah[2]:
                case 'X':
                    nove_skore += skoncit_ocekavanym_vysledkem(tah[0], 'prohra')
                case 'Y':
                    nove_skore += 3 + skoncit_ocekavanym_vysledkem(tah[0], 'remiza')
                case 'Z':
                    nove_skore += 6 + skoncit_ocekavanym_vysledkem(tah[0], 'vyhra')
    return nove_skore


if __name__ == '__main__':
    # task 1
    print(spocitej_skore_bez_znalosti_strategie())
    # task 2
    print(spocitej_skore_se_znalosti_strategie())
