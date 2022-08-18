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
# (((P/Q)&(!(R=S)))&(!(!Q)))
# ((((P/Q)&(!(R=S)))&(!((!Q)/T)))/(L=K))
# ((((P&Q)>R)&((!P)>T))&((((!Q)>U)&(!R))&(V>((!T)/(!U)))))
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
# !P/1&Q=R
d = {}
n = n.upper()
transformat = 0
start = time.time()
n = n.strip()
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
        if i in '10':
            d[i] = i
        else:
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
            if j in '10':
                d2[j] = j
            else:
                d2[j] = d[j][i]
        interpretari.append(d2)


    listpoz = []
    listprop = []
    listpozend = []
    pozx = 0
    pozd = 0
    pozi = 0

    for i in range(0, n.count('(')):
        listpoz.append([])
        listpozend.append([])
    for i in range (0, len(n)):
        if n[i] == '(':
            listpoz[pozd].append(i)
            pozd += 1
            pozx += 1
        elif n[i] == ')':
            for j in range(pozx, -1 , -1):
                if len(listpozend[j - 1]) < 1:
                    listpozend[j - 1].append(i)
                    break

    #print(listpozend)
    for i in range(0, len(listpozend)):
        listpoz[i].append(listpozend[i][0])
    #print(listpoz)

    elementepttabel = []
    for i in listpoz:
        elementepttabel.append(n[i[0]:i[1] + 1])

    for i in range(0, len(elementepttabel)):
        for j in range(i+1, len(elementepttabel)):
            if len(elementepttabel[i]) > len(elementepttabel[j]):
                elementepttabel[i],elementepttabel[j] = elementepttabel[j], elementepttabel[i]

    for i in d.keys():
        print(i,' ', end = '')
        if i not in '10':
            for j in d[i]:
                print(j, ' ', end = '')
            print()
        else:
            print(i)
    
    Result = []

    for j in elementepttabel:
        print(j,' ')
        result = []
        for i in interpretari:
            x = valoareadevar2(j, i)
            result.append(x)
        Result.append(result)
        for q in result:
            print(q,' ', end = '')
        print()
    
    
    print("Tabelul de adevar : ")
    for i in d.keys():
        print(i,' ', end = '')
        for j in d[i]:
            print(j, ' ', end = '')
        print()    
    for i in range(0, len(elementepttabel)):
        print(elementepttabel[i], ' ', end = '')
        for j in Result[i]:
            print(j,' ', end = '')
        print()
else:
    print("Nu este propozitie!")

durata = time.time() - start
print(durata)
