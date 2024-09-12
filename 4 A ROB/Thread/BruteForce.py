#psw: lettere minuscole alfabeto fatta da n caratteri come variabile globale
#alfabeto (21)
#ogni thread avrà come parametro la lettera

import threading

password = "giorgis"
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z']

class lettThread(threading.Thread):
    def __init__(self, lettera):
        super().__init__()
        self.lettera = lettera

    def run(self):
        for c1 in alfabeto:
            for c2 in alfabeto:
                for c3 in alfabeto:
                    for c4 in alfabeto:
                        for c5 in alfabeto:
                            for c6 in alfabeto:
                                for c7 in alfabeto:
                                    pw = self.lettera + c1 + c2 + c3 + c4 + c5 + c6 + c7
                                    if pw == password:
                                        print("Password: " + pw)
                                        break

def main():
    lista_thread = [lettThread(l) for l in alfabeto]
    for t in lista_thread:
        t.start()
            
if __name__ == "__main__":
    main()