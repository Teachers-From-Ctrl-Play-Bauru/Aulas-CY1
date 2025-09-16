feirinha = [] # lista inicialmente vazia
#entrada de limite
limite = int(input("Diga quantos itens vai colocar: "))
i = 0
while  i<limite: #enquanto o indice for menor que o limite
    feirinha.append(input()) #adiciona item no final da lista 
    i+=1 #adiciona mais 1 em i
print(feirinha) #mostra o resultado







'''
feiraOrdenada = sorted(feirinha)
feiraInversa = feirinha
feiraInversa.reverse() 
print("Feira ordenada: "+ str(feiraOrdenada))
print("Feira Inversa: "+ str(feiraInversa))
'''

