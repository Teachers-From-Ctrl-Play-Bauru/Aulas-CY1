cardapio = {"expresso":7.0,  "pingado": 9.0, "pão na chapa":11.0, "achocolatado": 13.0, "misto quente": 15.0}
precoTotal = 0
while True:
    item = input().lower()
    if(item != ""):
        qtd = int(input())
        precoTotal += cardapio[item] * qtd
    else:
        break
print(precoTotal)
