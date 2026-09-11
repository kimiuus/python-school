kuukaudet = ("kevät", "kesä", "syksy", "talvi")
while True:
    kk = int(input("Syötä kuukausi lukuna: "))
    if kk in (1, 2, 3):
        print(kuukaudet[0])
        break
    elif kk in (4, 5, 6):
        print(kuukaudet[1])
        break
    elif kk in (7, 8, 9):
        print(kuukaudet[2])
        break
    elif kk in (10, 11, 12):
        print(kuukaudet[3])
        break
    else:
        print("Virheellinen luku")
        continue