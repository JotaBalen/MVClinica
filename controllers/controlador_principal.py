from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_atendimento import ControladorAtendimento
from views.tela_principal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.__ctrl_paciente = ControladorPaciente(self)
        self.__ctrl_atendimento = ControladorAtendimento(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def ctrl_paciente(self): return self.__ctrl_paciente
    @property
    def ctrl_atendimento(self): return self.__ctrl_atendimento

    def iniciar(self):
        opcoes = {
            "1": self.__ctrl_paciente.abrir_tela,
            "2": self.menu_atendimentos,
            "0": exit
        }
        while True:
            try:
                opcao = self.__tela_principal.mostrar_opcoes()
                funcao = opcoes.get(opcao)
                if funcao:
                    funcao()
                else:
                    self.__tela_principal.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_principal.mostrar_mensagem(str(e))

    def menu_atendimentos(self):
        self.__ctrl_atendimento.abrir_tela()