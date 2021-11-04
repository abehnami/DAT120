# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:53:33 2021

@author: aronb
"""

spørsmåler = []
svaralternativ = []
riktigsvar = []

with open("sporsmaalsfil.txt","r",encoding="utf-8") as kildefil:
    for linje in kildefil:
        tekst = linje.split(":")
        spørsmåler.append(tekst[0])
        tekst[1] = tekst[1].strip()
        tekst[1] = int(tekst[1])
        riktigsvar.append(tekst[1])
        sa_oppbygging = tekst[2].split(",")
        svaralternativ.append(sa_oppbygging)

#riktigsvar = [i.strip("") for i in riktigsvar]
        
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
        for a in range(len(self.svaralternativ)):
            resultat += f" {a}-" + self.svaralternativ[a] + "\n"
        return resultat
        
    

        
quez = []   

for a in range(8):
    quez.append(spørrespill(riktigsvar[a],spørsmåler[a],svaralternativ[a]))


score1 = 0 
score2 = 0 

for i in quez:
    print(i)
    player1 = int(input("svaret til spiller nr1: "))
    player2 = int(input("svaret til spiller nr2: "))
    
    if i.check(player1):
        print("\n")
        score1 += 1
        print(score1)
    
    if i.check(player2):
        print("\n")
        score2 += 1
        print(score2)
    
    
    
    
    
    
# if __name__ == "__main__":
#     antallspørsmål = 8
#     spørsmål = []
#     spørsmål_1 = spørrespill(riktigsvar[0],spørsmåler[0],svaralternativ[0])
#     print(spørsmål_1)
#     svar_1 = int(input("skriv her svaret ditt: "))
#     spørsmål_1.check(svar_1)
    
#     spørsmål_2 = spørrespill(riktigsvar[1],spørsmåler[1],svaralternativ[1])
#     print(spørsmål_2)
#     svar_2 = int(input("skriv her svaret ditt: "))
#     spørsmål_2.check(svar_2)
    
#     spørsmål_3 = spørrespill(riktigsvar[2],spørsmåler[2],svaralternativ[2])
#     print(spørsmål_3)
#     svar_3 = int(input("skriv her svaret ditt: "))
#     spørsmål_3.check(svar_3)
    
#     spørsmål_4 = spørrespill(riktigsvar[3],spørsmåler[3],svaralternativ[3])
#     print(spørsmål_4)
#     svar_4 = int(input("skriv her svaret ditt: "))
#     spørsmål_4.check(svar_4)
        
#     spørsmål_5 = spørrespill(riktigsvar[4],spørsmåler[4],svaralternativ[4])
#     print(spørsmål_5)
#     svar_5 = int(input("skriv her svaret ditt: "))
#     spørsmål_5.check(svar_5)
    
#     spørsmål_6 = spørrespill(riktigsvar[5],spørsmåler[5],svaralternativ[5])
#     print(spørsmål_6)
#     svar_6 = int(input("skriv her svaret ditt: "))
#     spørsmål_6.check(svar_6)
    
#     spørsmål_7 = spørrespill(riktigsvar[6],spørsmåler[6],svaralternativ[6])
#     print(spørsmål_7)
#     svar_7 = int(input("skriv her svaret ditt: "))
#     spørsmål_7.check(svar_7)
    
#     spørsmål_8 = spørrespill(riktigsvar[7],spørsmåler[7],svaralternativ[7])
#     print(spørsmål_8)
#     svar_8 = int(input("skriv her svaret ditt: "))
#     spørsmål_8.check(svar_8)