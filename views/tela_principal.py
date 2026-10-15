class TelaPrincipal:
    def mostrar_opcoes(self):
        print("\n--- SISTEMA DE CLÍNICAS ---")
        print("1. Gerenciar Pacientes")
        print("2. Gerenciar Atendimentos")
        print("0. Sair")
        return input("Escolha uma opção: ")

    def mostrar_mensagem(self, msg: str):
        print(f"\n>>> {msg}")