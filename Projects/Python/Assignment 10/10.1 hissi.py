class Hissi:
    def __init__(self, alin=1, ylin=8, kerros=1):
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros

    def siirry_kerrokseen(self, kerrat):
        while self.kerros != kerrat:
            if self.kerros < kerrat:
                h.kerros_ylös()
            elif self.kerros > kerrat:
                h.kerros_alas()
        print(f"Kerros: {self.kerros}")
        return
    def kerros_ylös(self):
        self.kerros += 1
        return
    def kerros_alas(self):
        self.kerros -= 1
        return
h = Hissi()
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)