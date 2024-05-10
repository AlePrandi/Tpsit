import threading
import time

# lock = threading.Lock()
semaforo = threading.Semaphore(1)
# mettere semaforo a 1 è come fare la lock
# il numero indica la quantità di thread
# che possono accedere alla sezione critica


class StampaNome(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        # with lock: #metodo alternativo a acquire e release
        with semaforo:
            for _ in range(5):
                print("Ciao ", end="")
                time.sleep(1)
                print(self.nome)


def main():
    nomi = ["mauro", "brama", "poggis", "sciula"]
    listaThread = [StampaNome(nome) for nome in nomi]
    for t in listaThread:
        t.start()

    for t in listaThread:
        t.join()


if __name__ == "__main__":
    main()
