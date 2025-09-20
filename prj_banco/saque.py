import os
import json
import time

class Saque:
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
    
    def sacar(self):
        valor_saque = float(input("Digite o valor do saque: "))
        time.sleep(1)
        senha_correta = input("Digite a senha correta: ")
        while True:
            pessoa_encontrada = False
            for pessoa in self.dados:
                if pessoa["senha"] == senha_correta:
                    pessoa_encontrada = True
                    break
            if pessoa_encontrada:
                break
            else:
                print("Senha incorreta. Tente novamente.")
                senha_correta = input("Digite a senha correta: ")
        time.sleep(2)
        print("Dados encontrados com sucesso!")
        time.sleep(1)
        print("Realizando saque...")
        time.sleep(1)
        for pessoa in self.dados:
            if pessoa["saldo"] >= valor_saque:
                pessoa["saldo"] -= valor_saque
                time.sleep(1)
                print("Saque realizado com sucesso!")
                time.sleep(1)
                print("Saldo atual:", pessoa["saldo"])
                self.salvar_dados(self.dados)
                return True
            else:
                print("Saldo insuficiente para saque.")
                return False