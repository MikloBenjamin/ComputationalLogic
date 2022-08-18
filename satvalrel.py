from functiiptimport import *
import time
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
print("Rezolvarea consta din inlocuiri si comparatii")
n = input("Introduceti sirul de simboluri: ")
n = n.strip()
# (((P/Q)&(!(R=S)))&(!(!Q)))
# (P>Q)&!Q&!P
# (P>Q)>((Q>S)>((P/Q)>R))
# !(P>Q)=((P/Q)&(!P>Q))
# (P=Q)=(!(P>!Q))
# (!P=(Q&R))=((Q/!R)=P)
# (!P/Q/R)&(P/!R)&(!Q/!R)&!(P&R)
# (!P/Q>R)&(P/!R)&(!Q=!R)>!(P=R)
# (P=(P&Q))=!Q
# (((P/Q)&(!(R=S)))&(!(!Q)))
# !P/1&Q=R
d = {}
n = n.upper()
transformat = 0
start = time.time()
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
    if transformat == 0:
        nr = 0
        for i in n:
            if i.isalpha() or i in '10':
                if i not in d.keys():
                    nr += 1
                    d[i] = []
    y = 1
    if '1' in d.keys():
        nr -= 1
    if '0' in d.keys():
        nr -= 1
    nr2 = 2**nr
    for i in d.keys():
        x = 0
        sw = 0
        c = 1
        while x < nr2:
            d[i].append(sw)
            if c == y:
                if sw == 1:
                    sw = 0
                else:
                    sw = 1
                c = 1
            else:
                c += 1
            x += 1
        y = y*2  
    
    interpretari = []

    for i in range(0, nr2):
        d2 = {}
        for j in d.keys():
            d2[j] = d[j][i]
        interpretari.append(d2)

    result = []
    print(interpretari)
    for i in interpretari:
        x = valoareadevar2(n, i)
        result.append(x)
    print(result)

    valid = '1'
    satisfiabil = '0'
    for i in result:
        if i == '1':
            satisfiabil = '1'
        if i == '0':
            valid = '0'
    if satisfiabil == '1':
        print("Satisfiabil")
    else:
        print("Nesatisfiabil")
    if valid == '1':
        print("Valid")
    else:
        print("Nevalid")
else:
    print("Nu este propozitie!")

durata = time.time() - start
print(durata)
