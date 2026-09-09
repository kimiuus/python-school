lista = []
num = 0
def jako(lista):
    for num in (lista):
        if num % 2 == 0:
            print(num)
while num != "":
    try:
        num = int(input("Syötä seuraava kokonaisluku: "))
        lista.append(num)
    except ValueError:
        break
print(lista)
jako(lista)