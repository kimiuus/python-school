numbers = []
num = input("Anna luku: ")
while not num.isnumeric():
    print("Ei numero!")
    num = input("Anna luku: ")
    if num.isnumeric():
        numbers.append(num)
while num != "":
    numbers.append(num)
    num = input("Anna seuraava luku: ")
    while not num.isnumeric():
        if num == "":
            break
        print("Ei numero!")
        num = input("Anna seuraava luku: ")
        if num.isnumeric():
            numbers.append(num)
print(f"Suurin: {max(numbers)} Pienin: {min(numbers)}")

# Toinen
luku = int(input("Syötä luku: "))
suurin = luku
pienin = luku
while True:
    try:
        luku = int(input("Syötä luku tai lopeta painamalla Enter: "))
        if luku > suurin:
            suurin = luku
        if luku < pienin:
            pienin = luku
    except ValueError:
        break
print(suurin)
print(pienin)