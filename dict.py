dict = {"pão na chapa":[7,8,9] , "strawberry":"morango", "pineple": "abacaxi"}

print(dict["strawberry"]) #acessando item pela chave
print(dict.values()) #valores das chaves
print(dict.keys()) # chaves
print(dict) #valores e chaves

#iterando dicionários
print("---- Dicionário inicial ----")
for key in dict:
    print(f"{key} : {dict[key]}")

#atualizando valores
dict["banana"] = "banana" 
dict.update({"melon":"melância"})

print("---- Dicionário Atualizado ----")
for key in dict:
    print(f"{key} : {dict[key]}") 

#remove item pela chave
dict.pop("apple")

print("---- Dicionário Atualizado ----")
for key in dict:
    print(f"{key} : {dict[key]}") 