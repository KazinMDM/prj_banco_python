import os
import json
import time

class Extrato:
    def __init__(self, nome, arquivo_json="cadastro.json"):
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_dados()
        self.nome = nome

    def carregar_dados(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def visualizar_extrato(self):
        print("\n============= Extrato Bancário =============")
        for pessoa in self.dados:
            if pessoa["nome"] == self.nome:
                if not pessoa.get("extrato"):
                    print("Nenhuma movimentação registrada.")
                else:
                    for mov in pessoa["extrato"]:
                        tipo = mov.get("tipo", "")
                        data = mov.get("data", "")
                        valor = mov.get("valor", 0.0)
                        de = mov.get("de", "")
                        para = mov.get("para", "")

                        linha = f"[{data}] {tipo} | Valor: R$ {valor:.2f}"
                        if de:
                            linha += f" | De: {de}"
                        if para:
                            linha += f" | Para: {para}"
                        print(linha)
                break