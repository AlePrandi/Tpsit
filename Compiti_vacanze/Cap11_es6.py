def leggi_parole_in_dizionario(file_name):
    dizionario = {}
    with open(file_name, 'r') as f:
        for linea in f:
            parola = linea.strip()
            dizionario[parola] = None
    return dizionario

def read_dictionary(filename='c06d'):
    pronunce = {}
    with open(filename, 'r') as f:
        for linea in f:
            parola, pronuncia = linea.split(maxsplit=1)
            pronunce[parola.lower()] = pronuncia.strip()
    return pronunce

def trova_parola_omofona(dizionario_parole, dizionario_pronunce):
    for parola in dizionario_parole:
        if len(parola) == 5:
            prima_parola = parola[1:]
            seconda_parola = parola[0] + parola[2:]
            if prima_parola in dizionario_pronunce and seconda_parola in dizionario_pronunce:
                if (dizionario_pronunce[prima_parola] == dizionario_pronunce[parola] and 
                    dizionario_pronunce[seconda_parola] == dizionario_pronunce[parola]):
                    return parola
    return None

def main():
    dizionario_parole = leggi_parole_in_dizionario('words.txt')
    dizionario_pronunce = read_dictionary('pronounce.txt')
    parola = trova_parola_omofona(dizionario_parole, dizionario_pronunce)
    if parola:
        print(f"La parola che risolve il quesito è: {parola}")
    else:
        print("Nessuna parola trovata.")

if __name__ == "__main__":
    main()
