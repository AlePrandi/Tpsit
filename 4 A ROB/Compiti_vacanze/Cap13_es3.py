import string

def pulisci_parola(parola):
    rimuovibili = string.punctuation + string.whitespace
    parola = parola.strip(rimuovibili).lower()
    return parola

def processa_libro(percorso_file):
    conteggio_parole = {}
    inizia = False

    with open(percorso_file, 'r', encoding='utf-8') as file:
        for riga in file:
            if '*** START OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***' in riga:
                inizia = True
                continue
            if '*** END OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***' in riga:
                break

            if inizia:
                parole = riga.split()
                for parola in parole:
                    parola_pulita = pulisci_parola(parola)
                    if parola_pulita:
                        conteggio_parole[parola_pulita] = conteggio_parole.get(parola_pulita, 0) + 1

    return conteggio_parole

def mostra_top_20_parole(conteggio_parole):
    parole_ordinate = sorted(conteggio_parole.items(), key=lambda x: x[1], reverse=True)
    print("Le 20 parole più usate:")
    for parola, conteggio in parole_ordinate[:20]:
        print(f"{parola}: {conteggio}")

def main():
    percorso_file = "Odissea_gutenberg.txt"
    conteggio_parole = processa_libro(percorso_file)
    mostra_top_20_parole(conteggio_parole)

if __name__ == "__main__":
    main()
