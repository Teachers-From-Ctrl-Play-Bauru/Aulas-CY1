
import turtle
import time
continuar = True

def init_screen():
    turtle.Screen().setup(1.0, 1.0)

def selecao(opcao):
    if(opcao == 4):
       global continuar
       continuar = False
       print("Você saiu")
    elif (opcao == 1):
        desenha_quad(int(input("Entre com o tamanho: ")))
    elif (opcao == 2):
        desenha_circ(int(input("Entre com o raio: ")))
    elif (opcao == 3):
        desenha_tri(int(input("Entre com o tamanho: ")))

def desenha_tri(tamanho):
    for _ in range(3):
        turtle.forward(tamanho)
        turtle.right(120)
    time.sleep(3)
    #turtle.clear()
       


def desenha_circ(raio):
     turtle.circle(raio)
     time.sleep(3)
     turtle.clear()


def desenha_quad(tamanho):
    for _ in range(4):
        turtle.forward(tamanho)
        turtle.right(90)
    time.sleep(3)
    turtle.clear()

init_screen()
while continuar:
    print("--- Desenhar Forma ---")
    print("1 - Quadrado")
    print("2 - Círculo")
    print("3 - Triângulo")
    print("4 - sair")
    opc = int(input("Entre com o número da opção: "))
    selecao(opc)






