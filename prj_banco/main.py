from deposito import deposito

def menu():
    while True:
        print("#================ MENU ================#")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        if opcao != int:
            print("Opção inválida")
            menu()
        else:
            continue

        if opcao == 1:
            
        elif opcao == 2:
            saque()
        elif opcao == 3:
            extrato()
        elif opcao == 0:
            break

if __name__ == "__main__":
    menu()