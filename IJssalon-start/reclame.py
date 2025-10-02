from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {prijs_na_korting:.2f} euro.'''
    return uitvoer

print(aanbieding_1('aardbei', 4, 0.1))


def inkomsten_totaal(inkomsten,btw=0.09):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    return uitvoer

inkomsten_week = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten_week, 0.09))


def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]


inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(inkomsten))


def gemiddelde(mijn_lijst):
    gemiddelde_waarde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten))


def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(lijst)
print(resultaat)


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer




