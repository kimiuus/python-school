inventory = []
from classes.hahmot import *
import json
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
def stats(pelhahmo):
    print(f"Name: {pelhahmo.nimi} \nLocation: {pelhahmo.sijainti.nimi} \nSpeed: {pelhahmo.spd} \nStamina: {pelhahmo.sta} \nPower: {pelhahmo.pwr} \nGuts: {pelhahmo.gts} \nWisdom: {pelhahmo.wit}")