class Auto:
    def __init__(self, rekisteri, maxspd, spd=0, matka=0):
        self.rekisteri = rekisteri
        self.maxspd = maxspd
        self.spd = spd
        self.matka = matka
auto = Auto("ABC-123", "142 km/h")
print(f"{auto.rekisteri}, {auto.maxspd}, {auto.spd}, {auto.matka}")