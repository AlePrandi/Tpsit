class Canguro:
    def __init__(self, contenuto_tasca=None):
        if contenuto_tasca is None:
            contenuto_tasca = []
        self.contenuto_tasca = contenuto_tasca
    
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    
    def __str__(self):
        return f"Canguro con oggetti nella tasca: {self.contenuto_tasca}"

# Test del codice
def main():
    can = Canguro()
    guro = Canguro()
    can.intasca('chiavi')
    guro.intasca('telefono')
    can.intasca(guro)
    
    print(can)
    print(guro)

if __name__ == "__main__":
    main()
