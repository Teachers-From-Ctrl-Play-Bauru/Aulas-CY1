salMinimo =  1518
criterio = salMinimo * 1.5
salPai = int(input("Salario do pai: "))
salMae = int(input("Salario do mae: "))
salAluno = int(input("Salario do aluno: "))
perCapita = (salAluno+salMae+salPai)/3

if (perCapita>criterio) :
    print("Per capita: "+str(perCapita)+", desclassificado")
else:
    print("Per capita: "+str(perCapita)+", classificado")
