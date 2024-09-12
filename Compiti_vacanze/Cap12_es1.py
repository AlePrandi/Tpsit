def piu_frequente(stringa):

    frequenza = {}
    
    for char in stringa.lower():
        if char.isalpha(): 
            if char in frequenza:
                frequenza[char] += 1
            else:
                frequenza[char] = 1
    
    lettere_ordinate = list(frequenza.items())

    for i in range(len(lettere_ordinate)):
        for j in range(i + 1, len(lettere_ordinate)):
            if lettere_ordinate[i][1] < lettere_ordinate[j][1]:
                lettere_ordinate[i], lettere_ordinate[j] = lettere_ordinate[j], lettere_ordinate[i]

    for lettera, freq in lettere_ordinate:
        print(f"{lettera}: {freq}")

def main():
  
    frase = "dbvajsbvoaurovbsbdjvbasu"
    piu_frequente(frase)

if __name__ == "__main__":
    main()
