def formula(s):
    #print(s)
    #print(len(s))
    if len(s) == 1:
        if s.isalpha() or s in '01':
            return 1
    else:
        if len(s) == 5:
            if s[0] == '(':
                if s[4] == ')':
                    if s[1].isalpha() or s[1] in '01':
                        if s[2] in ['=','>','!','/','&']:
                            if s[3].isalpha() or s[3] in '01':
                                return 1
        else:
            if s[0] == '(':
                if s[3] == ')':
                    if s[1] == '!':
                        if s[2].isalpha() or s[2] in '01':
                            return 1
    return 0


def propozitie(n):
    pozlast = []
    i = 0
    while i + 4 < len(n):
        if n[i] == '(':
            if n[i+3] == ')':
                if formula(n[i:i+4]):
                    n = n[0:i] + 'P' + n[i+4:]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                    else:
                        i = 0
                else:
                    return 0
                print(n)
            elif n[i+4] == ')' and n[i+1] != '(':
                if formula(n[i:i+5]):
                    n = n[0:i] + 'P' + n[i+5:]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                    else:
                        i = 0
                else:
                    return 0
                print(n)
            else:
                pozlast.append(i)
                i += 1
        else:
            i += 1
        #print(i, pozlast)
    #print(n, i, pozlast)
    if formula(n):
        return 1
    else:
        return 0


def listadins(s):
    l = []
    for i in s:
        if i in ['=','>','!','/','&']:
            l.append([i])
        else:
            l.append(i)
    return l


def listadinp(n,l):
    for i in n:
        l.append(i)
    pozlast = []
    print(l)
    if len(l) == 1:
        l = listadins([l[0]])
    elif len(l) < 5:
        x = l[1:len(l) - 1]
        l = listadins(x)
    else:
        i = 0
        while i + 4 < len(l):
            if l[i] == '(':
                if l[i+3] == ')':
                    x = l[i+1:i+3]
                    l[i] = listadins(x)
                    del l[i+1:i+4]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                    else:
                        i = 0
                elif l[i+4] == ')' and l[i+1] != '(':
                    x = l[i+1:i+4]
                    l[i] = listadins(x)
                    del l[i+1:i+5]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                    else:
                        i = 0
                else:
                    pozlast.append(i)
                    i += 1
            else:
                i += 1
            print(l)
        else:
            if len(l) == 4:
                #print(l[1:len(l) - 1])
                l = listadins(l[1:len(l) - 1])
        if len(l) == 1:
            l = l[0]
    return l


def sintaxarelaxata(n):
    #print(n.count('('),n.count(')'))
    if n.count('(') != n.count(')'):
        return 0
    else:
        i = 0
        while i < len(n):
            if n[i] in '()':
                n = n[:i]+n[i+1:]
            else:
                i += 1
        print(n)
        i = 0
        while i < len(n) - 1:
            if n[i].isalpha() or n[i] in '01':
                if n[i+1].isalpha() or n[i] in '01!':
                    return 0
            elif n[i] == '!':
                if not n[i+1].isalpha() and n[i] not in '01':
                    return 0
            elif n[i] in '>/=&':
                if n[i+1].isalpha() or n[i+1] in '01':
                    return 1
                else:
                    return 0
            i = i + 1
    print()
    return 1


def valoare(n):
    if len(n) == 1:
        return n[0]
    else:
        if len(n) == 3:
            if n[1] == ['/']:
                if n[0] == 0 and n[2] == 0:
                    return 0
            elif n[1] == ['>']:
                if n[0] == 1 and n[2] == 0:
                    return 0
            elif n[1] == ['=']:
                if n[0] != n[2]:
                    return 0
            elif n[1] == ['&']:
                if n[0] != 1 or n[2] != 1:
                    return 0
            return 1
        elif len(n) == 2:
            if n[1] == 1:
                return 0
            else:
                return 1
                    

def valoareadevar(l, ip):
    print(l)
    if len(l) == 1:
        if isinstance(l[0], str):
            l[0] = ip[l[0]]
        else:
            l[0] = valoareadevar(l[0], ip)
        print(l)
        return valoare(l)
    elif len(l) == 2:
        if isinstance(l[1], str):
            l[1] = ip[l[1]]
        else:
            l[1] = valoareadevar(l[1], ip)
        print(l)
        return valoare(l)
    else:
        if isinstance(l[0], str):
            l[0] = ip[l[0]]
        else:
            l[0] = valoareadevar(l[0], ip)
        if isinstance(l[2], str):
            l[2] = ip[l[2]]
        else:
            l[2] = valoareadevar(l[2], ip)
        print(l)
        return valoare(l)


def valoareadevar2(n, ip):
    pozlast = []
    i = 0
    
    while i < len(n) - 1:
        #print(n, len(n), i, pozlast)
        if n[i] == '(':
            if n[i+3] == ')':
                if formula2(n[i+1:i+3]):
                    n = n[0:i] + inlocuire(n[i+1:i+3], ip) + n[i+4:]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                        del pozlast[0]
                    else:
                        i = 0
                else:
                    i += 1
            elif n[i+4] == ')' and n[i+1] != '(':
                if formula2(n[i+1:i+4]):
                    n = n[0:i] + inlocuire(n[i+1:i+4], ip) + n[i+5:]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                        del pozlast[0]
                    else:
                        i = 0
                else:
                    i += 1
            else:
                pozlast.append(i)
                i += 1
        elif n[i] == '!':
            if n[i+1] == '(':
                i += 1
            elif n[i-1] in "/&>=" and (n[i+1].isalpha() or n[i+1] == '1' or n[i+1] == '0'):
                if formula2(n[i:i+2]):
                    n = n[0:i] + inlocuire(n[i:i+2], ip) + n[i+2:]
                    if len(pozlast) > 1:
                        i = pozlast[-1]
                        del pozlast[-1]
                    elif len(pozlast) == 1:
                        i = pozlast[0]
                        del pozlast[0]
                    else:
                        i = 0
                else:
                    i += 1
            elif n[i+1] in '01' or n[i+1].isalpha():
                if n[i-1] == '(' and n[i+2] == ')':
                    if formula2(n[i:i+2]):
                        n = n[0:i-1] + inlocuire(n[i:i+2], ip) + n[i+3:]
                        if len(pozlast) > 1:
                            i = pozlast[-1]
                            del pozlast[-1]
                        elif len(pozlast) == 1:
                            i = pozlast[0]
                            del pozlast[0]
                        else:
                            i = 0
                    else:
                        i += 1
                else:
                    if formula2(n[i:i+2]):
                        n = n[0:i] + inlocuire(n[i:i+2], ip) + n[i+2:]
                        if len(pozlast) > 1:
                            i = pozlast[-1]
                            del pozlast[-1]
                        elif len(pozlast) == 1:
                            i = pozlast[0]
                            del pozlast[0]
                        else:
                            i = 0
                    else:
                        i += 1
            else:
                if i not in pozlast:
                    pozlast.append(i)
                i += 1      
        elif n[i] == '1' or n[i] == '0' and n[i+1] in ">/&=" and (n[i+2]=='1' or n[i+2] == '0' or n[i+2].isalpha()):
            if formula2(n[i:i+3]):
                n = n[0:i] + inlocuire(n[i:i+3], ip) + n[i+3:]
                if len(pozlast) > 1:
                    i = pozlast[-1]
                    del pozlast[-1]
                elif len(pozlast) == 1:
                    i = pozlast[0]
                    del pozlast[0]
                else:
                    i = 0
            else:
                i += 1
        else:
            i += 1
        print(n)
        
    if len(n) >= 5:
        return valoareadevar2(n, ip)
    return inlocuire(n, ip)


def inlocuire(n, ip):
    if len(n) == 1:
        if n.isalpha():
            return str(ip[n])
        else:
            return str(n)
    elif len(n) == 2:
        if n[1].isalpha():
            if ip[n[1]] == 1:
                return '0'
            else:
                return '1'
        else:
            if n[1] == '1':
                return '0'
            else:
                return '1'
    elif len(n) == 3:
        if n[1] == '/':
            if n[0].isalpha():
                if n[2].isalpha():
                    if ip[n[0]] == 0 and ip[n[2]] == 0:
                        return '0'
                else:
                    if ip[n[0]] == 0 and n[2] == '0':
                        return '0'
            else:
                if n[2].isalpha():
                    if n[0] == '0' and ip[n[2]] == 0:
                        return '0'
                else:
                    if n[0] == '0' and n[2] == '0':
                        return '0'
        elif n[1] == '>':
            if n[0].isalpha():
                if n[2].isalpha():
                    if ip[n[0]] == 1 and ip[n[2]] != 1:
                        return '0'
                else:
                    if ip[n[0]] == 1 and n[2] != '1':
                        return '0'
            else:
                if n[2].isalpha():
                    if n[0] == '1' and ip[n[2]] != 1:
                        return '0'
                else:
                    if n[0] == '1' and n[2] != '1':
                        return '0'
        elif n[1] == '=':
            if n[0].isalpha():
                if n[2].isalpha():
                    if ip[n[0]] != ip[n[2]]:
                        return '0'
                else:
                    if ip[n[0]] != int(n[2]):
                        return '0'
            else:
                if n[2].isalpha():
                    if int(n[0]) != ip[n[2]]:
                        return '0'
                else:
                    if int(n[0]) != int(n[2]):
                        return '0'
        elif n[1] == '&':
            if n[0].isalpha():
                if n[2].isalpha():
                    if ip[n[0]] != 1 or ip[n[2]] != 1:
                        return '0'
                else:
                    if ip[n[0]] != 1 or n[2] != '1':
                        return '0'
            else:
                if n[2].isalpha():
                    if n[0] != '1' or ip[n[2]] != 1:
                        return '0'
                else:
                    if n[0] != '1' or n[2] != '1':
                        return '0'
        return '1'


def formula2(s):
    if len(s) == 1:
        if s.isalpha() or s == '1':
            return '1'
    else:
        if len(s) == 3:
            if s[0].isalpha() or s[0] == '1' or s[0] == '0':
                if s[1] in ['=','>','/','&']:
                    if s[2].isalpha() or s[2] == '1' or s[2] == '0':
                        return 1
        else:
            if s[0] == '!':
                if s[1].isalpha() or s[1] == '1' or s[1] == '0':
                    return 1
    return 0


def transfrelnorm(n, d):
    lnot = []
    nrnot = 0
    for j in range(0, len(n)):
        if n[j] == '!':
            if n[j-1] == '(':
                if n[j+1].isalpha():
                    if n[j+2] != ")":
                        lnot.append(nrnot)             
            else:
                lnot.append(nrnot)

            nrnot += 1
    
    #print(lnot)
    
    k = n.count('!')
    c = 0
    i = n.find('!')
    while c < k:
        #print(c)
        if c not in lnot:
            c += 1
            i = n.find('!', i+1)
            continue
        else:
            y = i + 1
            pd = 0
            pi = 0
            schimbay = "da"
            while y < len(n):
                if n[y] == ')':
                    pi += 1
                    if pi == pd:
                        break
                elif n[y] == '(':
                    pd += 1
                elif n[y] in ">/&=":
                    if pi == pd:
                        y -= 1
                        break
                elif n[y] in d.keys():
                    if pd == pi:
                        break
                y += 1
            
            #print(i, y, schimbay, n[i: y + 1])
            if y == len(n) - 1:
                if schimbay == 'da':
                    n = n[0:i] + '(' + n[i:] + ')'
                    i = n.find('!', i+2)
                else:
                    i = n.find('!', i+1)
            else:
                if schimbay == 'da':
                    n = n[0:i] + '(' + n[i:y + 1] + ')' + n[y + 1:]
                    i = n.find('!', i+2)
                else:
                    i = n.find('!', i+1)
            c += 1
            print(n, '     !')
    
    k = n.count('&')
    c = 0
    i = n.find('&')
    while c < k:
        x = i
        y = i
        pd = 0
        pi = 0
        schimbax = "da"
        schimbay = "da"
        diffs = 0
        diffd = 0
        while x > 0:
            x -= 1
            if n[x] == '(':
                pd += 1
                if pd > pi:
                    schimbax = "nu"
                    break
            elif n[x] == ')':
                pi += 1
            elif n[x] in d.keys() and n[x-1] != '(':
                if pd == pi:
                    schimbax = "da"
                    break
            elif n[x] in '>/=&':
                if pd == pi:
                    x += 1
                    schimbax = "da"
                    break
        
        diffs = pd - pi
        pd = 0
        pi = 0
        if diffs == 0:
            schimbax = "da"
        while y < len(n) - 1:
            y += 1
            if n[y] == '(':
                pd += 1
            elif n[y] == ')':
                pi += 1
                if pi > pd:
                    schimbay = "nu"
                    break
            elif n[y] in d.keys():
                if y < len(n) - 1:
                    if n[y+1] != ')':
                        if pd == pi:
                            schimbay = "da"
                            break
                else:
                    schimbay = "da"
            elif n[y] in '>/=&':
                if pi == pd:
                    y -= 1
                    schimbay = "da"
                    break
        diffd = pi - pd
        if diffd == 0:
            schimbay = "da"

        
        #print(x, y, schimbax, schimbay)

        if y == len(n) - 1:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:] + ')'
                i = n.find('&', i+2)
            else:
                i = n.find('&', i+1)
        else:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:y + 1] + ')' + n[y + 1:]
                i = n.find('&', i+2)
            else:
                i = n.find('&', i+1)
        c += 1
        print(n, '     &')
    
    k = n.count('/')
    c = 0
    i = n.find('/')
    while c < k:
        x = i
        y = i
        pd = 0
        pi = 0
        schimbax = "da"
        schimbay = "da"
        diffs = 0
        diffd = 0
        while x > 0:
            x -= 1
            if n[x] == '(':
                pd += 1
                if pd > pi:
                    schimbax = "nu"
                    break
            elif n[x] == ')':
                pi += 1
            elif n[x] in d.keys() and n[x-1] != '(':
                if pd == pi:
                    schimbax = "da"
                    break
            elif n[x] in '>/=&!':
                if pd == pi:
                    x += 1
                    schimbax = "da"
                    break
        
        diffs = pd - pi
        pd = 0
        pi = 0
        if diffs == 0:
            schimbax = "da"
        while y < len(n) - 1:
            y += 1
            if n[y] == '(':
                pd += 1
            elif n[y] == ')':
                pi += 1
                if pi > pd:
                    schimbay = "nu"
                    break
            elif n[y] in d.keys():
                if y < len(n) - 1:
                    if n[y+1] != ')':
                        if pd == pi:
                            schimbay = "da"
                            break
                else:
                    schimbay = "da"
            elif n[y] in '>/=&':
                if pi == pd:
                    y -= 1
                    schimbay = "da"
                    break
        diffd = pi - pd
        if diffd == 0:
            schimbay = "da"
        
        #print(x, y, schimbax, schimbay, notps, notpd)
        if y == len(n) - 1:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:] + ')'
                i = n.find('/', i+2)
            else:
                i = n.find('/', i+1)
        else:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:y + 1] + ')' + n[y + 1:]
                i = n.find('/', i+2)
            else:
                i = n.find('/', i+1)
        c += 1
        print(n, '     /')


    k = n.count('>')
    c = 0
    i = n.find('>')
    while c < k:
        x = i
        y = i
        pd = 0
        pi = 0
        schimbax = "da"
        schimbay = "da"
        diffs = 0
        diffd = 0
        while x > 0:
            x -= 1
            if n[x] == '(':
                pd += 1
                if pd > pi:
                    schimbax = "nu"
                    break
            elif n[x] == ')':
                pi += 1
            elif n[x] in d.keys() and n[x-1] != '(':
                if pd == pi:
                    schimbax = "da"
                    break
            elif n[x] in '>/=&':
                if pd == pi:
                    x += 1
                    schimbax = "da"
                    break
        
        diffs = pd - pi
        pd = 0
        pi = 0
        if diffs == 0:
            schimbax = "da"
        while y < len(n) - 1:
            y += 1
            if n[y] == '(':
                pd += 1
            elif n[y] == ')':
                pi += 1
                if pi > pd:
                    schimbay = "nu"
                    break
            elif n[y] in d.keys():
                if y < len(n) - 1:
                    if n[y+1] != ')':
                        if pd == pi:
                            schimbay = "da"
                            break
                else:
                    schimbay = "da"
            elif n[y] in '>/=&':
                if pi == pd:
                    y -= 1
                    schimbay = "da"
                    break
        diffd = pi - pd
        if diffd == 0:
            schimbay = "da"

        if y == len(n) - 1:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:] + ')'
                i = n.find('>', i+2)
            else:
                i = n.find('>', i+1)
        else:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:y + 1] + ')' + n[y + 1:]
                i = n.find('>', i+2)
            else:
                i = n.find('>', i+1)
        c += 1
        print(n, '     >')

    k = n.count('=')
    c = 0
    i = n.find('=')
    while c < k:
        x = i
        y = i
        pd = 0
        pi = 0
        schimbax = "da"
        schimbay = "da"
        diffs = 0
        diffd = 0
        while x > 0:
            x -= 1
            if n[x] == '(':
                pd += 1
                if pd > pi:
                    schimbax = "nu"
                    break
            elif n[x] == ')':
                pi += 1
            elif n[x] in d.keys() and n[x-1] != '(':
                if pd == pi:
                    schimbax = "da"
                    break
            elif n[x] in '>/=&':
                if pd == pi:
                    x += 1
                    schimbax = "da"
                    break
        
        diffs = pd - pi
        pd = 0
        pi = 0
        if diffs == 0:
            schimbax = "da"
        while y < len(n) - 1:
            y += 1
            if n[y] == '(':
                pd += 1
            elif n[y] == ')':
                pi += 1
                if pi > pd:
                    schimbay = "nu"
                    break
            elif n[y] in d.keys():
                if y < len(n) - 1:
                    if n[y+1] != ')':
                        if pd == pi:
                            schimbay = "da"
                            break
                else:
                    schimbay = "da"
            elif n[y] in '>/=&':
                if pi == pd:
                    y -= 1
                    schimbay = "da"
                    break
        diffd = pi - pd
        if diffd == 0:
            schimbay = "da"

        if y == len(n) - 1:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:] + ')'
                i = n.find('=', i+2)
            else:
                i = n.find('=', i+1)
        else:
            if schimbax == "da" or schimbay == 'da':
                n = n[0:x] + '(' + n[x:y + 1] + ')' + n[y + 1:]
                i = n.find('=', i+2)
            else:
                i = n.find('=', i+1)
        c += 1
        print(n, '     =')
    
    return n
