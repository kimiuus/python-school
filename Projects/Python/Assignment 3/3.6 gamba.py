# Uudelleentehty 28.8, alkuperäinen aikasemmin
import random
num = 1
luku1 = random.randint(0,9)
print("Lukkokoodi 3, 0-9")
while num < 4:
    print(luku1)
    luku1 = random.randint(0,9)
    num = num + 1
num2 = 1
luku2 = random.randint(1,6)
print("Lukkokoodi 4, 1-6")
while num2 < 5:
    print(luku2)
    luku2 = random.randint(1,6)
    num2 = num2 + 1
# Alkuperäinen
print("Lukkokoodi 3, 0-9")
print(random.randint(0,9),random.randint(0,9),random.randint(0,9))
print("Lukkokoodi 4, 1-6")
print(random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))