import datetime
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
            with sqlite3.connect("./fiumi.db", check_same_thread=False) as conn_db:
                cur = conn_db.cursor()
                message = self.connection.recv(BUFFER_SIZE).decode()
                id,livello_att,data = message.split("|")
                livello_att = float(livello_att)
                while True:
                    tempo_att = str(datetime.datetime.now()).split(" ")
                    tempo_att = float(tempo_att[1].replace(":", "")) #converto in float per fare il calcolo
                    if tempo_att - float(data) > 15:
                        query = f"""
                                    SELECT fiume,localita, livello
                                    FROM livelli
                                    WHERE id_stazione LIKE '%{id}%'
                                    """
                        cur.execute(query)
                        dati = cur.fetchall()[0]
                        print(f"Ricevuto:{dati[0]},{dati[1]}, {data}")
                        livello_max = dati[2]
                        perc30 = livello_max * 30 / 100
                        perc70 = livello_max * 70 / 100
                        
                        if livello_att < perc30:
                            self.connection.sendall("avvenuta ricezione".encode())
                        if livello_att > perc30 and livello_att < perc70:
                            self.connection.sendall("avvenuta ricezione".encode())
                            print("Pericolo imminente")
                        if livello_att > perc70:
                            self.connection.sendall("pericolo".encode())
                            print(f"Pericolo in corso nella stazione {dati[1]} del fiume {dati[0]}")
                        
        except ConnectionError as e:
            print(e)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()

    s.close()


if __name__ == "__main__":
    main()
