def mijn_functie_1(getal):
    return getal * getal

print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))


def mijn_functie_2(getal1, getal2):
    uitvoer_lijst = []
    uitvoer_lijst.append(getal1 + getal2)
    uitvoer_lijst.append(getal1 - getal2)
    uitvoer_lijst.append(getal1 * getal2)
    uitvoer_lijst.append(getal1 // getal2)  
    return uitvoer_lijst


print(mijn_functie_2(12, 3))
print(mijn_functie_2(12, 2))
print(mijn_functie_2(10, 5))
print(mijn_functie_2(100, 20))

