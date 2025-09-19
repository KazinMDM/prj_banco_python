import os
from cadastro import Pessoa


def menu():
    while True:
        print("#================ MENU =================#")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Saldo")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao != int:
            print("Opção inválida")
            menu()

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
            
        elif opcao == 3:
            extrato()
        elif opcao == 0:
            break

if __name__ == "__main__":
    menu_inicial()