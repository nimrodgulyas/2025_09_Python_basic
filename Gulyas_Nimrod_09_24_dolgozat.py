"""
A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!
"""


szalaghossz = int(input("Adja meg a szalag hosszát!: "))
labdaatmero = int(input("Adja meg a labda átmérőjét!: "))
labdaszam = int(input("Adja meg a labdák számát!: "))

r = labdaatmero / 2
PI = 3.14
d = labdaatmero
labdakerulet = d*PI + 60
vegsohossz = labdaszam * 2 * labdakerulet
maradek = szalaghossz - vegsohossz
kellmeg = vegsohossz - szalaghossz
print(f'Labda kerülete: {labdakerulet}')
if szalaghossz == vegsohossz:
    print(f'A szalag pontosan elég hosszú, azaz: {vegsohossz} cm.')
elif szalaghossz < vegsohossz:
    print(f'A szalag túl rövid! Kell még: {kellmeg} cm szalag')
else:
    print(f'A szalag elég hosszú! A maradék szalag: {maradek} cm szalag')
