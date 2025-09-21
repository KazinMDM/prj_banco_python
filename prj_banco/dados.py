import json
import os
import time

class Dados:
    def __init__(self, arquivo_json="cadastro.json"):
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
            arquivo.close()
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
                print(self.dados)
            elif opcao == 2:
                self.nova_senha = input("Digite a nova senha: ")
                while len(self.nova_senha) != 6:
                    print("Senha inválida")
                    self.nova_senha = input("Digite a nova senha: ")
                self.dados[0]["senha"] = self.nova_senha
                self.salvar_dados(self.dados)
            elif opcao == 3:
                self.rua = input("Digite a rua:\n--> ")
                self.numero = int(input("Digite o numero:\n--> "))
                self.bairro = input("Digite o bairro:\n--> ")
                self.cep = input("Digite o cep [00000-000]:\n--> ")
                while len(cep) != 9:
                    print("CEP inválido")
                    cep = input("Digite o cep [00000-000]:\n--> ")
                self.estado = input("Digite o estado:\n--> ")
                self.dados[0]["rua"] = self.rua
                self.dados[0]["numero"] = self.numero
                self.dados[0]["bairro"] = self.bairro
                self.dados[0]["cep"] = self.cep
                self.dados[0]["estado"] = self.estado
                self.salvar_dados(self.dados)
            elif opcao == 4:
                self.dados[0]["telefone"] = input("Digite o novo telefone: ")
                self.salvar_dados(self.dados)
            elif opcao == 0:
                time.sleep(2)
                print("Sessão encerrada com sucesso!")
                break