from functiiptimport import *
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
print("Rezolvarea consta din desfacerea problemei in mai multe subprobleme, dupa care")
print("inlocuim subproblema cu rezultatul subproblemei in problema parinte")
n = input("Introduceti sirul de simboluri: ")
n = n.upper()
n = n.strip()
# ((P/Q)&(!(R=S))&(!(!Q)))
# ((P=(P&Q))=(!Q))
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
d = {}
transformat = 0
if not propozitie(n):
    if sintaxarelaxata(n):
        print("Simbolurile introduse formeaza o propozitie in sintaxa relaxata.")
        print("Transformam sirul din sintaxa relaxata intr-unul nerelaxat :))")
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
        print("Simbolurile introduse nu formeaza un propozitie")
if propozitie(n):
    print()
    d = {}
    for i in n:
        if i.isalpha():
            if i not in d.keys():
                print("Valoare de adevar pentru ", i, " (1 pentru adevarat si 0 pentru fals) este : ", end = '')
                d[i] = int(input(""))
        elif i in '10':
            d[i] = int(i)
    n = listadinp(n, [])
    print(valoareadevar(n, d))
else:
    print("Simbolurile introduse nu formeaza o propozitie!")