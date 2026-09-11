numbers = []
num = input("Syötä numero: ")
while num != "":
    numbers.append(num)
    num = input("Syötä seuraava numero: ")
numbers.sort(key=int, reverse=True)
for num in numbers:
    print(num)