# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:15:12 2021

@author: aronb
"""


tid_dato = []
tiden_fra_start = []

x=1

with open("trykk_og_temperaturlogg.csv", "r", encoding="utf-8") as flist:
    for line in flist:
        line = line.strip()
        line = line.replace(",", ".")
        nylinje = line.split(";")
        if x != 1:
            tid_dato.append(nylinje[0])
            tiden_fra_start.append(float(nylinje[1])) 
            
        x += 1

for antall in range(len(tiden_fra_start)-1):
    diff = tiden_fra_start[antall+1]-tiden_fra_start[antall]
    if diff != 10:
       print("line: " + tid_dato[antall])
       print(diff)
       