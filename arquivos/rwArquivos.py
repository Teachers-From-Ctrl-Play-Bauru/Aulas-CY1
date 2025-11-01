with open("meuArquivo.txt", "r", encoding="utf-8") as file:
    conteudo = file.read()
    print(conteudo)

try:
    with open("meuArquivo1.txt", "r", encoding="utf-8") as file:
        conteudo = file.read()
        print(conteudo)
except FileNotFoundError:
        print("O arquivo não existe, criando agora")
        open("meuArquivo1.txt", "w")


    

