#i semafori regolano l'ordine dei thread e permettono ai thread di lavorare in contemporanea 
#mutex serve per dare la precedenza ai thread con il metodo 
import threading
import time

class Magazzino:
    def __init__(self):
        self.merce = 0
        self.semaphore = threading.Semaphore(1)  # Inizializzazione del semaforo con valore 1

    def aggiungi_merce(self):
        with self.semaphore:
            self.merce += 1
            print(f"Merce aggiunta. Totale merce: {self.merce}")

    def processo_aggiunta_merce(self, nome_processo, numero_aggiunte):
        for _ in range(numero_aggiunte):
            self.aggiungi_merce()
            time.sleep(0.5)  # Simulazione di un processo che richiede del tempo per aggiungere la merce

# Utilizzo della classe Magazzino
magazzino = Magazzino()

# Creazione di tre thread che simulano processi di aggiunta di merce
thread1 = threading.Thread(target=magazzino.processo_aggiunta_merce, args=("Processo 1", 3))
thread2 = threading.Thread(target=magazzino.processo_aggiunta_merce, args=("Processo 2", 2))
thread3 = threading.Thread(target=magazzino.processo_aggiunta_merce, args=("Processo 3", 4))

# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()

# Attendo il completamento dei thread
thread1.join()
thread2.join()
thread3.join()

print("Operazioni di aggiunta merce completate. Totale merce nel magazzino:", magazzino.merce)
 