""" 4 Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

x = int(input("Add meg az első számot!: "))
y = int(input("Add meg a második számot!: "))
z = int(input("Add meg a harmadik számot!: "))

if x > y and x > z:
    print("A legnagyobb szám a 3 közül: az első" )
elif y > x and y > z:
    print("A legnagyobb szám a 3 közül: a második" )
elif z > x and z > y:
    print("A legnagyobb szám a 3 közül: a harmadik" )
