def main():
    with open("words.txt", "r") as file:
        for riga in file:
            parole = riga.split(" ")
            for parola in parole:
                if len(parola) > 20:
                    print(parola)
                    
if __name__ == "__main__":
    main()