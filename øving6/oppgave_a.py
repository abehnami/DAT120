# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:52:40 2021

@author: aron Behnami
"""



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
    

    
print(tid_dato)
print(tiden_fra_start)
print(trykk_absolut)
print(temperatur)
