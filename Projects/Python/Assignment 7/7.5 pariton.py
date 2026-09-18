def jako(lista):
    for num in (lista):
        if num % 2 == 0:
            lista2.append(num)
    return lista2
lista = []
lista2 = []
num = 0
while num != "":
    try:
        num = int(input("Syötä seuraava kokonaisluku: "))
        lista.append(num)
    except ValueError:
        break
uusi = jako(lista)
print(lista)
print(uusi)