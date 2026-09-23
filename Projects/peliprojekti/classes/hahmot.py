# spd = Speed, sta = Stamina, pwr = Power, gts = Guts, wit = Wisdom
class Hahmo:
    def __init__(self, nimi, spd, sta, pwr, gts, wit):
        self.nimi = nimi
        self.spd = spd
        self.sta = sta
        self.pwr = pwr
        self.gts = gts
        self.wit = wit

hahmo1 = Hahmo("Seiun Sky", 120, 120, 108, 101, 101)
hahmo2 = Hahmo("Chrono Genesis", 116, 109, 106, 100, 119)
hahmolista = [hahmo1, hahmo2]
for hahmo in hahmolista:
    print(vars(hahmo))