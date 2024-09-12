def usa_tutte(parola, lettere_richieste):
    for lettera in lettere_richieste:
        if lettera not in parola:
            return False
    return True

def conta_parole_con_vocali(parole, vocali):

    conteggio = 0
    for parola in parole:
        if usa_tutte(parola, vocali):
            conteggio += 1
    return conteggio

def main():
    parole = ["education", "sequoia", "facetious", "abstemious", "automobile", "questionably", "unquestionably", "house", "rhythm", "syzygy"]
    
    vocali_aeiou = "aeiou"
    parole_con_aeiou = conta_parole_con_vocali(parole, vocali_aeiou)
    print(f"Numero di parole che contengono tutte le vocali '{vocali_aeiou}': {parole_con_aeiou}")

    vocali_aeiouy = "aeiouy"
    parole_con_aeiouy = conta_parole_con_vocali(parole, vocali_aeiouy)
    print(f"Numero di parole che contengono tutte le vocali '{vocali_aeiouy}': {parole_con_aeiouy}")

if __name__ == "__main__":
    main()
