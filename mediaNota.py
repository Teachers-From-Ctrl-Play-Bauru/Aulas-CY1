dicAlunoNotas = {} # dicionario Aluno:notas[]

continuar = True

#cadastro de alunos e notas
while continuar:
    aluno = input("Nome do Aluno: ")
    if(aluno != ""):
        print("Entre com as 3 avaliações: \n")
        i = 1
        media = 0
        somaNotas = 0
        nota1 = int(input("Instrumento 1: "))
        nota2 = int(input("Instrumento 2: "))
        nota3 = int(input("Instrumento 3: "))
        
        media= (nota1+nota2+nota3)/3
        dicAlunoNotas[aluno] = [nota1, nota2, nota3, media]
    else:
        continuar = False

#mostrar alunos e notas:

for aluno in dicAlunoNotas:
    print(aluno)
    notasMedia = dicAlunoNotas[aluno] 
    for nota in notasMedia:
        print(nota)
