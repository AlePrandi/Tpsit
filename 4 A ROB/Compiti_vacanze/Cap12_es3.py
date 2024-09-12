def trova_metatesi(file):
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
            for i in range(len(gruppo)):
                for j in range(i + 1, len(gruppo)):
                    if sorted(gruppo[i]) == sorted(gruppo[j]) and gruppo[i] != gruppo[j]:
                        differenze = sum(1 for a, b in zip(gruppo[i], gruppo[j]) if a != b)
                        if differenze == 2:
                            print(gruppo[i], gruppo[j])

def main():
    trova_metatesi('words.txt')

if __name__ == "__main__":
    main()
