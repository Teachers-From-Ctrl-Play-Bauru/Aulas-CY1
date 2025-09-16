print("--- Classificador de Ângulo ---")
alfa = int(input("Entre com o ângulo: "))
if(alfa < 90):
    print("agudo")
elif(alfa>90):
    print("obtuso")
else:
    print("reto")