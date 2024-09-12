def trova_bifronte(lista_parole):
    bifronti = []
    insieme_parole = set(lista_parole)
    for parola in lista_parole:
        if parola[::-1] in insieme_parole:
            bifronti.append((parola, parola[::-1]))
    return bifronti

def main():
    parole = ['stressed', 'desserts', 'gat', 'tag']
    print(trova_bifronte(parole)) 

if __name__ == "__main__":
    main()
