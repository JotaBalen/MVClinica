class TelaAtendimento:
    def mostrar_opcoes(self):
        print("\n--- ATENDIMENTOS ---")
        print("1. Registrar Atendimento")
        print("2. Listar Atendimentos")
        print("0. Voltar")
        return input("Escolha uma opção: ")

    def pegar_dados_atendimento(self):
        print("\n-- Registro de Atendimento --")
        cpf_paciente = input("CPF do Paciente (já cadastrado): ")
        data = input("Data (DD/MM/AAAA): ")
        hora_inicio = input("Hora Início (HH:MM): ")
        hora_fim = input("Hora Fim (HH:MM): ")
        valor = float(input("Valor Base (R$): "))
        return {"cpf_paciente": cpf_paciente, "data": data, "hora_inicio": hora_inicio, "hora_fim": hora_fim, "valor": valor}

    def listar_atendimentos(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        if not atendimentos:
            print("Nenhum atendimento registrado.")
            return
        for a in atendimentos:
            print(f"Data: {a.data_atend.strftime('%d/%m/%Y')} | Paciente: {a.paciente.nome} | Clínica: {a.clinica.nome} | Valor Total: R$ {a.calcular_valor_total():.2f}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n>>> {msg}")