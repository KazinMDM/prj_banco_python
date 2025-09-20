import os
from cadastro import Pessoa

# from saque import Saque


def menu():
    while True:
        print("#================ MENU =================#")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Saldo")
        print("3 - Extrato")
        print("0 - Sair")

        # opcao = int(input("Digite a opção desejada: "))
        # if opcao == 1:
            
        # elif opcao == 2:
            
        # elif opcao == 3:
            
        # elif opcao == 4:
            
        # elif opcao == 0:
        #     break

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
            if Pessoa.autenticar(nome, senha):
                menu()
            else:
                print("Nome ou senha incorretos")
        elif opcao == 0:
            break

if __name__ == "__main__":
    menu_inicial()