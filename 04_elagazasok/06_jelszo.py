"""
6 Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.

"""

jelszo = input('Add meg a jelszavad!: ')

if jelszo == ('junior'):
    print("Belépés engedélyezve!")
else:
    print("Belépés megtagadva!")