lista = []
num = 0
def summa(lista):
    y = sum(lista)
    return y
while num != "":
    try:
        num = int(input("Syötä seuraava kokonaisluku: "))
        lista.append(num)
    except ValueError:
        break
print(summa(lista))