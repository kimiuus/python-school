from math import pi
def pizza(num, hinta):
    h = num / 100
    p = pi*(h*h)
    c = hinta / p
    return c
num = int(input("Syötä halkaisija: "))
hinta = int(input("Syötä hinta: "))
pizza1 = pizza(num, hinta)
num = int(input("Syötä seuraava halkaisija: "))
hinta = int(input("Syötä seuraava hinta: "))
pizza2 = pizza(num, hinta)
if pizza1 > pizza2:
    print(f"Pizza 2 {pizza2:.3}€/neliömetri on halvempi kun pizza 1 {pizza1:.3}€/neliömetri")
else:print(f"Pizza 1 {pizza1:.3}€/neliömetri on halvempi kun pizza 2 {pizza2:.3}€/neliömetri")