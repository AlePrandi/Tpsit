def ackermann(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackermann(m - 1, 1, memo)
    elif m > 0 and n > 0:
        result = ackermann(m - 1, ackermann(m, n - 1, memo), memo)
    memo[(m, n)] = result
    return result

def main():
    print(f"Ackermann(3, 4): {ackermann(3, 4)}")

if __name__ == "__main__":
    main()
