def palindromo(parola):
    '''
    controllo se la parola è palindroma
    '''
    return True if parola == parola[::-1] else False


def main():

    parola = "banana"
    print(parola[0:5:2])
    # parola al contrario
    print(parola[::-1])

    if palindromo(parola):
        print(f"La parola {parola} è palindroma")
    else:
        print(f"La parola {parola} non è palindroma")


if __name__ == '__main__':
    main()
