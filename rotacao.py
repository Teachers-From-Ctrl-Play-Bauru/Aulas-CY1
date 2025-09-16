print("-- Calculadora de Rotações --")
angulo = int(input("Entre com o ângulo da rotação: "))

if(angulo < 360):
    print("Não há rotações completas")
else:
    rotacoes = int(angulo/360)
    print(f"O ângulo {angulo} realizou {rotacoes} rotacoes ")