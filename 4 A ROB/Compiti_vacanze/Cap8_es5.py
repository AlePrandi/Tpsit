def ruota_parola(parola, n):
    risultato = []
    
    for char in parola:
        if 'a' <= char <= 'z':
            nuovo_carattere = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            risultato.append(nuovo_carattere)
        elif 'A' <= char <= 'Z':
            nuovo_carattere = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            risultato.append(nuovo_carattere)
        else:
            risultato.append(char)
    
    return ''.join(risultato)

def main():
    parola = "ciao"
    print(ruota_parola(parola, 4))
    
if __name__ == "__main__":
    main()