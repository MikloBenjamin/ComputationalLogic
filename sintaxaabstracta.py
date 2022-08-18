from functiiptimport import *
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
print("Rezolvarea consta din inlocuirea formulelor simple cu o lista din ele, formand astfel o lista din propozitie")
n = input("Introduceti sirul de simboluri: ")
n = n.upper()
# (((P/Q)&(!(R=S)))&(!(!Q)))
# ((P/Q)&(!(R=S))&(!(!Q)))
# ((P=Q)=(!(P>(!Q))))
# P>!!!B=Q&S
# !P/B&Q>S>!!!B=Q&S
# !P/(!B&Q)=P
# P&Q=(Q/R)>P/R
# (!P=(Q&R))=((Q/!R)=P)
# ((!(P=(Q&R)))=((Q/!R)=P))
# (!P/Q/R)&(P/!R)&(!Q/!R)&!(P&R)
# (!P/Q>R)&(P/!R)&(!Q=!R)>!(P=R)
# (P=(P&Q))=!Q
# P=(P=Q)=Q
# (P>(P=Q)=Q)
# 0&Q>1/!B/G  
d = {}
n = n.strip()
if not propozitie(n):
    if sintaxarelaxata(n):
        print("Simbolurile introduse formeaza o propozitie in sintaxa relaxata.")
        print("Transformam sirul din sintaxa relaxata intr-unul nerelaxat aplicand regulile de prioritate al conectorilor logici")
        nr = 0
        for i in n:
            if i.isalpha() or i in '10':
                if i not in d.keys():
                    nr += 1
                    d[i] = []
        n = transfrelnorm(n, d)
        transformat = 1
        print()
    else:
        print("Simbolurile introduse nu formeaza un propozitie ... ")
print("Verificam daca sirul este o propozitie ... ")
if propozitie(n):
    print()
    n = listadinp(n, [])
    print(n)
else:
    print("Nu este propozitie!")