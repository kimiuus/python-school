class Hissi:
    def __init__(self, alin, ylin, kerros=1):
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros

    def siirry_kerrokseen(self, kerrat):
        while self.kerros != kerrat:
            if self.kerros < kerrat:
                self.kerros_ylös()
            elif self.kerros > kerrat:
                self.kerros_alas()
        print(f"Kerros: {self.kerros}")
        return
    def kerros_ylös(self):
        self.kerros += 1
        return
    def kerros_alas(self):
        self.kerros -= 1
        return
class Talo:
    def __init__(self, alin, ylin, hissimäärä):
        self.hissit = []
        self.alin = alin
        self.ylin = ylin
        self.hissimäärä = hissimäärä
    def aja_hissiä(self, hissin: int, kerros):
        hissi = self.hissit[hissin]
        hissi.siirry_kerrokseen(kerros)
talo = Talo(1, 8, 2)
for i in range(talo.hissimäärä):
    hissi = Hissi(talo.alin, talo.ylin)
    talo.hissit.append(hissi)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 4)
for hissi in talo.hissit:
    print(hissi.kerros)