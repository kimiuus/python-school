inventory = []
def esineet():
    esine = input("Syötä esineen nimi: ")
    inventory.append(esine)
def viewinv():
    print(f"Sinulla on: {inventory}")
def stattest(wit, spd):
    wit = wit + 6
    spd = spd + 2
    print(("Wit +6, Spd +2"))
    return (wit, spd)