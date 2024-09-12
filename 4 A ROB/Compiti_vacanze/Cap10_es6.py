def anagramma(parola1, parola2):
    return sorted(parola1) == sorted(parola2)

def main():
    print(anagramma('listen', 'silent')) 
    print(anagramma('hello', 'world')) 

if __name__ == "__main__":
    main()
