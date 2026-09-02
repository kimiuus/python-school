nimi = input("Syötä nimi: ")
ikä = int(input("Syötä ikä: "))
if ikä < 12:
    print("Alaikäinen käyttäjä, ohjelma sulkeutuu")
else:print(f"Hei {nimi}, ikä {ikä}")
print("Päävalikko versio 0.1")
print("Komennot: Aloita, Ohjeet, Lopeta")
komento = input("Syötä komento: ")
while komento != ("Lopeta"):
    if komento == ("Aloita"):
        print("WIP")
        komento = input("Syötä komento: ")
    elif komento == ("Ohjeet"):
        print("kirjoitus   peli")
        komento = input("Syötä komento: ")
    elif komento != ("Aloita") or komento != ("Ohjeet"):
        print("Ei komento.")
        komento = input("Syötä komento: ")
if komento == ("Lopeta"):
    print("Sammutetaan ohjelma")