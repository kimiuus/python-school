import random
import os
import json
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(os.getcwd())
inventory = []
wit = int(8)
spd = int(110)
from main import *
from classes.hahmot import *
hahmotlista = list(hahmolista)
huoneetlista = list(huonelista)
with open("intro.txt") as intro:
    print(intro.read())
with open("help.txt") as help:
    print(help.read())

print("Start a new game or continue? (1 / 2)")
jatka = input("")
if jatka == "2":
    username = input("Enter name: ")
    with open(f"data/{username}_savedata.json", "r") as saves:
        pelihahmo = json.load(saves)
        turn_loaded = pelihahmo["turn"]
        trnmod_loaded = pelihahmo["trnmod"]
        hahmo_loaded = Hahmo(**pelihahmo["pelihahmo"])
        print(f"Character: {hahmo_loaded.nimi} of user {username} loaded")
        pelhahmo = hahmo_loaded
elif jatka == "1":
    nimi = input("Enter name: ")
    while True:
        try:
            ikä = int(input("Enter age: "))
            break
        except ValueError:
            print("Error: Not a number")
    if ikä < 12:
        print("User underage, application closing.")
        quit()
    else:print(f"Hello {nimi}, Age {ikä}")
    print("Hopeful Stakes Simulator")
    print("Commands: \n1. Start \n2. Debug \n3. Items \n4. Statstest \n5. Quit")

if jatka == "1":
    komento = input("Enter command: ")
    while komento != ("Quit"):
        if komento == ("Start") or komento == "1":
            print("Select a character (1 / 2)")
            for hahmo in hahmotlista:
                print((hahmo.nimi))
            while True:
                valinta = input("")
                if valinta == "1" or valinta == "2":
                    valinta = int(valinta)
                    break
                else:
                    print("Invalid input")
            if valinta == 1:
                print(f"{hahmo1.nimi} chosen")
                pelhahmo = hahmo1
            elif valinta == 2:
                print(f"{hahmo2.nimi} chosen")
                pelhahmo = hahmo2
            print("Starting game...")
            break
        if komento == ("Debug") or komento == "2":
            esineet()
            komento = input("Enter command: ")
        elif komento == ("Items") or komento == "3":
            viewinv()
            komento = input("Enter command: ")
        elif komento == ("Statstest") or komento == "4":
            wit, spd = stattest(wit, spd)
            print(f"Spd: {spd}, Wit: {wit}")
            komento = input("Enter command: ")
        elif komento != ("Debug") or komento != ("Items") or komento != ("Statstest"):
            print("Not a command.")
            komento = input("Enter command: ")
    if komento == ("Quit") or komento == 5:
        print("Shutting down...")
        quit()

# Aloitus
# Variables: turn = Vuoro, trnmod = Ominaisuuksien saannin kerroin 
print()
if jatka =="2":
    turn = turn_loaded
    trnmod = trnmod_loaded
else:
    turn = 1
    trnmod = 1
pelhahmo.sijainti = start
while turn < 10:
    print(f"Turn: {turn} Training Modifier: {trnmod}")
    komento = input("\nArea \nStats \nInventory \nMenu\n")
    if komento == "Area" or komento == "1":
        while True:
            sijainti = input(" 1. Track \n 2. Pool \n 3. Gym \n 4. Hill \n 5. Library \n")
            if sijainti == "1" or sijainti == "2" or sijainti == "3" or sijainti == "4" or sijainti == "5":
                sijainti = int(sijainti)
                break
            else:
                print("Invalid input")
        coord = -1 + sijainti
        pelhahmo.sijainti = huoneetlista[(coord)]
        huone = huoneetlista[(coord)]
        huone.generate(huone, pelhahmo, trnmod)
        turn += 1
    elif komento == "Stats" or komento == "2":
        stats(pelhahmo)
    elif komento == "Inventory" or komento == "3":
        if len(pelhahmo.inventory) < 1:
            print("No items")
        else:
            print(pelhahmo.inventory)
            while True:
                use = input("Use item? (Y/N)\n")
                if use == "Y" or input == "N":
                    break
                else:
                    print("Invalid command")
            if use == "Y":
                multiplier = 1
                while True:
                    try:
                        itemnum = int(input("Enter item number: "))
                        if itemnum <= len(pelhahmo.inventory):
                            break
                    except ValueError:
                        print("Enter a number!")
                    else:
                        print("Invalid input")
                listnum = 1 - itemnum
                esine = pelhahmo.inventory[listnum]
                print(f"Item used: {esine}")
                if esine == song1:
                    multiplier = 1.5
                if esine == song2:
                    spd = int(pelhahmo.spd) + 22
                    pelhahmo.spd = spd
                    print("Speed increased by 22")
                if esine == song3:
                    wit = int(pelhahmo.wit) + 22
                    pelhahmo.wit = wit
                    print("Wisdom increased by 22")
                pelhahmo.inventory.remove(esine)
                trnmod = trnmod * multiplier
            if use == "N":
                print("Returning to menu")
    elif komento == "Menu" or komento == "4":
        print("\nPaused \n \nSave \nQuit \nBack")
        komento = input("")
        if komento == "Save" or komento == "1":
            data ={
                "turn": turn,
                "trnmod": trnmod,
                "pelihahmo": pelhahmo.savechar()
            }
            with open(f"data/{nimi}_savedata.json", "w") as saves:
                json.dump(data, saves)
        elif komento == "Quit" or komento == "2":
            quit()
        elif komento == "Back" or komento == "3":
            pass
print("\nIt's race day! \nRunning styles are impacted by your stats")
print("Front Runner: Speed and Guts\nPace Chaser: Stamina and Speed\nLate Surger: Power and Wisdom \nEnd Closer: Guts and Wisdom")
print("Your current stats: ")
stats(pelhahmo)
while True:
    style = input("Select running style (1 - 4): \n1. Front \n2. Pace \n3. Late \n4. End\n")
    if style == "1" or style == "2" or style == "3" or style == "4":
        style = int(style)
        break
    else:
        print("Invalid input")
if style == 1:
    if pelhahmo.spd >= 175 and pelhahmo.gts >= 150:
        print("A front running victory leading the pack all the way! \nThe path to stardom starts here \nEnding 1: Front Success")
    else:
        print("Your stats were insufficient for victory, try again! \nEnding 1: Front Fail")
if style == 2:
    if pelhahmo.sta >= 175 and pelhahmo.spd >= 150:
        print("A pace chasing victory, keeping pace with the leaders until the final stretch! \nThe path to stardom starts here \nEnding 1: Pace Success")
    else:
        print("Your stats were insufficient for victory, try again! \nEnding 1: Pace Fail")
if style == 3:
    if pelhahmo.pwr >= 175 and pelhahmo.wit >= 150:
        print("A late surger victory, navigating through the pack and showcasing true strenght! \nThe path to stardom starts here \nEnding 1: Late  Success")
    else:
        print("Your stats were insufficient for victory, try again! \nEnding 1: Late  Fail")
if style == 4:
    if pelhahmo.wit >= 175 and pelhahmo.gts >= 150:
        print("An end closer, cutting through the whole pack to soar to victory at the final stretch! \nThe path to stardom starts here \nEnding 1: End Success")
    else:
        print("Your stats were insufficient for victory, try again! \nEnding 1: End Fail")