class Tempo:
    def __init__(self, ore, minuti, secondi):
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi
    
    def tot_secondi(self):
        return self.ore * 3600 + self.minuti * 60 + self.secondi
    
    def from_secondi(self, tot_sec):
        self.ore = tot_sec // 3600
        self.minuti = (tot_sec % 3600) // 60
        self.secondi = tot_sec % 60

    def __str__(self):
        return f"{self.ore:02}:{self.minuti:02}:{self.secondi:02}"

def moltiplica_tempo(tempo, numero):
    tot_sec = tempo.tot_secondi() * numero
    nuovo_tempo = Tempo()
    nuovo_tempo.from_secondi(int(tot_sec))
    return nuovo_tempo

def media_gara(tempo_finale, distanza):
    return moltiplica_tempo(tempo_finale, 1 / distanza)

def main():
    
    tempo_finale = Tempo(1, 30, 0)  
    distanza = 15  # distanza percorsa in km
    
    tempo_per_km = media_gara(tempo_finale, distanza)
    print("Tempo al chilometro:", tempo_per_km)

if __name__ == "__main__":
    main()
