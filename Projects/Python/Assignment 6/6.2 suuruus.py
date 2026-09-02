numbers = []
num = input("Syötä numero: ")
while num != "":
    numbers.append(num)
    num = input("Syötä seuraava numero: ")
numbers.sort(key=int, reverse=True)
print(numbers[0:5])