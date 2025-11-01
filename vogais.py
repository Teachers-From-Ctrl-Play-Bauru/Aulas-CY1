listaString = []
while True: 
    string = input()
    if(string != ""):
        listaString.append(string.lower)
    else:
        break

for string in listaString:
    contador = 0
    for s in string:
        if(s == "a" or s == "e" or
           s == "i" or s == "o" or
           s == "u"):
            contador+=1
    print(string + " "+str(contador))
