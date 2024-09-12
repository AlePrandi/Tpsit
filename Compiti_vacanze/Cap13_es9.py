import math
import matplotlib.pyplot as plt
import numpy as np
import string

def pulisci_parola(parola):
    rimuovibili = string.punctuation + string.whitespace
    parola = parola.strip(rimuovibili).lower()
    return parola

def conta_frequenze(percorso_file):
    frequenze = {}

    with open(percorso_file, 'r', encoding='utf-8') as file:
        for riga in file:
            parole = riga.split()
            parole_pulite = [pulisci_parola(parola) for parola in parole]
            for parola in parole_pulite:
                if parola:
                    if parola in frequenze:
                        frequenze[parola] += 1
                    else:
                        frequenze[parola] = 1
    
    return frequenze

def calcola_log_rango_frequenza(frequenze):
    frequenze_ordinate = sorted(frequenze.items(), key=lambda x: x[1], reverse=True)
    
    dati_log = []
    for rango, (parola, frequenza) in enumerate(frequenze_ordinate, start=1):
        log_rango = math.log10(rango)
        log_frequenza = math.log10(frequenza)
        dati_log.append((log_rango, log_frequenza))
    
    return dati_log

def traccia_grafico(dati_log):

    log_ranghi, log_frequenze = zip(*dati_log)

    plt.figure(figsize=(10, 6))
    plt.scatter(log_ranghi, log_frequenze, label='Dati')
    plt.xlabel('Log(Rango)')
    plt.ylabel('Log(Frequenza)')
    plt.title('Legge di Zipf')
    
    coefficiente_angular, intercetta = np.polyfit(log_ranghi, log_frequenze, 1)
    plt.plot(log_ranghi, np.polyval([coefficiente_angular, intercetta], log_ranghi), color='red', label=f'Fit Lineare (s ≈ {-coefficiente_angular:.2f})')

    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    percorso_file = "Odissea_gutenberg.txt"
    frequenze = conta_frequenze(percorso_file)
    dati_log = calcola_log_rango_frequenza(frequenze)
    traccia_grafico(dati_log)

if __name__ == "__main__":
    main()
