import random

class Carta:
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = ['Asso', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Fante', 'Regina', 'Re']

    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def __str__(self):
        return f'{Carta.valori[self.valore]} di {self.seme}'

class Mazzo:
    def __init__(self):
        self.carte = [Carta(seme, valore)
                      for seme in Carta.semi
                      for valore in range(13)]

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

class PokerHand(Mano):
    def ha_coppia(self):
        valori = [carta.valore for carta in self.carte]
        return any(valori.count(valore) == 2 for valore in set(valori))

    def ha_doppiacoppia(self):
        valori = [carta.valore for carta in self.carte]
        contatori = [valori.count(valore) for valore in set(valori)]
        return contatori.count(2) == 2

    def ha_tris(self):
        valori = [carta.valore for carta in self.carte]
        return any(valori.count(valore) == 3 for valore in set(valori))

    def ha_scala(self):
        valori = sorted(set(carta.valore for carta in self.carte))
        return len(valori) >= 5 and any(
            valori[i:i+5] == list(range(valori[i], valori[i] + 5)) 
            for i in range(len(valori) - 4)
        )

    def ha_colore(self):
        semi = [carta.seme for carta in self.carte]
        return any(semi.count(seme) >= 5 for seme in set(semi))

    def ha_full(self):
        return self.ha_tris() and self.ha_coppia()

    def ha_poker(self):
        valori = [carta.valore for carta in self.carte]
        return any(valori.count(valore) == 4 for valore in set(valori))

    def ha_scalareale(self):
        if not self.ha_colore():
            return False
        valori = sorted(carta.valore for carta in self.carte)
        return set(valori[-5:]) == {9, 10, 11, 12, 13}

    def classifica(self):
        if self.ha_scalareale():
            self.label = "Scala Reale"
        elif self.ha_poker():
            self.label = "Poker"
        elif self.ha_full():
            self.label = "Full"
        elif self.ha_colore():
            self.label = "Colore"
        elif self.ha_scala():
            self.label = "Scala"
        elif self.ha_tris():
            self.label = "Tris"
        elif self.ha_doppiacoppia():
            self.label = "Doppia Coppia"
        elif self.ha_coppia():
            self.label = "Coppia"
        else:
            self.label = "Nessuna"

def calcola_probabilita():
    mazzo = Mazzo()
    mazzo.mescola()
    mani = mazzo.dai_mani(9, 5)  
    conta_mani = {
        "Scala Reale": 0,
        "Poker": 0,
        "Full": 0,
        "Colore": 0,
        "Scala": 0,
        "Tris": 0,
        "Doppia Coppia": 0,
        "Coppia": 0,
        "Nessuna": 0
    }

    for mano in mani:
        poker_hand = PokerHand(mano.nome)
        poker_hand.carte = mano.carte
        poker_hand.classifica()
        conta_mani[poker_hand.label] += 1
        print(mano)

    totale_mani = len(mani)
    for combinazione, conteggio in conta_mani.items():
        print(f"{combinazione}: {conteggio / totale_mani:.2%}")

if __name__ == "__main__":
    calcola_probabilita()
