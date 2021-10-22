# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:37:56 2021

@author: aronb
"""


ordliste=dict()
with open("oving_1_rein_tekst.txt","r", encoding="utf_8") as fil:
    for linje in fil:
        ordene=linje.split()
        for ordet in ordene:
            ordet=ordet.lower()
            if ordet in ordliste:
                teller = ordliste[ordet]
                teller += 1
                ordliste[ordet] = teller
            else:
                ordliste[ordet] = 1
    for ordet in ordliste:
        print (f"ordet: ({ordet}) forekommer {ordliste[ordet]} ganger")
                 
        



