"""
1️ Páros vagy páratlan?
Kérj be egy egész számot, és írd ki, hogy páros-e vagy páratlan.
2️ Pozitív, negatív vagy nulla
Kérj be egy számot, és állapítsd meg, hogy pozitív, negatív vagy nulla.
3️ Jegyosztályozás
Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen


50–64: Elégséges


65–79: Közepes


80–89: Jó


90–100: Jeles


"""

pontszam = int(input("Add meg az elért pontszámot!: "))
if pontszam <= 100 and pontszam >= 90:
    print("Jeles")

elif pontszam <= 89 and pontszam >= 80:
    print("Jó")

elif pontszam <= 79 and pontszam >= 65:
    print("Közepes")

elif pontszam <= 64 and pontszam >= 50:
    print("Elégéséges")

elif pontszam <= 49 and pontszam >= 0:
    print("Elégtelen")

else:
    print("Hibás számot adtál meg!")