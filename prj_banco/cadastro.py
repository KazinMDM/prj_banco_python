import json
class Pessoa:
    __arquivo = "cadastro.json"
    def __init__(self, nome, data_nasc, cpf, senha, rua, numero, bairro, cep,estado, saldo=0.0):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__cpf = cpf
        self.__senha = senha
        self.__saldo = saldo
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__estado = estado
    
    @classmethod
    def cadastro(cls):
        print("Cadastro de pessoa")
        nome = input("Digite o nome:\n--> ").capitalize()

        data_nasc = input("Digite a data_nasc [dd/mm/aaaa]:\n--> ")
        while len(data_nasc) != 10:
            print("Data inválida")
            data_nasc = input("Digite a data_nasc [dd/mm/aaaa]:\n--> ")

        cpf = input("Digite o CPF:\n--> ")
        while len(cpf) != 11:
            print("CPF inválido")
            cpf = input("Digite o CPF:\n--> ")

        senha = input("Digite a senha [6 digitos]:\n--> ")
        while len(senha) != 6:
            print("Senha inválida")
            senha = input("Digite a senha [6 digitos]:\n--> ")

        rua = input("Digite a rua:\n--> ")
        numero = int(input("Digite o numero:\n--> "))
        bairro = input("Digite o bairro:\n--> ")
        cep = input("Digite o cep [00000-000]:\n--> ")
        while len(cep) != 9:
            print("CEP inválido")
            cep = input("Digite o cep [00000-000]:\n--> ")
        estado = input("Digite o estado:\n--> ")
        pessoa = {
            "nome": nome,
            "data_nasc": data_nasc,
            "cpf": cpf,
            "senha": senha,
            "endereco": {
                "rua": rua,
                "numero": numero,
                "bairro": bairro,
                "cep": cep,
                "estado": estado
            },
            "saldo": 0.0
            }
        pessoas = cls.carregar_pessoas()
        pessoas.append(pessoa)
        cls.salvar_pessoas(pessoas)
        
        

    @classmethod
    def carregar_pessoas(cls):
        try:
            with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
                pessoas = json.load(arquivo)
                return pessoas
        except FileNotFoundError:
            return []

    @classmethod
    def salvar_pessoas(cls, pessoas):
        with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii=False, indent=4)
            arquivo.close()
        print("Pessoas salvas com sucesso!")

