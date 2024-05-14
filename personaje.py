class Personaje:
    def __init__(self, y, x):
        self.puntos = 0
        self.posicion_y = y
        self.posicion_x = x
        self.anchura = 10
        self.altura = 100
        
    def moverse(self, n):
        self.posicion_y += n
        
    def update(self):
        if self.posicion_y < 25:
            self.posicion_y = 25
        elif self.posicion_y > 475:
            self.posicion_y = 475
    