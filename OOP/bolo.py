class Bolo:
    #função chamada ao instanciar a classe
    def __init__(self, graus, tempo, sabor, ovos, leite, farinha, acucar):
        self.graus = graus
        self.tempo = tempo
        self.sabor = sabor
        self.ovos = ovos
        self.leite = leite
        self.farinha = farinha 
        self.acucar = acucar

    def fazerBolo(self):
        self.misturarMassa()
        self.assarBolo()


    def misturarMassa(self):
        print(f"---Misturando Líquidos---")
        print(f"{self.leite} ml de leite")
        print(f"{self.ovos} ovos")
        print(f"Adicionando {self.acucar} gramas de açucar")
        print(f"Adicionando {self.sabor}")
        print(f"Adicionando {self.farinha} gramas de farinha")

    def assarBolo(self):
        print(f"Assando bolo por {self.tempo} minutos, à {self.graus} graus ")
    
    
    pass

bolo_choco = Bolo( graus = 220, tempo= 180, sabor = "Chocolote",
                   ovos= 3, leite = 200, farinha = 400, acucar = 150) #instanciando classe bolo
bolo_morango = Bolo(graus = 220, tempo= 120, sabor = "Morango",
                   ovos= 4, leite = 250, farinha = 400, acucar = 200)

bolo_choco.fazerBolo()
bolo_morango.fazerBolo()