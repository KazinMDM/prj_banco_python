import json
import os

class Saldo:
    def __init__(self, arquivo_json="cadastro.json"):
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_pessoas()
        self.nome = input("confirme seus dados [Insira seu nome]:\n-->")
        self.visualizar_saldo()

    def carregar_pessoas(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def visualizar_saldo(self):
        try:
            for pessoa in self.dados:
                if pessoa["nome"] == self.nome:
                    print(f"Saldo atual de {self.nome}: R$ {pessoa['saldo']:.2f}")
        except:
            print("Conta não encontrada.")
