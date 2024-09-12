class Tempo:
    def __init__(self, ore=0, minuti=0, secondi=0):
        self.secondi_dalla_mezzanotte = ore * 3600 + minuti * 60 + secondi
    
    def int_in_tempo(self, int_sec):
        self.secondi_dalla_mezzanotte = int_sec

    def tempo_in_int(self):
        return self.secondi_dalla_mezzanotte

    def __add__(self, altro):
        return Tempo(secondi=self.secondi_dalla_mezzanotte + altro.secondi_dalla_mezzanotte)

    def __sub__(self, altro):
        return Tempo(secondi=self.secondi_dalla_mezzanotte - altro.secondi_dalla_mezzanotte)

    def __str__(self):
        ore = self.secondi_dalla_mezzanotte // 3600
        minuti = (self.secondi_dalla_mezzanotte % 3600) // 60
        secondi = self.secondi_dalla_mezzanotte % 60
        return f"{ore:02}:{minuti:02}:{secondi:02}"

def main():
    tempo1 = Tempo(9, 45, 0)
    tempo2 = Tempo(1, 35, 0)
    print("Tempo 1:", tempo1)
    print("Tempo 2:", tempo2)
    somma = tempo1 + tempo2
    print("Somma:", somma)
    differenza = tempo1 - tempo2
    print("Differenza:", differenza)
    tempo_totale = Tempo()
    tempo_totale.int_in_tempo(tempo1.tempo_in_int())
    print("Tempo totale:", tempo_totale)

if __name__ == "__main__":
    main()
