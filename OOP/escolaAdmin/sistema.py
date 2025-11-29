import aluno 

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

        if(self.opcao == 1):
            self.inserir()
            
    # função que pede como entrada os atributos da classe Aluno 
    # e adiciona um novo aluno na variável listaAlunos[]
    # ao terminar o cadastro chame o menu de novo
    def inserir(self):
        pass



sistema = Sistema() # criando um objeto de sistema
