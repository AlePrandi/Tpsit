def parole_incastrate(lista_parole):
    incastrate = []
    set_parole = set(lista_parole)
    for parola1 in lista_parole:
        for parola2 in lista_parole:
            incastro = ''.join(a + b for a, b in zip(parola1, parola2))
            if incastro in set_parole:
                incastrate.append((parola1, parola2, incastro))
    return incastrate

def main():
    parole = ['shoe', 'cold', 'schooled']
    print(parole_incastrate(parole)) 

if __name__ == "__main__":
    main()
