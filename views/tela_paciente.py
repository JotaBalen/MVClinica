class TelaPaciente:
    def mostrar_opcoes(self):
        print("\n--- PACIENTES ---")
        print("1. Incluir Paciente")
        print("2. Listar Pacientes")
        print("3. Alterar Paciente")
        print("4. Excluir Paciente")
        print("0. Voltar")
        return input("Escolha uma opção: ")

    def pegar_dados_paciente(self):
        print("\n-- Dados do Paciente --")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        ano = int(input("Ano de nascimento (AAAA): "))
        mes = int(input("Mês de nascimento (MM): "))
        dia = int(input("Dia de nascimento (DD): "))
        return {"nome": nome, "celular": celular, "cpf": cpf, "ano": ano, "mes": mes, "dia": dia}

    def pegar_cpf(self):
        return input("Digite o CPF do paciente: ")

    def listar_pacientes(self, pacientes):
        print("\n--- LISTA DE PACIENTES ---")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return
        for p in pacientes:
            print(f"Nome: {p.nome} | CPF: {p.cpf} | Idade: {p.calcular_idade()} anos")

    def mostrar_mensagem(self, msg: str):
        print(f"\n>>> {msg}")