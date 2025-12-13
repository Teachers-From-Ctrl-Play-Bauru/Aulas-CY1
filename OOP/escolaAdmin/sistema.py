from aluno import Aluno

class Sistema:

    def __init__(self):
        self.listaAlunos = []
        self.menu()
    
    def menu(self):
        print("--- Cadastro de Alunos ---")
        print("1 - inserir")
        print("2 - atualizar")
        print("3 - deletar")
        print("4 - listar")
        print("5 - sair")
        self.opcao = input()

        if(self.opcao == '1'):
            self.inserir()

            
    # função que pede como entrada os atributos da classe Aluno 
    # e adiciona um novo aluno na variável listaAlunos[]
    # ao terminar o cadastro chame o menu de novo
    def inserir(self):
        print("entrou em inserir")
        while True:
            print("deseja inserir um novo aluno? (y/n)")
            resposta = input()
            if resposta == "y":
                nome = input("nome: ")
                ra = input("RA: ")
                n1 = input("nota 1: ")
                n2 = input("nota 2: ")
                novoAluno = Aluno(nome,ra,n1,n2)
                self.listaAlunos.append(novoAluno)
            else:
                break





sistema = Sistema() # criando um objeto de sistema
