lento = {"EFHK": "Helsinki-Vantaan lentoasema"}
while True:
    print("Komennot: Lisää uusi asema (add), etsi tiedoissa olevaa asemaa (find), lopeta (quit)")
    k = input()
    if k == "quit":
        break
    elif k == "add":
        koodi = input("Syötä ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lento[koodi] = nimi
    elif k == "find":
        koodi = input("Syötä ICAO-koodi: ")
        if koodi in lento:
            print(f"{lento[koodi]}")
        else:
            print("Ei tiedoissa")