class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0     

    def set_distancia(self, d):
        if d >= 0:
            self.__distancia = d
        else:
            print("Distância inválida!")

    def set_tempo(self, horas, minutos):
        tempo_total = horas + minutos / 60.0
        if tempo_total > 0:
            self.__tempo = tempo_total
        else:
            print("Tempo inválido!")

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        if self.__tempo > 0:
            return self.__distancia / self.__tempo
        else:
            return 0.0

    def __str__(self):
        return f"Distância: {self.__distancia:.2f} km, Tempo: {self.__tempo:.2f} h, Velocidade Média: {self.velocidade_media():.2f} km/h"
