from functiiptimport import *
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
n = input("Introduceti sirul de simboluri: ")
n = n.strip()
# (P>Q)&!!!!!!!B=Q/S/(Q&R)
# 0&Q>1/!B/G
# P>!!!B=Q&S
# P>!B
# p>!b
# (P>Q)&!Q&!P
# (P>Q)>((Q>S)>((P/Q)>R))
# !(P>Q)=((P/Q)&(!P>Q))
# (P=Q)=(!(P>!Q))
# (!P=(Q&R))=((Q/!R)=P)
# (!P/Q/R)&(P/!R)&(!Q/!R)&!(P&R)
# (!P/Q>R)&(P/!R)&(!Q=!R)>!(P=R)
# (P=(P&Q))=!Q
carok = ">/&=!ABCDEFGHIJKLMNOPQRSTUVWXYZ10()"
n = n.upper()
d = {}
for i in n:
    if i.isalpha() or i in '10':
        if i not in d.keys():
            d[i] = []
if sintaxarelaxata(n):
    n = transfrelnorm(n, d)
    print('Da, sirul introdus este o propozitie in sintaxa relaxata, fiindca se poate scrie ca \n' + n + '\n' + 'Aplicand regulile de prioritate asupra conectorilor logici.')
else:
    print("Sirul introdus nu este a propozitie in sintaxa relaxata")