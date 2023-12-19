import math
x = 13
y = 16
k = 13


class Figura():

    def area(self):
        return 0

    def perimetro(self):
        return 0

    def view(self):
        print("Los datos de la figura son: {}".format(self))


class Circulo(Figura):
    def __init__(self, _x, _y, _r) -> None:
        self.x = _x
        self.y = _y
        self.r = _r
        pass

    def area(self):
        return math.pi * self.r ** 2

    def perimetro(self):
        return 2 * math.pi * self.r


class Cuadrado(Figura):
    def __init__(self, _x, _y, _w, _h) -> None:
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h
        pass

    def area(self):
        return self.w * self.h

    def perimetro(self):
        return 2 * self.w + 2 * self.h


my_figura_1 = Circulo(0, 0, 13)
my_area = my_figura_1.area()
peri = my_figura_1.perimetro()

my_figura_2 = Cuadrado(3, 4, 10, 10)
pass
