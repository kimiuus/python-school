inventory = []
wit = int(8)
spd = int(110)
from scr import esineet, viewinv, stattest
nimi = input("Syötä nimi: ")
ikä = int(input("Syötä ikä: "))
if ikä < 12:
    print("Alaikäinen käyttäjä, ohjelma sulkeutuu")
else:print(f"Hei {nimi}, ikä {ikä}")
print("devtest versio 0.2")
print("Komennot: Debug, Tavarat, Statstest, Lopeta")
komento = input("Syötä komento: ")
while komento != ("Lopeta"):
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