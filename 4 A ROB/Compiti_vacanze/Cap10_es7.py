def ha_duplicati(lista):
    return len(lista) != len(set(lista))

def main():
    print(ha_duplicati([1, 2, 3, 4])) 
    print(ha_duplicati([1, 2, 3, 3])) 

if __name__ == "__main__":
    main()
