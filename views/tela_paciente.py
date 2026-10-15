class TelaPaciente:
    def mostrar_opcoes(self):
        print("\n--- PACIENTES ---")
        print("1. Incluir Paciente")
        print("2. Listar Pacientes")
        print("0. Voltar")
        return input("Escolha uma opção: ")

    def pegar_dados_paciente(self):
        print("\n-- Cadastro de Paciente --")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        ano = int(input("Ano de nascimento (AAAA): "))
        mes = int(input("Mês de nascimento (MM): "))
        dia = int(input("Dia de nascimento (DD): "))
        return {"nome": nome, "celular": celular, "cpf": cpf, "ano": ano, "mes": mes, "dia": dia}

    def listar_pacientes(self, pacientes):
        print("\n--- LISTA DE PACIENTES ---")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return
        for p in pacientes:
            print(f"Nome: {p.nome} | CPF: {p.cpf} | Idade: {p.calcular_idade()} anos")

    def mostrar_mensagem(self, msg: str):
        print(f"\n>>> {msg}")