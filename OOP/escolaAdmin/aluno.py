class Aluno:

    def __init__(self, nome, RA, nota1, nota2):
        self.nome = nome
        self.set_RA(RA)
        self.set_N1(nota1)
        self.set_N2(nota2)

    
    def ficha_aluno(self):
        self.valores()
        self.calculo_média()

    def valores(self):
        print(f'---- ficha de identificação ----')
        print(f'nome:{self.nome}')
        print(f'Registro de aluno:{self.__RA}')

    def calculo_média(self):
        print(f'primeira nota:{self.nota1}')
        print(f'segunda nota:{self.nota2}')
        self.media = (self.nota1+self.nota2)/2
        print(f'média:{self.media}')

    def get_RA(self):
        return self.__RA
    
    def get_N1(self):
        return self.__n1
    
    
    def get_N2(self):
        return self.__n2
    
    

    def set_RA(self, novoRA ):
        try:
            if int(novoRA) <= 0:
             raise ValueError("RA deve ser maior que 0") 
            else:
                self.__RA = novoRA
        except:
            print("RA deve ser uma sequência numérica")
   
    def set_N1(self, n1):
        try:
            self.__n1 =  int(n1)
        except:
            print("Nota deve ser um número")
     
    def set_N2(self, n2):
        try:
            self.__n2 =  int(n2)
        except:
            print("Nota deve ser um número")



            



    pass

#FI = Aluno(nome= input('nome:'), RA= input('RA:'), nota1= int(input('sua nota 1:')), nota2= int(input('sua nota2:')), média= '')
#FI.ficha_aluno()