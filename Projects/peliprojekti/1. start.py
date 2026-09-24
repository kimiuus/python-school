import random
import json
inventory = []
wit = int(8)
spd = int(110)
from main import *
from classes.hahmot import *
hahmotlista = list(hahmolista)

print("Aloita uusi peli vai jatka? (1 tai 2)")
jatka = input("")
if jatka == "2":
    username = input("Syötä nimi: ")
    with open(f"data/{username}_savedata.json", "r") as saves:
        pelihahmo = json.load(saves)
        print(f"Nimi: {pelihahmo["spd"]}")
        pelhahmo = Hahmo(f"{pelihahmo["nimi"]}", f"{pelihahmo["spd"]}", f"{pelihahmo["sta"]}", f"{pelihahmo["pwr"]}", f"{pelihahmo["gts"]}", f"{pelihahmo["wit"]}")
elif jatka == "1":
    nimi = input("Syötä nimi: ")
    while True:
        try:
            ikä = int(input("Syötä ikä: "))
            break
        except ValueError:
            print("Virhe: Ei luku")
    if ikä < 12:
        print("Alaikäinen käyttäjä, ohjelma sulkeutuu")
        quit()
    else:print(f"Hei {nimi}, ikä {ikä}")
    print("Hopeful Stakes Simulator")
    print("Komennot: \n1. Aloita \n2. Debug \n3. Tavarat \n4. Statstest \n5. Lopeta")

if jatka == "1":
    komento = input("Syötä komento: ")
    while komento != ("Lopeta"):
        if komento == ("Aloita"):
            print("Valitse hahmo (1 tai 2)")
            for hahmo in hahmotlista:
                print((hahmo.nimi))
            valinta = int(input(""))
            while valinta not in [1,2]:
                print("Virhe")
                valinta = int(input(""))
            if valinta == 1:
                print(f"{hahmo1.nimi} valittu")
                pelhahmo = hahmo1
            elif valinta == 2:
                print(f"{hahmo2.nimi} valittu")
                pelhahmo = hahmo2
            print("Aloitetaan")
            break
        if komento == ("Debug"):
            esineet()
            komento = input("Syötä komento: ")
        elif komento == ("Tavarat"):
            viewinv()
            komento = input("Syötä komento: ")
        elif komento == ("Statstest"):
            wit, spd = stattest(wit, spd)
            print(f"Spd: {spd}, Wit: {wit}")
            komento = input("Syötä komento: ")
        elif komento != ("Debug") or komento != ("Tavarat") or komento != ("Statstest"):
            print("Ei komento.")
            komento = input("Syötä komento: ")
    if komento == ("Lopeta"):
        print("Sammutetaan ohjelma")
        quit()

# Aloitus
print()
turn = 1
while turn < 10:
    komento = input("\nAlue \nStats \nShop \nMenu\n")
    if komento == "Stats":
        print(vars(pelhahmo))
    elif komento == "Menu":
        print("\nPaused \nSave \nQuit \nBack")
        komento = input("")
        if komento == "Quit":
            quit()
        elif komento == "Back":
            pass
        elif komento == "Save":
            res = json.dumps(pelhahmo.__dict__)
            with open(f"data/{nimi}_savedata.json", "w") as saves:
                saves.write(res)
    turn += 1