import random
luku = random.randint(1,10)
arvaus = float(input("Syötä numero 1-10: "))
while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri")
        arvaus = float(input("Syötä numero 1-10: "))
    elif arvaus < luku:
        print("Liian pieni")
        arvaus = float(input("Syötä numero 1-10: "))
print("Oikein")