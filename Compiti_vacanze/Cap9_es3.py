def evita(parola, lettere_vietate):
    for lettera in parola:
        if lettera in lettere_vietate:
            return False
    return True

def main():
    
    lettere_vietate = input("Inserisci una stringa di lettere vietate: ").strip()
    
    parole = ["ciao", "mondo", "python", "programmazione", "esempio", "test", "funzione", "escludere"]
    
    conteggio = 0
    for parola in parole:
        if evita(parola, lettere_vietate):
            conteggio += 1
    
    print(f"Numero di parole che non contengono nessuna delle lettere vietate: {conteggio}")

if __name__ == "__main__":
    main()
