def alfabetica(parola):
    alfa = True
    
    for k,c in enumerate(parola[:-1]):
        if c <= parola[k + 1] and alfa is True:
            alfa = True
        else:
            alfa = False
            
    return alfa

def main():
    print(alfabetica("abcdde"))
    
if __name__ == "__main__":
    main()