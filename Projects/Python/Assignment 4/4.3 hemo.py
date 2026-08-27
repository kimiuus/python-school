g = input("Biological gender (f/m): ")
value = float(input("Hemoglobin value (g/l): "))
if g == "m" and value < 117 or g == "f" and value < 134:
    print("Hemoglobin low")
elif g == "m" and value > 175 or g == "f" and value > 195:
    print("Hemoglobin high")
else:print("Hemoglobin normal")