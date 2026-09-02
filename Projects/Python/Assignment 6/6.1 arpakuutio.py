import random
numerot = []
noppa = random.randint(1,6)
arpa = int(input("Anna arpakuutioiden määrä: "))
kerrat = 0
for luku in range(arpa):
    noppa = random.randint(1,6)
    numerot.append(noppa)
    kerrat = kerrat + 1
print(sum(numerot))