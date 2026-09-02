yritys = 1
tunnus = input("Syötä käyttäjätunnus: ")
salasana = input("Syötä salasana: ")
while tunnus != ("python") or salasana != ("rules"):
    if yritys < 5:
        yritys = yritys + 1
        print("Pääsy evätty")
        tunnus = input("Syötä käyttäjätunnus: ")
        salasana = input("Syötä salasana: ")
    elif yritys == 5:
        print("Maksimimäärä yrityksiä saavutettu")
        break
if tunnus == ("python") and salasana == ("rules"):
    print("Tervetuloa")