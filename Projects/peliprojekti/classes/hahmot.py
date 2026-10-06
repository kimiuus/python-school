# spd = Speed, sta = Stamina, pwr = Power, gts = Guts, wit = Wisdom
import random
class Hahmo:
    def __init__(self, nimi, sijainti, spd: int, sta: int, pwr:int , gts:int, wit:int):
        self.nimi = nimi
        self.sijainti = sijainti
        self.spd = spd
        self.sta = sta
        self.pwr = pwr
        self.gts = gts
        self.wit = wit
        self.inventory = []
    def savechar(self):
        return {
            "nimi": self.nimi,
            "sijainti": self.sijainti.nimi,
            "spd": self.spd,
            "sta": self.sta,
            "pwr": self.pwr,
            "gts": self.gts,
            "wit": self.wit
            }

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino
    def __repr__(self):
        return f"{self.nimi}: {self.paino}kg\n"
            
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
            stat1 = random.randint(8, 15) * trnmod
            stat2 = random.randint(2,5) * trnmod
            spd = int(pelhahmo.spd) + stat1
            pwr = int(pelhahmo.pwr) + stat2
            pelhahmo.spd = int(spd)
            pelhahmo.pwr = int(pwr)
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{int(stat1)}, {att2} +{int(stat2)}")
        if sijainti == pool:
            att1 = "Stamina"
            att2 = "Guts"
            stat1 = random.randint(8, 13) * trnmod
            stat2 = random.randint(4,6) * trnmod
            sta = int(pelhahmo.sta) + stat1
            gts = int(pelhahmo.gts) + stat2
            pelhahmo.sta = int(sta)
            pelhahmo.gts = int(gts)
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{int(stat1)}, {att2} +{int(stat2)}")
        if sijainti == gym:
            att1 = "Power"
            att2 = "Stamina"
            stat1 = random.randint(9, 15) * trnmod
            stat2 = random.randint(6,8) * trnmod
            pwr = int(pelhahmo.pwr) + stat1
            sta = int(pelhahmo.sta) + stat2
            pelhahmo.pwr = int(pwr)
            pelhahmo.sta = int(sta)
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{int(stat1)}, {att2} +{int(stat2)}")
        if sijainti == hill:
            att1 = "Guts"
            att2 = "Power"
            att3 = "Speed"
            stat1 = random.randint(8, 12) * trnmod
            stat2 = random.randint(3,6) * trnmod
            stat3 = random.randint(3,6) * trnmod
            gts = int(pelhahmo.gts) + stat1
            pwr = int(pelhahmo.pwr) + stat2
            spd = int(pelhahmo.spd) + stat3
            pelhahmo.gts = int(gts)
            pelhahmo.pwr = int(pwr)
            pelhahmo.spd = int(spd)
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{int(stat1)}, {att2} +{int(stat2)}, {att3} +{int(stat3)}")
        if sijainti == library:
            att1 = "Wisdom"
            att2 = "Speed"
            stat1 = random.randint(9, 15) * trnmod
            stat2 = random.randint(3,5) * trnmod
            wit = int(pelhahmo.wit) + stat1
            spd = int(pelhahmo.spd) + stat2
            pelhahmo.wit = int(wit)
            pelhahmo.spd = int(spd)
            pelhahmo.sijainti = sijainti
            print(f"Location = {sijainti.nimi} \n {att1} +{int(stat1)}, {att2} +{int(stat2)}")
        rng = random.randint(1,3)
        if rng == 3:
            global esinum
            if esinum < 2:
                huoneenesine = esinelista[esinum]
                (sijainti).esine.append(huoneenesine)
                print(f"Item found: {huoneenesine.nimi}")
                print("Add item to inventory? (Y/N)")
                while True:
                    add = input("")
                    if add == "Y" or add == "N":
                        break
                    else:
                        print("Invalid input")
                if add == "Y":
                    pelhahmo.inventory.append(huoneenesine)
                    print(f"{huoneenesine.nimi} added to inventory")
                    esinum += 1
                    return esinum
                elif add == "N":
                    print("Item skipped")
            elif esinum >= 2:
                totalsta = int(pelhahmo.sta) + 15
                pelhahmo.sta = totalsta
                print("Excellent training!\n +15 Stamina")



hahmo1 = Hahmo("Seiun Sky", None, 120, 120, 108, 101, 101)
hahmo2 = Hahmo("Chrono Genesis", None, 116, 109, 106, 100, 119)
hahmolista = [hahmo1, hahmo2]

start = Huone("Start")
track = Huone("Track")
pool = Huone("Pool")
gym = Huone("Gym")
hill = Huone("Hill")
library = Huone("Library")
huonelista = [track, pool, gym, hill, library]