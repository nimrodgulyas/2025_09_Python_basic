"""
7 Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”


0-20: „Hűvös, kabát ajánlott.”


21-30: „Kellemes idő.”


30 felett: „Forróság, igyál sok vizet!”
"""
homerseklet = int (input('Kérlek add meg a hőmérsékletet Celsius fokban!: '))

if homerseklet < 0:
    print('Nagyon hideg, öltözz melegen!')

elif homerseklet >= 0 and homerseklet <= 20:
    print('Hűvös, kabát ajánlott.')

elif homerseklet >= 21 and homerseklet <= 30:
    print('Kellemes idő.')

else:
    print('Forróság, igyál sok vizet!')