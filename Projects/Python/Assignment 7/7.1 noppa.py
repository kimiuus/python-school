import random
def noppa():
    return random.randint(1,6)
heitto = 1
h = 0
while h != 6:
    h = noppa()
    print(f"Heitto {heitto}: {h}")
    heitto = heitto + 1