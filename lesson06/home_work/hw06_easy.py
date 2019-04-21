# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    x1 = int
    x2 = int
    x3 = int
    y1 = int
    y2 = int
    y3 = int

    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def sq(self):
        s = abs(1/2*(self.x1-self.x3)*(self.y2-self.y3)-(self.x2-self.x3)*(self.y1-self.y3))
        return s

    def height(self):
        from math import sqrt
        d = sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        h = (2*sq(self))/d
        return h

    def perimetr(self):
        d1 = sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        d2 = sqrt((self.x3-self.x1)**2 + (self.y3-self.y1)**2)
        d3 = sqrt((self.x2-self.x3)**2 + (self.y2-self.y3)**2)
        p = d1 + d2 + d3
        return p

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Isosceles_trapeze:
    x1 = int
    x2 = int
    x3 = int
    x4 = int
    y1 = int
    y2 = int
    y3 = int
    y4 = int
    from math import sqrt

    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def if_trapeze(self):
        if y3 - y2 == y4 - y1 and \
                y2 - y1 != y3 - y4 and \
                (x3 - x1) ** 2 + (y3 - y1) ** 2 == (x4 - x2) ** 2 + (y3 - y2) ** 2:
            return True

    def sq(self):
        d_up = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        d_down = sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        s = height(self) * ((d_down + d_up) / 2)

    def perimetr(self):
        d_side = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        d_up = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        d_down = sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        p = 2 * d_side + d_up + d_down
        return p

    def height(self):
        d_side = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        d_up = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        d_down = sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        h = sqrt(d_side ** 2 - ((d_down - d_up) ** 2) / 4)
        return h

