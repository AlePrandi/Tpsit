def ordinata(lista):
    return lista == sorted(lista)

def main():
    print(ordinata([1, 2, 2])) 
    print(ordinata(['b', 'a']))

if __name__ == "__main__":
    main()
