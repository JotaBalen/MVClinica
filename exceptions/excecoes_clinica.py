class IdadeInvalidaException(Exception):
    def __init__(self):
        super().__init__("Erro: O paciente deve ter mais de 18 anos para realizar o atendimento independentemente.")

class HorarioInvalidoException(Exception):
    def __init__(self):
        super().__init__("Erro: O horário do atendimento está fora do horário de funcionamento da clínica.")

class DataPagamentoInvalidaException(Exception):
    def __init__(self):
        super().__init__("Erro: O pagamento não pode ser realizado em data posterior ao atendimento.")

class ObjetoNaoEncontradoException(Exception):
    def __init__(self, objeto: str):
        super().__init__(f"Erro: {objeto} não encontrado(a) no sistema.")