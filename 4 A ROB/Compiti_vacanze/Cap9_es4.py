def usa_solo(parola, lettere):

    for lettera in parola:
        if lettera not in lettere:
            return False
    return True

def main():

    lettere_consentite = "acefhlo"
    
    parole = ["each", "leaf", "of", "a", "loaf", "hoe", "alfalfa", "hello", "coffee"]

    parole_valide = [parola for parola in parole if usa_solo(parola, lettere_consentite)]

    print("Parole che utilizzano solo le lettere consentite:")
    for parola in parole_valide:
        print(parola)

    frase = "Each leaf of a loaf"
    #all si usa per vedere se tutte le iterazioni restituisco True
    if all(usa_solo(parola, lettere_consentite) for parola in frase.split()):
        print(f"Frase valida: {frase}")
    else:
        print(f"Frase non valida: {frase}")

if __name__ == "__main__":
    main()
