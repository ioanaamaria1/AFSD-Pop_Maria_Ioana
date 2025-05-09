
import json
import random as rnd

resturi = []
bancnote, preturi = {}, {}
with open(__file__[:__file__.rfind('\\')+1] + 'jsonmagazin.json', 'r') as fisier_json:
    magazin = json.load(fisier_json)
    bancnote = magazin['bancnote']
    preturi = magazin['produse']
produse = list(preturi.keys())

chei = list(bancnote.keys())
for cheie in chei:
    bancnote[int(cheie)] = bancnote[cheie]
    bancnote.pop(cheie)

while True:
    produs = rnd.choice(produse)
    pret = preturi[produs]
    platit = rnd.randint(pret + 1, pret + 20)
    rest = platit - pret
    oferit = []
    poate_da_rest = False
    temp = rest

    while rest >= len(resturi):
        resturi.append('')

    if resturi[rest] == '':
        for bancnota in bancnote.keys():
            numar = temp // bancnota
            if bancnota <= temp and bancnote[bancnota] >= numar:
                poate_da_rest = True
                oferit.append(f"{numar}x{bancnota}")
                temp %= bancnota
                bancnote[bancnota] -= numar
        oferit = ', '.join(oferit)
    else:
        poate_da_rest = True
        oferit = resturi[rest]

    print()
    print('-' * 50)
    print()
    print(f"Produs cumparat: {produs}")
    print(f"Pret produs: {pret}")
    print(f"Platit: {platit}")

    if poate_da_rest:
        print(f"Rest: {rest} - {oferit}")
    else:
        print('Rest: 0')
        print(f"        Lipsesc {temp} unitati pentru a da rest\n")
        break
