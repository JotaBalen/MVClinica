from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, nome): self.__nome = nome

    @property
    def cpf(self): return self.__cpf
    
    @property
    def celular(self): return self.__celular
    @celular.setter
    def celular(self, celular): self.__celular = celular

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self): return self.__data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data): self.__data_nascimento = data

    def calcular_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year
        if (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day):
            idade -= 1
        return idade

class Profissional(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self): return self.__especialidade
    @property
    def registro_profissional(self): return self.__registro_profissional