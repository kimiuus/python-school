numero = int(input("Syötä numero: "))
if numero < 2:
    print("Ei alkuluku")
for luku in range(2, int(numero**0.5) + 1):
        if numero % luku == 0:
            print("Ei alkuluku")
            break
else:print("On alkuluku")