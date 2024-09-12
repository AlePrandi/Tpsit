def trova_anagrammi(file):
    with open(file, 'r') as f:
        parole = f.read().split()
    
    anagrammi = {}
    
    for parola in parole:
        chiave = ''.join(sorted(parola))
        if chiave not in anagrammi:
            anagrammi[chiave] = [parola]
        else:
            anagrammi[chiave].append(parola)
    
    for gruppo in anagrammi.values():
        if len(gruppo) > 1:
            print(gruppo)
            
def anagrammi_lung(file):
    with open(file, 'r') as f:
        parole = f.read().split()
    
    anagrammi = {}
    
    for parola in parole:
        chiave = ''.join(sorted(parola))
        if chiave not in anagrammi:
            anagrammi[chiave] = [parola]
        else:
            anagrammi[chiave].append(parola)
    
    anagrammi_ordinati = sorted(anagrammi.values(), key=lambda x: len(x), reverse=True)
    
    for gruppo in anagrammi_ordinati:
        if len(gruppo) > 1:
            print(gruppo)
            
def comb_scarabeo(file):
    
    with open(file, 'r') as f:
        parole = f.read().split()
    
    anagrammi = {}
    
    for parola in parole:
        chiave = ''.join(sorted(parola))
        if chiave not in anagrammi:
            anagrammi[chiave] = [parola]
        else:
            anagrammi[chiave].append(parola)
    
    max_combinazioni = []
    
    for chiave, gruppo in anagrammi.items():
        if len(chiave) == 8 and len(gruppo) > len(max_combinazioni):
            max_combinazioni = gruppo
    
    print(max_combinazioni)

def main():
    comb_scarabeo('words.txt')

if __name__ == "__main__":
    main()
