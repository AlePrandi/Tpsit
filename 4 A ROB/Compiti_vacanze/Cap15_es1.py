import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cerchio:
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio

class Rettangolo:
    def __init__(self, larghezza, altezza, angolo_inferiore_sinistro):
        self.larghezza = larghezza
        self.altezza = altezza
        self.angolo_inferiore_sinistro = angolo_inferiore_sinistro

def punto_nel_cerchio(cerchio, punto):
    distanza = math.sqrt((punto.x - cerchio.centro.x) ** 2 + (punto.y - cerchio.centro.y) ** 2)
    return distanza <= cerchio.raggio

def rett_nel_cerchio(cerchio, rettangolo):
    p1 = rettangolo.angolo_inferiore_sinistro
    p2 = Punto(p1.x + rettangolo.larghezza, p1.y)
    p3 = Punto(p1.x, p1.y + rettangolo.altezza)
    p4 = Punto(p2.x, p2.y + rettangolo.altezza)
    
    return (punto_nel_cerchio(cerchio, p1) and
            punto_nel_cerchio(cerchio, p2) and
            punto_nel_cerchio(cerchio, p3) and
            punto_nel_cerchio(cerchio, p4))

def rett_cerchio_sovrapp(cerchio, rettangolo):
    p1 = rettangolo.angolo_inferiore_sinistro
    p2 = Punto(p1.x + rettangolo.larghezza, p1.y)
    p3 = Punto(p1.x, p1.y + rettangolo.altezza)
    p4 = Punto(p2.x, p2.y + rettangolo.altezza)
    
    return (punto_nel_cerchio(cerchio, p1) or
            punto_nel_cerchio(cerchio, p2) or
            punto_nel_cerchio(cerchio, p3) or
            punto_nel_cerchio(cerchio, p4))

def main():
   
    centro_cerchio = Punto(150, 100)
    cerchio = Cerchio(centro_cerchio, 75)
    
 
    punto = Punto(160, 100)
    print("Il punto è nel cerchio:", punto_nel_cerchio(cerchio, punto))
    

    angolo_rettangolo = Punto(120, 80)
    rettangolo = Rettangolo(50, 30, angolo_rettangolo)
    

    print("Il rettangolo è nel cerchio:", rett_nel_cerchio(cerchio, rettangolo))
    
    
    print("Il rettangolo si sovrappone al cerchio:", rett_cerchio_sovrapp(cerchio, rettangolo))

if __name__ == "__main__":
    main()
