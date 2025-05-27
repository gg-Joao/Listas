import math

class Circulo:
    def __init__(self):
        self.__raio = 0.0  # raio privado

    def set_raio(self, v):
        if v >= 0:
            self.__raio = v
        else:
            print("Raio inválido!")

    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return math.pi * (self.__raio ** 2)

    def calc_circunferencia(self):
        return 2 * math.pi * self.__raio

    def __str__(self):
        return (f"Raio: {self.__raio:.2f}, "
                f"Área: {self.calc_area():.2f}, "
                f"Circunferência: {self.calc_circunferencia():.2f}")
