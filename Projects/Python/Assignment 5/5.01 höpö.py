nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    mode = input("Haluatko poistaa vai lisätä nimiä? (l/p) ")
    if mode == "l":
        etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")
    elif mode == "p":
        etunimi = input("Anna poistettava nimi: ")
        nimet.remove(etunimi)

for nimi in nimet:
    print(f"Moi, {nimi}!")