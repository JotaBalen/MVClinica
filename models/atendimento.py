from datetime import date, time
from models.pessoa import Paciente, Profissional
from models.clinica import Clinica
from models.pagamento import Pagamento

class TipoAtendimento:
    def __init__(self, nome: str):
        self.__nome = nome
    @property
    def nome(self): return self.__nome

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional_responsavel: Profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional_responsavel = profissional_responsavel
    @property
    def custo(self): return self.__custo
    @property
    def descricao(self): return self.__descricao

class Atendimento:
    def __init__(self, data_atend: date, horario_inicio: time, horario_fim: time, valor_base: float,
                 paciente: Paciente, profissional: Profissional, clinica: Clinica, tipo: TipoAtendimento):
        self.__data_atend = data_atend
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor_base = valor_base
        self.__paciente = paciente
        self.__profissional = profissional
        self.__clinica = clinica
        self.__tipo = tipo
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def data_atend(self): return self.__data_atend
    @data_atend.setter
    def data_atend(self, data): self.__data_atend = data

    @property
    def horario_inicio(self): return self.__horario_inicio
    @horario_inicio.setter
    def horario_inicio(self, hora): self.__horario_inicio = hora

    @property
    def horario_fim(self): return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, hora): self.__horario_fim = hora

    @property
    def valor_base(self): return self.__valor_base
    @valor_base.setter
    def valor_base(self, valor): self.__valor_base = valor

    @property
    def paciente(self): return self.__paciente
    @paciente.setter
    def paciente(self, pac): self.__paciente = pac

    @property
    def clinica(self): return self.__clinica
    @property
    def procedimentos(self): return self.__procedimentos

    def adicionar_procedimento(self, proc: Procedimento):
        self.__procedimentos.append(proc)

    def registrar_pagamento(self, pag: Pagamento):
        self.__pagamentos.append(pag)

    def calcular_valor_total(self) -> float:
        total_procedimentos = sum(p.custo for p in self.__procedimentos)
        return self.__valor_base + total_procedimentos

    def calcular_saldo_restante(self) -> float:
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.calcular_valor_total() - total_pago