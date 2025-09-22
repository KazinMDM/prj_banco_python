import os
import json
import time
import datetime

class Saque:
    def __init__(self, nome, arquivo_json="cadastro.json"):
        self.nome = nome
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_dados()
    
    def carregar_dados(self):
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []
    
    def salvar_dados(self, dados):
        with open(self.arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")
    
    def sacar(self):
        valor_saque = float(input("Digite o valor do saque: "))
        time.sleep(1)

        pessoa_encontrada = None
        for pessoa in self.dados:
            if pessoa["nome"] == self.nome:
                pessoa_encontrada = pessoa
                break

        if pessoa_encontrada is None:
            print("Usuário não encontrado!")
            return False
        
        senha_usuario = input("Digite a senha correta: ")
        while senha_usuario != pessoa_encontrada["senha"]:
            print("Senha incorreta. Tente novamente.")
            senha_usuario = input("Digite a senha correta: ")

        time.sleep(1)
        print("Dados encontrados com sucesso!")
        time.sleep(1)
        print("Realizando saque...")
        time.sleep(1)

        if pessoa_encontrada["saldo"] >= valor_saque:
            pessoa_encontrada["saldo"] -= valor_saque

            movi_saque = {
                "tipo": "Saque",
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "valor": -valor_saque
            }
            pessoa_encontrada["extrato"].append(movi_saque)

            self.salvar_dados(self.dados)
            print("Saque realizado com sucesso!")
            time.sleep(1)
            print("Saldo atual:", pessoa_encontrada["saldo"])
            time.sleep(1.5)
            return True
        else:
            print("Saldo insuficiente para saque.")
            return False
