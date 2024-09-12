import threading
import time

class MyThread(threading.Thread): # MyThread è una sottoclasse di threading.Thread

# Il metodo __init__ è il costruttore della classe, prende i parametri name, delay e inizializza gli attributi delay e name
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self): #run è un metodo che viene eseguito quando si avvia il thread
        print("Thread %s avviato" % self.name)
        print("In attesa di %d secondi" % self.delay)
        time.sleep(self.delay) # attesa dell'attributo delay
        print("Thread %s completato" % self.name)

# Sottoclasse che eredita da MyThread
class MyThreadSubclass(MyThread): # sottoclasse di MyThread eredita tutti gli attributi e i metodi di MyThread
# il costruttore inizializza l'attributo repeat e permette di specificare il numero di ripetizioni per l'operazione
    def __init__(self, name, delay, repeat):
        super().__init__(name, delay)
        self.repeat = repeat

    def run(self):
        print("Thread %s avviato" % self.name)
    # questo metodo esegue un ciclo specificato dal parametro repeat stampando un messaggio per ogni iterazione e attende per un certo arco di tempo tra le iterazioni
        for i in range(self.repeat):
            print("Ciclo %d di %s" % (i+1, self.name))
            time.sleep(self.delay)
        print("Thread %s completato" % self.name)

# Creazione di istanze di classi thread
thread1 = MyThread("Thread 1", 2) # istanza di MyThread
thread2 = MyThreadSubclass("Thread 2", 3, 2)  # istanza di MyThreadSubclass
thread3 = MyThread("Thread 3",2 ,3 )

# Avvio dei thread con utilizzo del metodo start che fa eseguire il metodo run
thread1.start()
thread2.start()
thread3.start()

# il metodo join attende che entrambi i thread bbiano terminato l'esecuzione prima di procedere con il resto del codice+
thread1.join()
thread2.join()
thread3.join()

print("Fine del programma")