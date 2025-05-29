import math

class Retangulo:
    def __init__(self, b: float, h: float):
        if b <= 0 or h <= 0:
            raise ValueError("Base e altura devem ser valores positivos.")
        self.__b = b
        self.__h = h

    def SetBase(self, b: float) -> None:
        if b > 0:
            self.__b = b
        else:
            raise ValueError("A base deve ser positiva.")

    def SetAltura(self, h: float) -> None:
        if h > 0:
            self.__h = h
        else:
            raise ValueError("A altura deve ser positiva.")

    def GetBase(self) -> float:
        return self.__b

    def GetAltura(self) -> float:
        return self.__h

    def CalcArea(self) -> float:
        return self.__b * self.__h

    def CalcDiagonal(self) -> float:
        return math.sqrt(self.__b ** 2 + self.__h ** 2)

    def ToString(self) -> str:
        return f"Retângulo: base = {self.__b}, altura = {self.__h}"
