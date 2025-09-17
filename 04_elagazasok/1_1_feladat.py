"""
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

"""
valasz1 = input('Jó napod van? "Igennel" vagy "Nemmel" válaszolj! ')

if valasz1 == ('Igen'):
    print('Akkor maradjon is így!')
elif valasz1 == ('Nem'):
    print('Remélem minden rendben, fel a fejjel!')

# 1.2 feladat

else:
    print('Sajnos nem értem a válaszodat!')