class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittata = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittata}, Sivut: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, julkaisija):
        self.julkaisija = julkaisija
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Julkaisija: {self.julkaisija}")

j = Julkaisu
julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytto n:o 6", "Rosa Liksom", "200 sivua"))
for j in julkaisut:
    j.tulosta_tiedot()