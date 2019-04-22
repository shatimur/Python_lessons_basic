# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    @property
    def _sq(self):      # площадь треугольника через определитель второго порядка
        s = abs(1/2*(self.x1-self.x3)*(self.y2-self.y3)-(self.x2-self.x3)*(self.y1-self.y3))
        return s

    def _height(self):  # высота треугольника через площадь и длину одной из сторон
        from math import sqrt
        d = sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)   # длина оной из сторон треугольника
        h = (2*self.sq)/d
        return h

    def _perimetr(self):
        from math import sqrt
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
    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def if_trapeze(self):   # если 2 стороны параллельны, а другие две непараллельны, и длина двух непараллельных стороны равна - то это равнобедренная трапеция
        if y3 - y2 == y4 - y1 and \         # по-хорошему, нужно такую проверку и для двух других сторон, но так как задача в создании класса, то не буду усложнять
            y2 - y1 != y3 - y4 and \
            (x3 - x1) ** 2 + (y3 - y1) ** 2 == (x4 - x2) ** 2 + (y3 - y2) ** 2:
            return True

    @property
    def _d_side(self):      # длина боковой стороны трапеции
        from math import sqrt
        d_side = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return d_side

    @property               # для обращения не как как к функции, а как к аргументу
    def _d_up(self):        # длина верхнего основания трапеции
        from math import sqrt
        d_up = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        return d_up

    @property
    def _d_down(self):      # длина нижнего основания трапеции
        from math import sqrt
        d_down = sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        return d_down

    @property
    def _height(self):      # высота трапеции
        from math import sqrt
        h = sqrt(self.d_side ** 2 - ((self.d_down - self.d_up) ** 2) / 4)
        return h

    def _sq(self):          # площадь трапеции
        s = self.height * ((self.d_down + self.d_up) / 2)
        return s

    def _perimetr(self):    # периметр трапеции
        p = 2 * self.d_side + self.d_up + self.d_down
        return p

