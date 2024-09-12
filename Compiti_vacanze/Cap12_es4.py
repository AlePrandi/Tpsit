def figli(parola, parole_set):
    return [parola[:i] + parola[i+1:] for i in range(len(parola)) if parola[:i] + parola[i+1:] in parole_set]

def riducibile(parola, parole_set, memo):
    if parola in memo:
        return memo[parola]
    
    for figlia in figli(parola, parole_set):
        if riducibile(figlia, parole_set, memo):
            memo[parola] = True
            return True
    
    memo[parola] = False
    return False

def parola_riducibile(file):
    with open(file, 'r') as f:
        parole = f.read().split()
    
    parole_set = set(parole)
    memo = {'': True, 'a': True, 'i': True}
    
    riducibili = []
    for parola in parole:
        if riducibile(parola, parole_set, memo):
            riducibili.append(parola)
    
    riducibili.sort(key=len, reverse=True)
    print(riducibili[0], len(riducibili[0]))

def main():
    parola_riducibile('words.txt')

if __name__ == "__main__":
    main()
