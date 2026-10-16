from datetime import date
from models.pessoa import Paciente
from views.tela_paciente import TelaPaciente
from exceptions.excecoes_clinica import CpfInalteravelException, CpfDuplicadoException, CpfInvalidoException

class ControladorPaciente:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_paciente = TelaPaciente()
        self.__pacientes = []

    def abrir_tela(self):
        opcoes = {
            "1": self.incluir,
            "2": self.listar,
            "3": self.alterar,
            "4": self.excluir,
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

    def buscar_paciente_por_cpf(self, cpf):
        for p in self.__pacientes:
            if p.cpf == cpf:
                return p
        return None

    def incluir(self):
        try:
            dados = self.__tela_paciente.pegar_dados_paciente()
            
            # Verifica se o utilizador digitou letras no CPF
            if not dados["cpf"].isdigit():
                raise CpfInvalidoException()
            
            # Impede cadastrar dois pacientes com o mesmo CPF
            if self.buscar_paciente_por_cpf(dados["cpf"]):
                raise CpfDuplicadoException()
                
            nascimento = date(dados["ano"], dados["mes"], dados["dia"])
            paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], nascimento)
            self.__pacientes.append(paciente)
            self.__tela_paciente.mostrar_mensagem("Paciente cadastrado com sucesso.")
            
        except (CpfDuplicadoException, CpfInvalidoException) as e:
            self.__tela_paciente.mostrar_mensagem(str(e))
        except ValueError:
            self.__tela_paciente.mostrar_mensagem("Erro: Data de nascimento inválida. Digite apenas números.")

    def listar(self):
        self.__tela_paciente.listar_pacientes(self.__pacientes)

    def alterar(self):
        cpf_busca = self.__tela_paciente.pegar_cpf()
        paciente = self.buscar_paciente_por_cpf(cpf_busca)
        
        if not paciente:
            self.__tela_paciente.mostrar_mensagem("Paciente não encontrado.")
            return
            
        self.__tela_paciente.mostrar_mensagem(f"Modificando dados de: {paciente.nome} (CPF: {paciente.cpf})")
        
        try:
            # Chama a nova função da View que NÃO pede o CPF
            dados = self.__tela_paciente.pegar_dados_alteracao()

            # O CPF continua intacto. Alteramos apenas os dados mutáveis.
            paciente.nome = dados["nome"]
            paciente.celular = dados["celular"]
            paciente.data_nascimento = date(dados["ano"], dados["mes"], dados["dia"])
            
            self.__tela_paciente.mostrar_mensagem("Paciente alterado com sucesso.")
            
        except ValueError:
            self.__tela_paciente.mostrar_mensagem("Erro: Data de nascimento inválida.")

    def excluir(self):
        cpf = self.__tela_paciente.pegar_cpf()
        paciente = self.buscar_paciente_por_cpf(cpf)
        
        if not paciente:
            self.__tela_paciente.mostrar_mensagem("Paciente não encontrado.")
            return
            
        self.__pacientes.remove(paciente)
        self.__tela_paciente.mostrar_mensagem("Paciente excluído com sucesso.")

    def retornar(self):
        pass

    @property
    def pacientes(self): return self.__pacientes