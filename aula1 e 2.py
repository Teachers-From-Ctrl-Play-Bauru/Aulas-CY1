#Escreva um progrma que 
# entre com o nome de um aluno
#entre com a primeira nota de prova
# entre com a segunda nota de prova
# Mostre o nome e a média de provas
#texto = input("Entre com o nome") # entre com  o nome
#nota1 = int(input("Entre com a nota ")) # entre com a nota #média = n1 + n2 / 2
#print(nota1) exemplo de saída
nome = input("Entre com o nome do aluno: ")
nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))
print(nome)
#media = (nota1 + nota2)/2 
#print(media)
# facam uma condicional que diga se o aluno foi aprovado caso media seja > 5, senão diga que ele reprovou
if((nota1 + nota2)/2 <5 ):
    print("reprovado")
else:
    print("Aprovado")