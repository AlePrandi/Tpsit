import threading
import time

class ContoBancario(threading.Thread):
    def __init__(self, saldo, numero_conto):
        super.__init__()
        self.saldo = saldo
        self.numero_conto = numero_conto
        
    def run(self):
        pass
        
class ContoCorrente(ContoBancario):
    def __init__(self):
        super.__init__()
        
    def run(self):
        pass
    
class ContoRisparmio(ContoBancario):
    def __init__(self):
        super.__init__()
        
    def run(self):
        pass
    
def main():
    pass

if __name__ == '__main__':
    main()