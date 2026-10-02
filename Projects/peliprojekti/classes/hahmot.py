# spd = Speed, sta = Stamina, pwr = Power, gts = Guts, wit = Wisdom
import random
class Hahmo:
    def __init__(self, nimi, sijainti, spd, sta, pwr, gts, wit):
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
    def useitem(self, esine):
        if esine == song1:
            trnmod += 1
        if esine == song2:
            pelhahmo.spd += 22
        if esine == song3:
            pelhahmo.wit += 22
        pelhahmo.inventory.remove(esine)
            
song1 = Esine("Make Debut", 0.2)
song2 = Esine("Full Speed Ahead", 0.2)
song3= Esine("Believe", 0.5)
esinelista = [song1, song2, song3]

stat1 = 0
stat2 = 0
globalesinum = 0
class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esine = []
    def generate(self, sijainti):
        rng = random.randint(5,5)
        if rng == 5:
            esinum = globalesinum
            huoneenesine = esinelista[esinum]
            (sijainti).esine.append(huoneenesine)
            print(f"Item found: {huoneenesine.nimi}")
            if esinum < 3:
                globalesinum += 1
                return globalesinum
            elif esinum >= 3:
                globalesinum = 0
                return globalesinum
        if sijainti == track:
            att1 = "Speed"
            att2 = "Power"
            stat1 = random.randint(8, 15)
            stat2 = random.randint(2,5)
            pelhahmo.sijainti = sijainti
        print(f"Location = {sijainti.nimi} \n {att1} +{stat1}, {att2} +{stat2}")


hahmo1 = Hahmo("Seiun Sky", None, 120, 120, 108, 101, 101)
hahmo2 = Hahmo("Chrono Genesis", None, 116, 109, 106, 100, 119)
hahmolista = [hahmo1, hahmo2]


track = Huone("Track")
pool = Huone("Pool")
gym = Huone("Gym")
hill = Huone("Hill")
library = Huone("Library")
huonelista = [track, pool, gym, hill, library]