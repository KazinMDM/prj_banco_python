import os
import json
from cadastro import Pessoa
from saque import Saque
from deposito import Deposito

def autenticar(nome, senha, arquivo="cadastro.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if nome in dados and dados[nome]["senha"] == senha:
                return True
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
            Deposito.depositar()
        elif opcao == 2:
            Saque.saque()
        # elif opcao == 3:
            
        # elif opcao == 4:
            
        elif opcao == 0:
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
            if autenticar(nome, senha) == True:
                menu()
            else:
                print("Nome ou senha incorretos. Tente novamente.")
        elif opcao == 0:
            break

if __name__ == "__main__":
    menu_inicial()