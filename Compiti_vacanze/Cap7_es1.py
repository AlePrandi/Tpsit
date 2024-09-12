import math
def mia_radq(a):
    epsilon = 0.00000001
    x = a
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
        
    return y

def test_radq():
    print("a \t mia_radq(a) \t math.sqrt(a) \t diff")
    print("- \t ----------- \t ------------ \t ----")
    for a in range(1,10):
        print(f"{a} \t {mia_radq(a)} \t {math.sqrt(a)} \t {abs(mia_radq(a)-math.sqrt(a))}")

def main():
    test_radq()


if __name__ == '__main__':
    main()
