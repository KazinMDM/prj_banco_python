import json
import os
import time

class Dados:
    def __init__(self, nome, arquivo_json="cadastro.json"):
        self.nome = nome 
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            return []

    def salvar_dados(self, dados):
        with open(self.arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")
        time.sleep(2)

    def menu_dados(self):
        while True:
            print("#================ MENU DADOS =================#")
            print("1 - Visualizar dados")
            print("2 - Trocar senha")
            print("3 - Trocar endereço")
            print("4 - Trocar telefone")
            print("0 - Sair")

            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                for pessoa in self.dados:
                    if pessoa["nome"] == self.nome:
                        print("\n#=== Dados da conta ===#")
                        print(f"Nome: {pessoa['nome']}")
                        print(f"Data de Nascimento: {pessoa['data_nasc']}")
                        print(f"CPF: {pessoa['cpf']}")
                        print(f"Endereço: {pessoa['endereco']['rua']}, {pessoa['endereco']['numero']}")
                        print(f"Bairro: {pessoa['endereco']['bairro']}")
                        print(f"CEP: {pessoa['endereco']['cep']}")
                        print(f"Estado: {pessoa['endereco']['estado']}")
                        print(f"Saldo: R$ {pessoa['saldo']:.2f}")
                        return
                print("Conta não encontrada.")
            elif opcao == 2:
                self.nova_senha = input("Digite a nova senha: ")
                while len(self.nova_senha) != 6:
                    print("Senha inválida")
                    self.nova_senha = input("Digite a nova senha: ")
                for pessoa in self.dados:
                    if pessoa["nome"] == self.nome:
                        pessoa["senha"] = self.nova_senha
                        break
                self.salvar_dados(self.dados)
            elif opcao == 3:
                self.rua = input("Digite a rua:\n--> ")
                self.numero = int(input("Digite o numero:\n--> "))
                self.bairro = input("Digite o bairro:\n--> ")
                self.cep = input("Digite o cep [00000-000]:\n--> ")
                while len(self.cep) != 9:
                    print("CEP inválido")
                    self.cep = input("Digite o cep [00000-000]:\n--> ")
                self.estado = input("Digite o estado:\n--> ")
                for pessoa in self.dados:
                    if pessoa["nome"] == self.nome:
                        pessoa["endereco"]["rua"] = self.rua
                        pessoa["endereco"]["numero"] = self.numero
                        pessoa["endereco"]["bairro"] = self.bairro
                        pessoa["endereco"]["cep"] = self.cep
                        pessoa["endereco"]["estado"] = self.estado
                        break
                self.salvar_dados(self.dados)
            elif opcao == 4:
                novo_tel = input("Digite o novo telefone: ")
                for pessoa in self.dados:
                    if pessoa["nome"] == self.nome:
                        pessoa["telefone"] = novo_tel
                        break
                self.salvar_dados(self.dados)
            elif opcao == 0:
                time.sleep(2)
                print("Sessão encerrada com sucesso!")
                break
            