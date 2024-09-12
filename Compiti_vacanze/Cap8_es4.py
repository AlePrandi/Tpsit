#se la prima lettera è minuscola ritorna True
def una_minuscola1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#se la lettera 'c' nell'if è minuscola ritorna True in stringa
def una_minuscola2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#ritorna quale lettera è minuscola
def una_minuscola3(s):
    for c in s:
        flag = c.islower()
    return flag

#se c'è almeno una minuscola ritorna True
def una_minuscola4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#se non tutte le lettere sono minuscole ritorna False
def una_minuscola5(s):
    for c in s:
        if not c.islower():
            return False
    return True
