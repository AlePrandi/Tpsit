def crea_lista_con_append(file_name):
    lista = []
    with open(file_name, 'r') as f:
        for linea in f:
            parola = linea.strip()
            lista.append(parola)
    return lista

def crea_lista_con_concat(file_name):
    lista = []
    with open(file_name, 'r') as f:
        for linea in f:
            parola = linea.strip()
            lista = lista + [parola]
    return lista

def main():
    lista1 = crea_lista_con_append('words.txt')
    lista2 = crea_lista_con_concat('words.txt')
    print(f"Lista creata con append: {lista1}")
    print(f"Lista creata con concatenazione: {lista2}")

if __name__ == "__main__":
    main()
