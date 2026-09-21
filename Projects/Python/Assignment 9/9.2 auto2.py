class Auto:
    def __init__(self, rekisteri, maxspd: int, spd=0, matka=0):
        self.rekisteri = rekisteri
        self.maxspd = maxspd
        self.spd = (f"{spd} km/h")
        self.matka = matka
    def kiihdytä(self, kmh):
        self.spd += kmh
        if self.spd > self.maxspd:
            self.spd = self.maxspd
        elif self.spd < 0:
            self.spd = 0
        return self.spd
auto = Auto("ABC-123", 142)
print(f"{auto.rekisteri}, {auto.maxspd}, {auto.spd}, {auto.matka}")
auto.kiihdytä(30)
print(auto.spd)
auto.kiihdytä(70)
print(auto.spd)
auto.kiihdytä(50)
print(auto.spd)
auto.kiihdytä(-200)
print(auto.spd)