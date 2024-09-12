def somma_nidificata(liste_nidificate):
    somma_totale = 0
    for sotto_lista in liste_nidificate:
        somma_totale += sum(sotto_lista)
    return somma_totale

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(somma_nidificata(t))  # Output: 21

if __name__ == "__main__":
    main()