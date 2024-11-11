import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(SERVER_ADDRESS)
        print("Connesso al server.")

        while True:
            print("\nScegli un'azione:")
            print("1. Controlla se un file esiste")
            print("2. Ottieni il numero di frammenti di un file")
            print("3. Ottieni l'IP dell'host di un frammento specifico")
            print("4. Ottieni tutti gli IP degli host di un file")
            print("5. Esci")

            scelta = input("Scelta: ")

            if scelta == "1":
                s.sendall("check_file".encode())
                message = s.recv(BUFFER_SIZE).decode()
                filename = input(f"{message} ")
                s.sendall(filename.encode())
                risposta = s.recv(BUFFER_SIZE).decode()
                print("Risultato:", risposta)

            elif scelta == "2":
                s.sendall("get_fragment_count".encode())
                message = s.recv(BUFFER_SIZE).decode()
                filename = input(f"{message} ")
                s.sendall(filename.encode())
                risposta = s.recv(BUFFER_SIZE).decode()
                print("Numero di frammenti:", risposta)

            elif scelta == "3":
                s.sendall("get_fragment_host".encode())
                message = s.recv(BUFFER_SIZE).decode()
                filename, fragment_number = input(f"{message} ").split(";")
                s.sendall(f"{filename};{fragment_number}".encode())
                risposta = s.recv(BUFFER_SIZE).decode()
                print("IP dell'host:", risposta)

            elif scelta == "4":
                s.sendall("get_all_hosts".encode())
                message = s.recv(BUFFER_SIZE).decode()
                filename = input(f"{message} ")
                s.sendall(filename.encode())
                risposta = s.recv(BUFFER_SIZE).decode()
                print("IP degli host:", risposta)

            elif scelta == "5":
                print("Chiusura client.")
                break

            else:
                print("Scelta non valida.")

    except ConnectionError as e:
        print(f"Errore di connessione: {e}")

    finally:
        s.close()
        print("Connessione chiusa.")

if __name__ == "__main__":
    main()
