year = float(input("Enter year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("ye")
    else:print("nah")
elif year % 4 == 0:
    print("ye")
else:print("nah")