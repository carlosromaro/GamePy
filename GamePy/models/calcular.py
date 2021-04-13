from random import randint
import PySimpleGUI as sg


class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__operacao: int = randint(1, 3)
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    @property
    def _gerar_valor(self: object) -> int:
        if self.__dificuldade == 1 and (self.operacao == 1 or self.__operacao == 2):
            return randint(5, 30)
        elif self.__dificuldade == 2 and (self.operacao == 1 or self.__operacao == 2):
            return randint(16, 99)
        elif self.__dificuldade == 3 and (self.__operacao == 1 or self.__operacao == 2):
            return randint(30, 150)
        elif self.__dificuldade == 1 and self.__operacao == 3:
            return randint(3, 10)
        elif self.__dificuldade == 2 and self.__operacao == 3:
            return randint(3, 20)
        elif self.__dificuldade == 3 and self.__operacao == 3:
            return randint(5, 35)

    @property
    def _gerar_resultado(self):
        if self.__operacao == 1:
            return self.__valor1 + self.__valor2
        elif self.__operacao == 2:
            return self.__valor1 - self.__valor2
        elif self.__operacao == 3:
            return self.__valor2 * self.__valor1

    def __str__(self):
        return f'{self.valor1}\n{self.valor2}\n{self.operacao}\n{self.resultado}'

    def checar_resultado(self: object, resposta: int) -> bool:
        if self.resultado == resposta:
            return True
        else:
            return False

    def gerar_operacao(self: object) -> str:
        op: str = str
        if self.__operacao == 1:
            op = '+'
        elif self.__operacao == 2:
            op = '-'
        else:
            op = '*'

        return f'{self.__valor1} {op} {self.__valor2} = '
