from datetime import datetime, date, time
from exceptions.excecoes_clinica import IdadeInvalidaException, HorarioInvalidoException, DataPagamentoInvalidaException, ObjetoNaoEncontradoException
from models.atendimento import Atendimento, TipoAtendimento
from models.pagamento import Pagamento
from models.clinica import Clinica
from models.pessoa import Profissional
from views.tela_atendimento import TelaAtendimento

class ControladorAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_atendimento = TelaAtendimento()
        self.__atendimentos = []
        
        self.__clinica_padrao = Clinica("Clínica UFSC", "Florianópolis", "Clínica Geral", time(8, 0), time(18, 0))
        self.__profissional_padrao = Profissional("Dr. Silva", "999999999", "00000000000", "Clínico Geral", "CRM-SC 1234")
        self.__tipo_padrao = TipoAtendimento("Consulta de Rotina")

    def abrir_tela(self):
        opcoes = {
            "1": self.incluir,
            "2": self.listar,
            "3": self.alterar,
            "4": self.excluir,
            "0": self.retornar
        }
        while True:
            opcao = self.__tela_atendimento.mostrar_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
                if opcao == "0": break
            else:
                self.__tela_atendimento.mostrar_mensagem("Opção inválida.")

    def incluir(self):
        try:
            dados = self.__tela_atendimento.pegar_dados_atendimento()
            paciente = self.buscar_paciente(dados["cpf_paciente"])
            
            data_obj = datetime.strptime(dados["data"], "%d/%m/%Y").date()
            hora_in = datetime.strptime(dados["hora_inicio"], "%H:%M").time()
            hora_out = datetime.strptime(dados["hora_fim"], "%H:%M").time()

            self.criar_atendimento(paciente, self.__clinica_padrao, self.__profissional_padrao, self.__tipo_padrao, data_obj, hora_in, hora_out, dados["valor"])
            self.__tela_atendimento.mostrar_mensagem("Atendimento registrado com sucesso!")
        
        except (IdadeInvalidaException, HorarioInvalidoException, ObjetoNaoEncontradoException) as e:
            self.__tela_atendimento.mostrar_mensagem(str(e))
        except ValueError:
            self.__tela_atendimento.mostrar_mensagem("Erro: Formato de data/hora (use DD/MM/AAAA e HH:MM) ou valor inválido.")

    def listar(self):
        self.__tela_atendimento.listar_atendimentos(self.__atendimentos)

    def alterar(self):
        self.listar()
        if not self.__atendimentos: return
        
        indice = self.__tela_atendimento.pegar_indice()
        if indice < 0 or indice >= len(self.__atendimentos):
            self.__tela_atendimento.mostrar_mensagem("Atendimento não encontrado.")
            return
            
        atendimento = self.__atendimentos[indice]
        self.__tela_atendimento.mostrar_mensagem("Digite os novos dados para este atendimento:")
        try:
            dados = self.__tela_atendimento.pegar_dados_atendimento()
            paciente = self.buscar_paciente(dados["cpf_paciente"])

            data_obj = datetime.strptime(dados["data"], "%d/%m/%Y").date()
            hora_in = datetime.strptime(dados["hora_inicio"], "%H:%M").time()
            hora_out = datetime.strptime(dados["hora_fim"], "%H:%M").time()
            
            if paciente.calcular_idade() < 18:
                raise IdadeInvalidaException()
            if hora_in < atendimento.clinica.hora_abertura or hora_out > atendimento.clinica.hora_fechamento:
                raise HorarioInvalidoException()

            atendimento.paciente = paciente
            atendimento.data_atend = data_obj
            atendimento.horario_inicio = hora_in
            atendimento.horario_fim = hora_out
            atendimento.valor_base = dados["valor"]
            
            self.__tela_atendimento.mostrar_mensagem("Atendimento alterado com sucesso!")
        except (IdadeInvalidaException, HorarioInvalidoException, ObjetoNaoEncontradoException) as e:
            self.__tela_atendimento.mostrar_mensagem(str(e))
        except ValueError:
            self.__tela_atendimento.mostrar_mensagem("Erro: Formato de dados inválido.")

    def excluir(self):
        self.listar()
        if not self.__atendimentos: return
        
        indice = self.__tela_atendimento.pegar_indice()
        if indice < 0 or indice >= len(self.__atendimentos):
            self.__tela_atendimento.mostrar_mensagem("Atendimento não encontrado.")
            return
            
        self.__atendimentos.pop(indice)
        self.__tela_atendimento.mostrar_mensagem("Atendimento excluído com sucesso!")

    def retornar(self):
        pass

    def buscar_paciente(self, cpf):
        paciente = None
        for p in self.__controlador_principal.ctrl_paciente.pacientes:
            if p.cpf == cpf:
                paciente = p
                break
        if not paciente:
            raise ObjetoNaoEncontradoException("Paciente")
        return paciente

    def criar_atendimento(self, paciente, clinica, profissional, tipo, data_atend, hora_inicio, hora_fim, valor):
        if paciente.calcular_idade() < 18:
            raise IdadeInvalidaException()
        if hora_inicio < clinica.hora_abertura or hora_fim > clinica.hora_fechamento:
            raise HorarioInvalidoException()
        novo_atend = Atendimento(data_atend, hora_inicio, hora_fim, valor, paciente, profissional, clinica, tipo)
        self.__atendimentos.append(novo_atend)
        return novo_atend

    @property
    def atendimentos(self): return self.__atendimentos