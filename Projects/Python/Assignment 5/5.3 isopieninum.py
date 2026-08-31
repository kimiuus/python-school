numbers = []
num = input("Anna luku: ")
numbers.append(num)
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