import random
import string

def pulisci_parola(parola):
    rimuovibili = string.punctuation + string.whitespace + string.digits
    parola = parola.strip(rimuovibili).lower()
    return parola

def elabora_libro(percorso_file):
    diz_parole = {}
    inizio = False

    with open(percorso_file, 'r', encoding='utf-8') as file:
        for riga in file:
            if '*** START OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***' in riga:
                inizio = True
                continue
            if '*** END OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***' in riga:
                break

            if inizio:
                parole = riga.split()
                parole_pulite = [pulisci_parola(parola) for parola in parole]
                for i in range(len(parole_pulite) - 1):
                    parola = parole_pulite[i]
                    parola_successiva = parole_pulite[i + 1]
                    if parola:
                        if parola in diz_parole:
                            diz_parole[parola].append(parola_successiva)
                        else:
                            diz_parole[parola] = [parola_successiva]

    return diz_parole

def frase_random(dizionario, lunghezza_prefisso=3, lunghezza_testo=50):
    descrizione = []
    lista_parole = [parola for parola in dizionario.keys() if len(parola) == lunghezza_prefisso]
    
    if not lista_parole:
        print("Nessuna parola con la lunghezza del prefisso specificato.")
        return
    
    prima = random.choice(lista_parole)
    descrizione.append(prima)
    
    for _ in range(lunghezza_testo - 1):
        if prima in dizionario:
            sequenza = dizionario[prima]
            if sequenza:
                prossima = random.choice(sequenza)
                descrizione.append(prossima)
                prima = prossima
            else:
                break
        else:
            break

    print(' '.join(descrizione))

def main():
    percorso_file = './Odissea_gutenberg.txt'
    diz_parole = elabora_libro(percorso_file)
    frase_random(diz_parole)

if __name__ == "__main__":
    main()
