lu = 13.3
na = 13.3 * 32
le = na * 20
a = float(input("Talent value: "))
b = float(input("Nail value: "))
c = float(input("Bullet value: "))
num = (lu*c)+(na*b)+(le*a)
kg = int(num) // 1000
g = num % 1000
print(f"{kg} kilograms, {g:5.2f} grams")