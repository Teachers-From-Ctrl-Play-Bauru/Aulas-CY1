#Código produto
preco = [10.00, 9.00, 7.00, 6.00, 12.00] 
limite =int(input("Quantidade de itens: "))
i = 0
valorTotal = 1
while i< limite:
    cod = int(input("Código do produto: "))
    uni = int(input("Unidades do produto: "))
    valorTotal += preco[cod-1] * uni
    i+= 1
print("Preço total em R$: " + str(valorTotal))

    