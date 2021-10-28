# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:34:43 2021

@author: aronb
"""

class spørrespill:
    def __init__(self ,riktig ,spørsmål ,svaralternativ):
        self.riktig = riktig
        self.spørsmål = spørsmål
        self.svaralternativ = svaralternativ
        
    def check(self,svaret):
        if svaret == self.riktig:
            return print("svaret ditt er riktig" +"\n")
        else:
            return print("svaret ditt er feil" +"\n")
    
    def __str__(self):
        resultat = self.spørsmål + "\n"
        for svaret in self.svaralternativ:
            resultat += svaret + "\n"
        return resultat
    
    


if __name__ == "__main__":
    antallspørsmål = 3
    spørsmål = []
    spørsmål_1 = spørrespill(3,"hvor mange dager i året?",["12 (tast 0)","30 (tast 1)","360 (tast 2)","365 (tast 3)"])
    print(spørsmål_1)
    svar_1 = int(input("skriv her svaret ditt: "))
    spørsmål_1.check(svar_1)
    
    spørsmål_2 = spørrespill(1,"hva er kvadratrot av 9?",["27 (tast 0)","3 (tast 1)","82 (tast 2)","99 (tast 3)"])
    print(spørsmål_2)
    svar_2 = int(input("skriv her svaret ditt: "))
    spørsmål_2.check(svar_2)
    
    spørsmål_3 = spørrespill(2,"hva er 3+6/2?",["6 (tast 0)","12 (tast 1)","4.5 (tast 2)","10 (tast 3)"])
    print(spørsmål_3)
    svar_3 = int(input("skriv her svaret ditt: "))
    spørsmål_3.check(svar_3)
        