import socket
import datetime
import numpy as np

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
TEMPO_INVIO = 15


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(SERVER_ADDRESS)
        id = 1 #input("Inserisci l'id della stazione: ")
        sirena = "off"
        while True:
            tempo = str(datetime.datetime.now()).split(" ") #converto in stringa e separo data e ora
            tempo = tempo[1].replace(":", "") #unisco le cifre
            valore_fiume = np.random.randint(1, 13)
            stringa_val = f"{id}|{valore_fiume}|{tempo}"
            s.sendall(stringa_val.encode())
            print(f"Valori inviati: {stringa_val}")
            message = s.recv(BUFFER_SIZE).decode()

            if message == "pericolo":
                sirena = "on"
            else:
                sirena = "off"

            print(message)
            print(f"Stato sirena: {sirena}")

    except ConnectionError as e:
        print(f"Errore: {e}")
    s.close()


if __name__ == "__main__":
    main()
