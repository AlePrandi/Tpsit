import threading
import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        print("Cosa vuoi cercare ? (nome, numero, aggiunta): ")
        scelta = input("scelta: ")
        #faccio un controllo sulla scelta dell'utente
        if scelta == "nome":
            messaggio = input("inserisci il numero del nome che vuoi cercare: ")
            s.sendall(f"Cerca-nome|{messaggio}".encode())
            
        elif scelta == "numero":
            messaggio = input("inserisci il nome di cui vuoi sapere il numero: ")
            s.sendall(f"Cerca-numero|{messaggio}".encode())
            
        elif scelta == "aggiunta":
            nome = input("inserisci il nome: ")
            numero = input("inserisci il numero: ")
            s.sendall(f"Aggiungi-contatto|{nome};{numero}".encode())
            
        else:
            print("Scelta non valida")# se non è una delle scelte possibili
        message = s.recv(BUFFERSIZE)
        message = message.decode()
        print(message)
    s.close()


if __name__ == '__main__':
    main()
