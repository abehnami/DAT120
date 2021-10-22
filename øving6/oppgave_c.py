# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:00:57 2021

@author: aronb
"""

import matplotlib.pyplot as mp

tid_dato = []
tiden_fra_start = []
trykk_absolut = []
temperatur = []

tid_dato = []
tiden_fra_start = []
trykk_absolut = []
temperatur = []
x=1

with open("trykk_og_temperaturlogg.csv", "r", encoding="utf-8") as flist:
    for line in flist:
        line = line.strip()
        line = line.replace(",", ".")
        nylinje = line.split(";")
        if x != 1:
            tid_dato.append(nylinje[0])
            tiden_fra_start.append(float(nylinje[1]))
            trykk_absolut.append(float(nylinje[3]))
            temperatur.append(float(nylinje[4]))
        x += 1


mp.hist(temperatur)
mp.title("temperatur")

mp.show()
