import turtle

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

def disegna_rett(t, rettangolo):
    t.penup()
    t.goto(rettangolo.angolo_inferiore_sinistro.x, rettangolo.angolo_inferiore_sinistro.y)
    t.pendown()
    t.forward(rettangolo.larghezza)
    t.left(90)
    t.forward(rettangolo.altezza)
    t.left(90)
    t.forward(rettangolo.larghezza)
    t.left(90)
    t.forward(rettangolo.altezza)
    t.left(90)

def disegna_cerchio(t, cerchio):
    t.penup()
    t.goto(cerchio.centro.x, cerchio.centro.y - cerchio.raggio)
    t.pendown()
    t.circle(cerchio.raggio)

def main():
    t = turtle.Turtle()

    angolo_rettangolo = Punto(0, 0)
    rettangolo = Rettangolo(100, 50, angolo_rettangolo)
    disegna_rett(t, rettangolo)


    centro_cerchio = Punto(-200, -50)
    cerchio = Cerchio(centro_cerchio, 75)
    disegna_cerchio(t, cerchio)

    turtle.done()

if __name__ == "__main__":
    main()
