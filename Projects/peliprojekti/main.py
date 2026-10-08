inventory = []
from classes.hahmot import *
import json
# Ei käytetä pelissä, lisää menussa esine tavaraluetteloon
def esineet():
    esine = input("Syötä esineen nimi: ")
    inventory.append(esine)
# Näytä testitavaraluettelo
def viewinv():
    print(f"Sinulla on: {inventory}")
# Statstest komento päävalikossa, ei käytetä pelissä
def stattest(wit, spd):
    wit = wit + 6
    spd = spd + 2
    print(("Wit +6, Spd +2"))
    return (wit, spd)
# Palauttaa itse pelin hahmon muuttujat
def stats(pelhahmo):
    print(f"Name: {pelhahmo.nimi} \nLocation: {pelhahmo.sijainti.nimi} \nSpeed: {pelhahmo.spd} \nStamina: {pelhahmo.sta} \nPower: {pelhahmo.pwr} \nGuts: {pelhahmo.gts} \nWisdom: {pelhahmo.wit}")