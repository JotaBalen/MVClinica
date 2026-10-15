from abc import ABC, abstractmethod
from datetime import date
from models.pessoa import Paciente

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, data_pag: date, paciente: Paciente, valor_pago: float):
        self.__data_pag = data_pag
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def valor_pago(self): return self.__valor_pago
    @property
    def data_pag(self): return self.__data_pag
    @property
    def paciente(self): return self.__paciente

class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pag: date, paciente: Paciente, valor_pago: float):
        super().__init__(data_pag, paciente, valor_pago)

class PagamentoPix(Pagamento):
    def __init__(self, data_pag: date, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pag, paciente, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): return self.__cpf_pagador

class PagamentoCartao(Pagamento):
    def __init__(self, data_pag: date, paciente: Paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data_pag, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira