from datetime import date
from models.pessoa import Paciente
from views.tela_paciente import TelaPaciente

class ControladorPaciente:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_paciente = TelaPaciente()
        self.__pacientes = []

    def abrir_tela(self):
        opcoes = {
            "1": self.incluir,
            "2": self.listar,
            "0": self.retornar
        }
        while True:
            opcao = self.__tela_paciente.mostrar_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
                if opcao == "0": break
            else:
                self.__tela_paciente.mostrar_mensagem("Opção inválida.")

    def incluir(self):
        try:
            dados = self.__tela_paciente.pegar_dados_paciente()
            nascimento = date(dados["ano"], dados["mes"], dados["dia"])
            paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], nascimento)
            self.__pacientes.append(paciente)
            self.__tela_paciente.mostrar_mensagem("Paciente cadastrado com sucesso.")
        except ValueError:
            self.__tela_paciente.mostrar_mensagem("Erro: Data de nascimento inválida.")
        except Exception as e:
            self.__tela_paciente.mostrar_mensagem(f"Erro inesperado: {e}")

    def listar(self):
        self.__tela_paciente.listar_pacientes(self.__pacientes)

    def retornar(self):
        pass

    @property
    def pacientes(self): return self.__pacientes