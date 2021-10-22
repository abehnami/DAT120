# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:58:48 2021

@author: aronb
"""

import matplotlib.pyplot as mp

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
 

x_kordinat=(tiden_fra_start)
y_kordinat=(trykk_absolut)
y_kordinat2=(temperatur)

mp.subplot(2,2,1)
mp.plot(x_kordinat,y_kordinat,"-",color="blue")
mp.title("trykk")
mp.xlabel("tid")
mp.ylabel("trykk_absolut")

mp.subplot(2,2,2)
mp.plot(x_kordinat,y_kordinat2,"-",color="red")
mp.title("temperatur")
mp.xlabel("tid")
mp.ylabel("temperatur")

mp.show()