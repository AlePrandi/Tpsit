def leggi_parole_in_dizionario(file_name):
    dizionario = {}
    with open(file_name, 'r') as f:
        for linea in f:
            parola = linea.strip()
            dizionario[parola] = None
    return dizionario

def main():
    dizionario = leggi_parole_in_dizionario('words.txt')
    parola = "test"
    if parola in dizionario:
        print(f"La parola '{parola}' è nel dizionario.")
    else:
        print(f"La parola '{parola}' non è nel dizionario.")

if __name__ == "__main__":
    main()
