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
        
        # Dados padrão para agilizar os testes e a apresentação
        self.__clinica_padrao = Clinica("Clínica UFSC", "Florianópolis", "Clínica Geral", time(8, 0), time(18, 0))
        self.__profissional_padrao = Profissional("Dr. Silva", "999999999", "00000000000", "Clínico Geral", "CRM-SC 1234")
        self.__tipo_padrao = TipoAtendimento("Consulta de Rotina")

    def abrir_tela(self):
        opcoes = {
            "1": self.incluir,
            "2": self.listar,
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
            
            # Busca o paciente na lista de pacientes do ControladorPaciente pelo CPF
            paciente = None
            for p in self.__controlador_principal.ctrl_paciente.pacientes:
                if p.cpf == dados["cpf_paciente"]:
                    paciente = p
                    break
            
            if not paciente:
                raise ObjetoNaoEncontradoException("Paciente")

            # Converte as strings digitadas pelo usuário para objetos de data e hora do Python
            data_obj = datetime.strptime(dados["data"], "%d/%m/%Y").date()
            hora_in = datetime.strptime(dados["hora_inicio"], "%H:%M").time()
            hora_out = datetime.strptime(dados["hora_fim"], "%H:%M").time()

            # Chama o método que contém as validações exigidas pelo trabalho
            self.criar_atendimento(paciente, self.__clinica_padrao, self.__profissional_padrao, self.__tipo_padrao, data_obj, hora_in, hora_out, dados["valor"])
            
            self.__tela_atendimento.mostrar_mensagem("Atendimento registrado com sucesso!")
        
        except (IdadeInvalidaException, HorarioInvalidoException, ObjetoNaoEncontradoException) as e:
            self.__tela_atendimento.mostrar_mensagem(str(e))
        except ValueError:
            self.__tela_atendimento.mostrar_mensagem("Erro: Formato de data/hora (use DD/MM/AAAA e HH:MM) ou valor inválido.")
        except Exception as e:
            self.__tela_atendimento.mostrar_mensagem(f"Erro inesperado: {e}")

    def listar(self):
        self.__tela_atendimento.listar_atendimentos(self.__atendimentos)

    def retornar(self):
        pass

    def criar_atendimento(self, paciente, clinica, profissional, tipo, data_atend, hora_inicio, hora_fim, valor):
        # Validação: Paciente precisa ter 18 anos
        if paciente.calcular_idade() < 18:
            raise IdadeInvalidaException()

        # Validação: Horário comercial da clínica
        if hora_inicio < clinica.hora_abertura or hora_fim > clinica.hora_fechamento:
            raise HorarioInvalidoException()

        novo_atend = Atendimento(data_atend, hora_inicio, hora_fim, valor, paciente, profissional, clinica, tipo)
        self.__atendimentos.append(novo_atend)
        return novo_atend

    def pagar_atendimento(self, atendimento: Atendimento, pagamento: Pagamento):
        if pagamento.data_pag > atendimento.data_atend:
            raise DataPagamentoInvalidaException()
        atendimento.registrar_pagamento(pagamento)

    @property
    def atendimentos(self): return self.__atendimentos