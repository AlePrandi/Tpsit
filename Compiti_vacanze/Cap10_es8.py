import random

def stima_probabilità_compleanno(numero_studenti, campioni):
    successi = 0
    for _ in range(campioni):
        compleanni = [random.randint(1, 365) for _ in range(numero_studenti)]
        if len(compleanni) != len(set(compleanni)):
            successi += 1
    return successi / campioni

def main():
    probabilità = stima_probabilità_compleanno(23, 10000)
    print(probabilità)

if __name__ == "__main__":
    main()
