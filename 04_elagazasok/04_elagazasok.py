# szam = int(input('Adj meg egy egész számot!: '))

# if szam < 0:
#     print("Negatív")
# elif szam > 0:
#     print("Pozitív")
# else:
#     print("Nulla")

"""Páros számra írja ki a program azt, hogy páros, a páratlanra azt, hogy páratlan"""

szam = int(input("Kérlek adj meg egy számot!: "))

if szam % 2 == 0 and szam != 0:
    print("Páros")

elif szam == 0:
    print("Nulla")

else:
    print("Páratlan")
