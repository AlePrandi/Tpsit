def tronca(lista):
    del lista[0]
    del lista[-1]
    return None

def main():
    t = [1, 2, 3, 4]
    tronca(t)
    print(t)  

if __name__ == "__main__":
    main()
