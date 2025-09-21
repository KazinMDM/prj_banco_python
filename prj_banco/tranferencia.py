import json
import os
import time

class Transferencia:
    def __init__(self, arquivo_json="cadastro.json"):
        self.arquivo_json = arquivo_json
        self.dados = self._carregar_dados()

    def _carregar_dados(self):        
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def _salvar_dados(self):
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=4)

    def _encontrar_por_senha(self, senha):
        for p in self.dados:
            if p.get("senha") == senha:
                return p
        return None

    def _encontrar_por_nome(self, nome):
        nome = nome.capitalize()
        for p in self.dados:
            if p.get("nome") == nome:
                return p
        return None

    def transferir(self):
        print("=== Transferência ===")
        senha = input("Digite sua senha: ")
        remetente = self._encontrar_por_senha(senha)
        if not remetente:
            print("Senha inválida ou usuário não encontrado.")
            return False

        print(f"Remetente: {remetente['nome']} - Saldo: R$ {remetente.get('saldo', 0):.2f}")
        nome_dest = input("Nome do destinatário: ")
        destinatario = self._encontrar_por_nome(nome_dest)
        if not destinatario:
            print("Destinatário não encontrado.")
            return False

        try:
            valor = float(input("Valor a transferir: R$ "))
        except ValueError:
            print("Valor inválido.")
            return False

        if valor <= 0:
            print("Valor deve ser positivo.")
            return False
        if remetente.get("saldo", 0) < valor:
            print("Saldo insuficiente.")
            return False

        time.sleep(1)
        remetente["saldo"] = remetente.get("saldo", 0) - valor
        destinatario["saldo"] = destinatario.get("saldo", 0) + valor
        self._salvar_dados()
        print("Transferência realizada com sucesso!")
        print(f"Novo saldo {remetente['nome']}: R$ {remetente['saldo']:.2f}")
        return True
