print("Programa de bicicletas do joão")

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def Buzinar(self):
        print("BUz bUZ buZ")
    
    def Parar(self):
        print("Parando")
    
    def Correr(self):
        print("Correndo....")

    def __str__(self):
        return f"Bicicleta{self.cor}, {self.modelo}"
    def __str__(self):
        return f"{self.__class__.__name__}"


b1 = Bicicleta("vermelha","Aro 29", 2019, 2000)

b1.Buzinar()
b1.Correr()
b1.Parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)