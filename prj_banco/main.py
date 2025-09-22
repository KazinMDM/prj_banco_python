import os
import json
import time
from cadastro import Pessoa
from saque import Saque
from deposito import Deposito
from saldo import Saldo
from transferecia import Transferencia
from dados import Dados
from extrato import Extrato


usuario_logado = None

def autenticar(nome, senha, arquivo="cadastro.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for pessoa in dados:
                if pessoa["nome"] == nome and pessoa["senha"] == senha:
                    return True
    else:        
        return False

def menu(nome):
    global usuario_logado
    while True:
        print("#================ MENU =================#")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Saldo")
        print("5 - Dados")
        print("6 - Extrato")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            deposito=Deposito(nome)
            deposito.depositar()
        elif opcao == 2:
            saque=Saque(nome)
            saque.sacar()
        elif opcao == 3:
            transferencia=Transferencia(nome)
            transferencia.transferir()
        elif opcao == 4:
            saldo=Saldo(nome)
        elif opcao == 5:
            dados=Dados(nome)
            dados.menu_dados()
        elif opcao == 6:
            extrato = Extrato(nome)
            extrato.visualizar_extrato()            
        elif opcao == 0:
            time.sleep(2)
            print("Sessão encerrada com sucesso!")
            break

def menu_inicial():
    global usuario_logado
    while True:
        print("#================ MENU INICIAL =================#")
        print("1 - Cadastro")
        print("2 - Entrar")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            Pessoa.cadastro()
        elif opcao == 2:
            nome = input("Digite o nome: ").capitalize()
            senha = input("Digite a senha: ")
            verificar = autenticar(nome, senha)
            if verificar == True:
                usuario_logado = nome
                menu(nome)
            else:
                print("Nome ou senha incorretos. Tente novamente.")
        elif opcao == 0:
            time.sleep(2)
            print("Saída efetuada com sucesso!")
            break

if __name__ == "__main__":
    menu_inicial()