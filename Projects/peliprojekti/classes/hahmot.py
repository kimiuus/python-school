# spd = Speed, sta = Stamina, pwr = Power, gts = Guts, wit = Wisdom
import random
class Hahmo:
    def __init__(self, nimi, sijainti, spd: int, sta: int, pwr:int , gts:int, wit:int):
        self.inventory = []
        self.sijainti = sijainti
        self.nimi = nimi
        self.spd = spd
        self.sta = sta
        self.pwr = pwr
        self.gts = gts
        self.wit = wit

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino
    def __repr__(self):
        return f"{self.nimi}: {self.paino}kg\n"
    def useitem(self, esine, pelhahmo):
        global mult
        if esine == song1:
            mult = 2
        if esine == song2:
            spd = int(pelhahmo.spd) + 22
            pelhahmo.spd = spd
        if esine == song3:
            pelhahmo.wit += 22
        pelhahmo.inventory.remove(esine)
            
song1 = Esine("Make Debut", 0.2)
song2 = Esine("Full Speed Ahead", 0.2)
song3= Esine("Believe", 0.5)
esinelista = [song1, song2, song3]

stat1 = 0
stat2 = 0
esinum = 0
class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esine = []
    def generate(self, sijainti, pelhahmo, trnmod):
        if sijainti == track:
            att1 = "Speed"
            att2 = "Power"
            stat1 = random.randint(8, 15)
            stat2 = random.randint(2,5)
            spd = int(pelhahmo.spd) + (stat1 * trnmod)
            pwr = int(pelhahmo.pwr) + (stat2 * trnmod)
            pelhahmo.spd = spd
            pelhahmo.pwr = pwr
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{stat1}, {att2} +{stat2}")
        rng = random.randint(5,5)
        if rng == 5:
            global esinum
            huoneenesine = esinelista[esinum]
            (sijainti).esine.append(huoneenesine)
            print(f"Item found: {huoneenesine.nimi}")
            print("Add item to inventory? (Y/N)")
            add = input("")
            if add == "Y":
                pelhahmo.inventory.append(huoneenesine)
                print(f"{huoneenesine.nimi} added to inventory")
            elif add == "N":
                print("Item skipped")
            if esinum < 3:
                esinum += 1
                return esinum
            elif esinum >= 3:
                esinum = 0
                return esinum



hahmo1 = Hahmo("Seiun Sky", None, 120, 120, 108, 101, 101)
hahmo2 = Hahmo("Chrono Genesis", None, 116, 109, 106, 100, 119)
hahmolista = [hahmo1, hahmo2]


track = Huone("Track")
pool = Huone("Pool")
gym = Huone("Gym")
hill = Huone("Hill")
library = Huone("Library")
huonelista = [track, pool, gym, hill, library]