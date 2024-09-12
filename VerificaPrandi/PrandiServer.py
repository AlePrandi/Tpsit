import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096

lock = threading.Lock()

rubrica = {
    "Mario Rossi": "123-456-7890",
    "Luca Bianchi": "234-567-8901",
    "Giulia Verdi": "345-678-9012",
    "Elena Neri": "456-789-0123",
    "Roberto Russo": "567-890-1234"
}

class Rubrica_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
        
    def run(self):
        while self.running:
            
            messaggio = self.connection.recv(BUFFERSIZE) #ricevo  il messaggio 
            ricerca, tipo = messaggio.decode().split("|") #faccio la split sugli elementi
            #faccio un controllo sul tipo di ricerca che ha scelto il client e se è presente
            if ricerca == "Cerca-nome":
                for chiave in rubrica:
                    if tipo == rubrica[chiave]:
                        self.connection.sendall(chiave.encode())#se ricevo il numero restituisco il nome
            elif ricerca == "Cerca-numero":
                for chiave in rubrica:
                    if tipo == chiave:
                        self.connection.sendall(rubrica[chiave].encode())# se ricevo il nome restituisco il numero
            elif ricerca == "Aggiungi-contatto":
                    with lock: #faccio la lock per permettere a solo un client alla volta di aggiungere un contatto
                        nome, numero = tipo.split(";")
                        rubrica[nome] = numero # creo un nuovo elemento del dizionario del dizionario 
                        self.connection.sendall("OK".encode())        
            else:
                self.connection.sendall("Azione non valida".encode())
                    
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    while True:
        s.listen()
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        thread = Rubrica_handler(connection)
        thread.start()


if __name__ == "__main__":
    main()
