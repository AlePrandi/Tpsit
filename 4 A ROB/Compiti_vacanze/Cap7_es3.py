import math


def stima_pi():
    k = 0
    somma = 0
    fattore = (2 * math.sqrt(2)) / 9801

    while True:
        numeratore = math.factorial(4 * k) * (1103 + 26390 * k)
        denominatore = math.pow(math.factorial(k),4) * math.pow(396, (4 * k))
        termine = fattore * (numeratore / denominatore)

        if termine < 1e-15:
            break

        somma += termine
        k += 1

    pi_stima = 1 / somma
    return pi_stima


def main():
    pi_calcolato = stima_pi()
    print(f"Stima di π: {pi_calcolato}")
    print(f"Valore di math.pi: {math.pi}")
    print(f"Differenza: {abs(pi_calcolato - math.pi)}")


if __name__ == "__main__":
    main()
