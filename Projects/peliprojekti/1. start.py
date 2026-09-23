inventory = []
wit = int(8)
spd = int(110)
from main import esineet, viewinv, stattest
from classes.hahmot import *
hahmotlista = list(hahmolista)

nimi = input("Syötä nimi: ")
while True:
    try:
        ikä = int(input("Syötä ikä: "))
        break
    except ValueError:
        print("Virhe: Ei luku")
if ikä < 12:
    print("Alaikäinen käyttäjä, ohjelma sulkeutuu")
else:print(f"Hei {nimi}, ikä {ikä}")
print("devtest versio 0.2")
print("Komennot: Aloita, Debug, Tavarat, Statstest, Lopeta")

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
komento = input("Valitse toiminto: ")
if komento == "Stats":
    print(vars(pelhahmo))