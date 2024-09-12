def ha_duplicati(lista):
    dizionario = {}
    for elemento in lista:
        if elemento in dizionario:
            return True
        dizionario[elemento] = None
    return False

def main():
    lista = [1, 2, 3, 4, 1]
    if ha_duplicati(lista):
        print("La lista ha duplicati.")
    else:
        print("La lista non ha duplicati.")

if __name__ == "__main__":
    main()
