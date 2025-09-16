idade = int(input("Qual a sua idade? "))
alistou = ""
if(idade >= 18):
    alistou = input("Você já se alistou?")
if(alistou=="s" and idade>=18 or idade<18):
    print("está em dia com o alistamento")
else:
    print("não está em dia com o alistamento")
#operadores lógicos: <=,>=,==, !=, and, or, not
 