def sottrai(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    
    diff = set1 - set2
    
    res = {chiave: None for chiave in diff}
    return res

def main():
    d1 = {'parola1': 5, 'parola2': 2, 'parola3': 7, 'parola4': 1}
    d2 = {'parola2': 3, 'parola4': 4, 'parola5': 9}
    
    risultato1 = sottrai(d1, d2)
    risultato2 = sottrai(d2, d1)
    
    print("Parole in d1 ma non in d2:", risultato1)
    print("Parole in d2 ma non in d1:", risultato2)

if __name__ == '__main__':
    main()
