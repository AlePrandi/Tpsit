def inverti_diz(dizionario):
    invertito = {}
    for chiave, valore in dizionario.items():
        invertito.setdefault(valore, []).append(chiave)
    return invertito

def main():
    dizionario = {'a': 1, 'b': 2, 'c': 1}
    print(f"Dizionario invertito: {inverti_diz(dizionario)}")

if __name__ == "__main__":
    main()
