import math
def eval_ciclo():
    while True:
        dato = input("Inserisci una funzione numerica oppure 'fatto' per uscire: ")
        if dato != "fatto":
            print(f"risultato: {eval(dato)}")
        else:
            break
        
def main():
    eval_ciclo()
    
if __name__ == '__main__':
    main()