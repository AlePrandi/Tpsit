import sqlite3
import socket
import threading

# Impostazioni server
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        try:
            with sqlite3.connect("./file.db") as conn_db:
                cur = conn_db.cursor()

                while True:
                    message = self.connection.recv(BUFFER_SIZE)
                    if not message:
                        print("Nessun messaggio ricevuto, chiusura connessione")
                        break

                    message = message.decode()
                    print(f"Ricevuto messaggio dal client: {message}")

                    query = None  # Inizializza query a None

                    if message == "check_file":
                        
                        self.connection.sendall("Inserisci il nome del file: ".encode())
                        filename = self.connection.recv(BUFFER_SIZE).decode()
                        
                        query = f"""
                                SELECT COUNT(*)
                                FROM files
                                WHERE nome LIKE '%{filename}%'
                                """

                    elif message == "get_fragment_count":
                        
                        self.connection.sendall("Inserisci il nome del file: ".encode())
                        filename = self.connection.recv(BUFFER_SIZE).decode()
                        
                        query = f"""
                                SELECT tot_frammenti
                                FROM files
                                WHERE nome LIKE '%{filename}%'
                                """

                    elif message == "get_fragment_host":
                        
                        self.connection.sendall("Inserisci il nome del file e numero del frammento (file;fram): ".encode())
                        data = self.connection.recv(BUFFER_SIZE).decode()
                        filename, num = data.split(";")
                        
                        query = f"""
                                SELECT f.host
                                FROM frammenti AS f, files AS fi
                                WHERE f.id_file = fi.id_file
                                AND fi.nome LIKE '%{filename}%'
                                AND f.n_frammento ='{num}'
                                """

                    elif message == "get_all_hosts":
                        
                        self.connection.sendall("Inserisci il nome del file: ".encode())
                        filename = self.connection.recv(BUFFER_SIZE).decode()
                        
                        query = f"""
                                SELECT f.host
                                FROM frammenti AS f, files AS fi
                                WHERE f.id_file = fi.id_file
                                AND fi.nome LIKE '%{filename}%'
                                """
                    else:
                        self.connection.sendall("Azione".encode())
                        continue

                    if query:
                        cur.execute(query)
                        risposta = cur.fetchall()
                        if not risposta:
                            risposta = "Nessun risultato trovato."
                        self.connection.sendall(str(risposta).encode())

        except Exception as e:
            print(f"Errore: {e}")

        finally:
            self.connection.close()
            print("Connessione chiusa con il client")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()


if __name__ == "__main__":
    main()
