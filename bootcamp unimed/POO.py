#Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. 
# já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

#exemplo de uma class
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome 
        self.cor = cor 
        self.acordado = acordado

    def latir(self):
        print("Auau")
    def dormir(self):
        self.acordado = False
        print("ZZZZzzzz")

cao1 = Cachorro("Dog", "Preto", False )
cao2 = Cachorro("Nasus","Branco")

cao1.latir()
cao2.latir()

cao1.dormir()
