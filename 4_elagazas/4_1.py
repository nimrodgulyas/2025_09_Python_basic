"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random
random_number = random.randint(1,3)
szam = int(input('Adj meg egy számot 1 és 3 között!: '))
if szam == random_number:
    print('Erre a számra gondoltam!')
elif szam < random_number:
    print('Nagyobb számra gondoltam!')
elif szam > random_number:
    print('Kisebb számra gondoltam!')