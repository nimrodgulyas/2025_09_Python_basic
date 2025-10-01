
folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n'or valasz == 'nem':
        folytatja = False
    elif valasz == 'igen':
        print('i vagy n betűket használj')
print('>> Program vége! <<')      
