import json
class Pessoa:
    __arquivo = "cadastro.json"
    def __init__(self, nome, idade, cpf, senha, saldo=0.0):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__senha = senha
        self.__saldo = saldo

    @classmethod
    def cadastro(cls):
        print("Cadastro de pessoa")
        nome = input("Digite o nome: ")
        idade = (input("Digite a idade: "))
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        pessoa = {
            "nome": nome,
            "idade": idade,
            "cpf": cpf,
            "senha": senha,
            "saldo": 0.0
            }
        pessoas = cls.carregar_pessoas()
        pessoas.append(pessoa)
        cls.salvar_pessoas(pessoas)
        
        

    @classmethod
    def carregar_pessoas(cls):
        try:
            with open(cls.__arquivo, "r") as arquivo:
                pessoas = json.load(arquivo)
                return pessoas
        except FileNotFoundError:
            return []

    @classmethod
    def salvar_pessoas(cls, pessoas):
        with open(cls.__arquivo, "w") as arquivo:
            json.dump(pessoas, arquivo)
            arquivo.close()
        print("Pessoas salvas com sucesso!")

