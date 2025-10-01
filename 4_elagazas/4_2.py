"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

import random
x = random.randint(1,2)
fej = 1
iras = 2
feldobas = int(input('Fej vagy írás? (A fej az 1es, az írás a 2es.): '))
if x == feldobas:
    print('Eltaláltad!')
else:
    print('Sajnos nem találtad el!')