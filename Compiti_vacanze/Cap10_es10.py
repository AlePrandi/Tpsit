def bisezione(lista, valore):
    inizio, fine = 0, len(lista) - 1
    while inizio <= fine:
        medio = (inizio + fine) // 2
        if lista[medio] == valore:
            return True
        elif lista[medio] < valore:
            inizio = medio + 1
        else:
            fine = medio - 1
    return False

def main():
    parole = ['apple', 'banana', 'cherry', 'date']
    print(bisezione(parole, 'banana'))  
    print(bisezione(parole, 'fig')) 

if __name__ == "__main__":
    main()
