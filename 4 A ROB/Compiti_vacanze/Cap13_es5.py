import random

def istogramma(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def estrai_da_isto(isto):
    lista_pesata = []
    for chiave, frequenza in isto.items():
        lista_pesata.extend([chiave] * frequenza)
    
    return random.choice(lista_pesata)

def main():
    t = ['a', 'a', 'b', 'c', 'd', 'c']
    isto = istogramma(t)
    print(isto)

    risultato = estrai_da_isto(isto)
    print(f"Valore estratto: {risultato}")

if __name__ == "__main__":
    main()
