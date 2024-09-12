def leggi_parole_in_dizionario(file_name):
    dizionario = {}
    with open(file_name, 'r') as f:
        for linea in f:
            parola = linea.strip()
            dizionario[parola] = None
    return dizionario

def ruota_parola(parola, n):
    return parola[n:] + parola[:n]

def trova_coppie_ruotabili(file_name):
    dizionario = leggi_parole_in_dizionario(file_name)
    coppie = []
    for parola in dizionario:
        for i in range(1, len(parola)):
            parola_ruotata = ruota_parola(parola, i)
            if parola_ruotata in dizionario:
                coppie.append((parola, parola_ruotata))
    return coppie

def main():
    coppie = trova_coppie_ruotabili('words.txt')
    print(f"Coppie ruotabili trovate: {coppie}")

if __name__ == "__main__":
    main()
