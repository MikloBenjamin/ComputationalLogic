from functiiptimport import *
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
print("Rezolvarea consta din introducerea parantezelor unde e nevoie, dupa prioritatea conectorilor logici.")
n = input("Introduceti sirul de simboluri: ")
n = n.upper()
n = n.strip()
# ! & / > =
# P>!!!B=Q&S
# !P/B&Q>S>!!!B=Q&S
# !P/(!B&Q)=P
# P&Q=(Q/R)>P/R
# (!P=(Q&R))=((Q/!R)=P)
# ((!(P=(Q&R)))=((Q/!R)=P))
# (!P/Q/R)&(P/!R)&!Q/(!R&(!P)&R)
# (!P/Q>R)&(P/!R)&(!Q=!R)>!(P=R)
# (P=(P&Q))=!Q
# P=(P=Q)=Q
# (P>(P=Q)=Q)
# !P=!Q/!!R/!S

d = {}
 
for i in n:
    if i.isalpha():
        if i not in d.keys():
            d[i] = []
            
if not sintaxarelaxata(n):
    print("Simbolurile introduse nu sunt in sintaxa relaxata")
else:
    n = transfrelnorm(n, d)
    print(n)
    if propozitie(n):
        print("da")

