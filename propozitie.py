from functiiptimport import formula, propozitie
# = > ! / & 
print("Pentru simbolul IMPLICA folositi '>'")
print("Pentru simbolul ECHIVALENT folositi '='")
print("Pentru simbolul SAU folositi '/'")
print("Pentru simbolul SI folositi '&'")
print("Pentru simbolul NEGATIE folositi '!'")
print("Pentru simbolul TAUTOLOGIE folositi '1'")
print("Pentru simbolul CONTRADICTIE folositi '0'")
print("Rezolvarea consta din inlocuiri")
n = input("Introduceti sirul de simboluri: ")
# (((P/Q)&(!(R=S)))&(!(!Q)))
# ((((P/Q)&(!(R=S)))&(!((!Q)/T)))/(L=K))
# ((((P&Q)>R)&((!P)>T))&((((!Q)>U)&(!R))&(V>((!T)/(!U)))))
n = n.upper()
n = n.strip()
if propozitie(n):
    print("Este propozitie!")
else:
    print("Nu este propozitie!")


