# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:46:10 2021

@author: aronb

Endre programmet fra oppgave c) til å i stedet regne 
ut gjennomsnittet av alle tallene.
 For å regne ut gjennomsnittet må du telle antall
 tall brukeren har skrevet
 inn og dele summen med antall tall.


"""

verdi1=int(input("skriv her et tall: "))
summen=0
antall=0
while verdi1 >=0:
    summen += verdi1
    antall +=1
    verdi2=int(input("skriv her et tall til: "))
print("gjennomsnitt",summen/antall)       
print("Summen ble",summen)