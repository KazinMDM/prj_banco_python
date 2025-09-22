import json
import os
import time
import datetime

class Transferencia:
    def __init__(self, nome,arquivo_json="cadastro.json"):
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

    def salvar_dados(self):
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")

    def transferir(self):
        print("\n============= Transferência Bancária ===============")

        senha_usuario = input("Digite a senha do usuário: ")
        time.sleep(1)
        remetente = None
        while remetente is None:
            for pessoa in self.dados:
                if pessoa["nome"] == self.nome:
                    if pessoa["senha"] == senha_usuario:
                        remetente = pessoa  
                        break
                    else:
                        print("Senha incorreta. Tente novamente.")
                        senha_usuario = input("Digite a senha correta: ")
        if not remetente:
            print("Usuário não encontrado ou senha incorreta.")
            return False
        print(f"Remetente: {remetente['nome']} - Saldo atual: R$ {remetente['saldo']}")

        nome_destinatario = input("Digite o nome do destinatário: ").capitalize()
        destinatario = None
        for pessoa in self.dados:
            if pessoa["nome"] == nome_destinatario:
                destinatario = pessoa
                break

        if not destinatario:
            print("Destinatário não encontrado.")
            return False

        try:
            valor_transf = float(input("Digite o valor da transferência: R$ "))
        except ValueError:
            print("Valor inválido.")
            return False

        if valor_transf <= 0:
            print("O valor deve ser positivo.")
            return False

        if remetente["saldo"] < valor_transf:
            print("Saldo insuficiente.")
            return False

        time.sleep(1)
        print("Processando transferência...")
        remetente["saldo"] -= valor_transf
        destinatario["saldo"] += valor_transf

        movi_remetente = {
            "tipo": "Transferência enviada",
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "valor": -valor_transf,
            "para": destinatario["nome"]
        }
        remetente["extrato"].append(movi_remetente)

        movi_destinatario = {
            "tipo": "Transferência recebida",
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "valor": valor_transf,
            "de": remetente["nome"]
        }
        destinatario["extrato"].append(movi_destinatario)

        self.salvar_dados()
        time.sleep(1)
        print(f"\nTransferência de R$ {valor_transf} realizada com sucesso!")
        time.sleep(1)
        print(f"Novo saldo de {remetente['nome']}: R$ {remetente['saldo']}")
        time.sleep(1.5)
        return True
