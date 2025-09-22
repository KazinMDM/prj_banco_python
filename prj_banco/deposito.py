import os
import json
import time
import datetime

class Deposito:
    def __init__(self, nome,arquivo_json="cadastro.json"):
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
            arquivo.close()
        print("Dados salvos com sucesso!")
    
    
    def depositar(self):
        valor_deposito = float(input("Digite o valor do deposito: "))
        time.sleep(1)
        senha_usuario = input("Digite a senha do usuário: ")

        pessoa_encontrada = None
        while pessoa_encontrada is None:
            for pessoa in self.dados:
                if pessoa["nome"] == self.nome:
                    if pessoa["senha"] == senha_usuario:
                        pessoa_encontrada = pessoa  
                        break
                    else:
                        print("Senha incorreta. Tente novamente.")
                        senha_usuario = input("Digite a senha correta: ")

        time.sleep(2)
        print("Dados encontrados com sucesso!")
        time.sleep(1)
        print("Realizando deposito...")
        time.sleep(1)
        pessoa_encontrada["saldo"] += valor_deposito

        movi_deposito = {
            "tipo": "Depósito",
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "valor": valor_deposito
        }

        pessoa_encontrada["extrato"].append(movi_deposito)
        self.salvar_dados(self.dados)
        print("Deposito realizado com sucesso!")
        time.sleep(1)
        print("Saldo atual:", pessoa_encontrada["saldo"])
        time.sleep(1.5)