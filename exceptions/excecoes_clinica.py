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

class CpfInalteravelException(Exception):
    def __init__(self):
        super().__init__("Erro de Segurança: O CPF é um documento de identificação único e não pode ser modificado na alteração de cadastro.")

class CpfDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Erro: Já existe um paciente cadastrado com este CPF no sistema.")

class CpfInvalidoException(Exception):
    def __init__(self):
        super().__init__("Erro: O CPF é inválido. Digite apenas números, sem letras ou pontuações.")