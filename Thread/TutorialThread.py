from threading import Thread #classe genitore per i Thread che usiamo noi
import time

class MioThread(Thread):
    def __init__(self, nome): 
        super().__init__()
        self.nome = nome
        self.running = True
        
    def run(self):
        #codice del Thread
        while self.running:
            print(f"Sono il Thread {self.nome}")
            time.sleep(1)
            
    def kill(self):
        self.running = False
            
def main():
    lista_nomi = ["Brama", "Sciolla", "Bergia"]
    lista_thread = [MioThread(k) for k in lista_nomi]
    for t in lista_thread:
        t.start()
        
    for _ in range(4):
        print("Sono il main Thread")
        time.sleep(1)
        
    for t in lista_thread:
        t.kill()
        t.join() # necessario per farli riunire al main thread
        
    print("\nSono il main Thread e ho chiuso chiuso tutti gli altri")
    
if __name__ == "__main__":
    main()