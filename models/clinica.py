from datetime import time

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str, hora_abertura: time, hora_fechamento: time):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__hora_abertura = hora_abertura
        self.__hora_fechamento = hora_fechamento

    @property
    def nome(self): return self.__nome
    @property
    def hora_abertura(self): return self.__hora_abertura
    @property
    def hora_fechamento(self): return self.__hora_fechamento