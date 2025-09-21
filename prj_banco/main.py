import os
import json
from cadastro import Pessoa
from saque import Saque
from deposito import Deposito
from transferencia import Transferencia
from saldo import Saldo
import time



def autenticar(nome, senha, arquivo="cadastro.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for pessoa in dados:
                if pessoa["nome"] == nome and pessoa["senha"] == senha:
                    return True
    else:        
        return False

def menu():
    while True:
        print("#================ MENU =================#")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Saldo")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            deposito=Deposito()
            deposito.depositar()
        elif opcao == 2:
            saque=Saque()
            saque.sacar()
        elif opcao == 3:
            transferencia=Transferencia()
            transferencia.transferir()  
        elif opcao == 4:
            saldo=Saldo()
        elif opcao == 0:
            time.sleep(2)
            print("Sessão encerrada com sucesso!")
            break

def menu_inicial():
    while True:
        print("#================ MENU INICIAL =================#")
        print("1 - Cadastro")
        print("2 - Entrar")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            Pessoa.cadastro()
        elif opcao == 2:
            nome = input("Digite o nome: ")
            senha = input("Digite a senha: ")
            verificar = autenticar(nome, senha)
            if verificar == True:
                menu()
            else:
                print("Nome ou senha incorretos. Tente novamente.")
        elif opcao == 0:
            time.sleep(2)
            print("Saída encerrada com sucesso!")
            break

if __name__ == "__main__":
    menu_inicial()