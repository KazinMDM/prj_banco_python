import json
import os
import time

class Transferencia:
    def __init__(self, arquivo_json="cadastro.json"):
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON."""
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def salvar_dados(self):
        """Salva os dados atualizados no arquivo JSON."""
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")

    def transferir(self):
        """Realiza transferência entre dois usuários."""
        print("\n=== Transferência Bancária ===")

        # Identificação do remetente
        senha_origem = input("Digite sua senha (remetente): ")
        remetente = None
        for pessoa in self.dados:
            if pessoa["senha"] == senha_origem:
                remetente = pessoa
                break

        if not remetente:
            print("Usuário remetente não encontrado ou senha incorreta.")
            return False

        print(f"Remetente: {remetente['nome']} - Saldo atual: R$ {remetente['saldo']:.2f}")

        # Identificação do destinatário
        nome_destinatario = input("Digite o nome do destinatário: ").capitalize()
        destinatario = None
        for pessoa in self.dados:
            if pessoa["nome"] == nome_destinatario:
                destinatario = pessoa
                break

        if not destinatario:
            print("Destinatário não encontrado.")
            return False

        # Valor da transferência
        try:
            valor = float(input("Digite o valor da transferência: R$ "))
        except ValueError:
            print("Valor inválido.")
            return False

        if valor <= 0:
            print("O valor deve ser positivo.")
            return False

        if remetente["saldo"] < valor:
            print("Saldo insuficiente.")
            return False

        # Processando transferência
        time.sleep(1)
        print("Processando transferência...")
        remetente["saldo"] -= valor
        destinatario["saldo"] += valor

        self.salvar_dados()

        print(f"\nTransferência de R$ {valor:.2f} realizada com sucesso!")
        print(f"Novo saldo de {remetente['nome']}: R$ {remetente['saldo']:.2f}")
        print(f"Novo saldo de {destinatario['nome']}: R$ {destinatario['saldo']:.2f}")

        return True
