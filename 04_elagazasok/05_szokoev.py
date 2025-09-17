"""5 Szökőév ellenőrző
Kérj be egy évet, és írd ki, hogy szökőév-e.
(Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""
ev = int(input("Adj meg egy évszámot!: "))

if ev % 4 == 0 and ev % 100 != 0 or ev % 400 == 0:
    print(f"{ev} " + "szökőév.")
else:
    print(f"{ev} " + "nem szökőév.")

# if ev % 400 == 0 and ev % 100 == 0:
#     print(f"{ev} " + "szökőév.")
# elif ev % 4 == 0 and ev % 100 !=0:
#     print(f"{ev} " + "szökőév.")