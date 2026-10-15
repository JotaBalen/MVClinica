class TelaAtendimento:
    def mostrar_opcoes(self):
        print("\n--- ATENDIMENTOS ---")
        print("1. Registrar Atendimento")
        print("2. Listar Atendimentos")
        print("3. Alterar Atendimento")
        print("4. Excluir Atendimento")
        print("0. Voltar")
        return input("Escolha uma opção: ")

    def pegar_dados_atendimento(self):
        print("\n-- Dados do Atendimento --")
        cpf_paciente = input("CPF do Paciente: ")
        data = input("Data (DD/MM/AAAA): ")
        hora_inicio = input("Hora Início (HH:MM): ")
        hora_fim = input("Hora Fim (HH:MM): ")
        valor = float(input("Valor Base (R$): "))
        return {"cpf_paciente": cpf_paciente, "data": data, "hora_inicio": hora_inicio, "hora_fim": hora_fim, "valor": valor}

    def pegar_indice(self):
        try:
            return int(input("\nDigite o código [índice] do atendimento: "))
        except ValueError:
            return -1

    def listar_atendimentos(self, atendimentos):
            print("\n--- LISTA DE ATENDIMENTOS ---")
            if not atendimentos:
                print("Nenhum atendimento registrado.")
                return
            # Mostra o índice para facilitar a escolha na alteração/exclusão e os novos detalhes
            for i, a in enumerate(atendimentos):
                data_formatada = a.data_atend.strftime('%d/%m/%Y')
                hora_inicio_str = a.horario_inicio.strftime('%H:%M')
                hora_fim_str = a.horario_fim.strftime('%H:%M')
                
                print(f"[{i}] Data: {data_formatada} ({hora_inicio_str} às {hora_fim_str}) | "
                    f"Paciente: {a.paciente.nome} (CPF: {a.paciente.cpf}) | "
                    f"Clínica: {a.clinica.nome} | Valor Total: R$ {a.calcular_valor_total():.2f}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n>>> {msg}")