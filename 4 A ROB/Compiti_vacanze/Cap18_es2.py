import random


class Carta:
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = ['Asso', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Fante', 'Regina', 'Re']

    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = self.valori[valore]

    def __str__(self):
        return f'{self.valore} di {self.seme}'

class Mazzo:
    def __init__(self):
        self.carte = [Carta(seme, valore)
                      for seme in Carta.semi
                      for valore in range(0, 13)]

    def mescola(self):
        random.shuffle(self.carte)

    def distribuisci_carta(self):
        return self.carte.pop()

    def dai_mani(self, num_mani, carte_per_mano):
        mani = []
        for i in range(num_mani):
            mano = Mano(f"Mano {i+1}")
            for _ in range(carte_per_mano):
                mano.aggiungi_carta(self.distribuisci_carta())
            mani.append(mano)
        return mani

class Mano:
    def __init__(self, nome=""):
        self.carte = []
        self.nome = nome

    def aggiungi_carta(self, carta):
        self.carte.append(carta)

    def __str__(self):
        return f"{self.nome} ha le seguenti carte: " + ", ".join(str(carta) for carta in self.carte)


def main():
    mazzo = Mazzo()
    mazzo.mescola()
    mani = mazzo.dai_mani(4, 5) 
    for mano in mani:
        print(mano)

if __name__ == "__main__":
    main()
