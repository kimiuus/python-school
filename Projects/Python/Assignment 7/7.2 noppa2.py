import random
def noppa(max):
    num = random.randint(1,max)
    return num
heitto = 1
h = 0
max = int(input("Syötä määrä: "))
while h != max:
    h = noppa(max)
    print(f"Heitto {heitto}: {h}")
    heitto = heitto + 1