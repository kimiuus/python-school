nimet = set()
while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
        continue
for nimi in nimet:
    print(nimi)