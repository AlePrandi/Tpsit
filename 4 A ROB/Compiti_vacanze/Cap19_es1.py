def coeff_binomiale(n, k, memo=None):

    if memo is None:
        memo = {}

    if (n, k) in memo:
        return memo[(n, k)]

    if k == 0 or k == n:
        result = 1
    elif k > n:
        result = 0
    else:
        result = coeff_binomiale(n-1, k, memo) + coeff_binomiale(n-1, k-1, memo)

    memo[(n, k)] = result
    return result

def main():
    
    n = 5
    k = 2
    risultato = coeff_binomiale(n, k)
    print(f"Il coefficiente binomiale di {n} sopra {k} è {risultato}")

if __name__ == "__main__":
    main()
