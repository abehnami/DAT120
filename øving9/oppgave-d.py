# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:53:33 2021

@author: aronb
"""

spørsmål = dict()
svar_alternativ = dict()
riktig_svar = dict()

with open("sporsmaalsfil.txt","r",encoding="utf-8") as kildefil:
    for linje in kildefil:
        linje = linje.split("?")
        spørsmål = linje