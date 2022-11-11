#O objetivo é entender o fucnionamento da estrutura de dados lista
#listas em python podem armazenar de maneira sequencial qualquer tipo de objeto.

fruta = ["laranja","maca","uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

#Criação de tupla
#Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutaveis.
#podemos criar tuplas atravs da classe tuple(), ou colocando valores separados por virgula entre parenteses.

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("brasil",)

#conjuntos
#Entender o funcionamento da estrutura de dados set.
#Como criar conjuntos
#Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

set([1,2,3,1,3,4])
set("abacaxi")
set(("palio","gol","celta","palio"))
linguagens = {"python","Java","python"}

#Conjuntos em python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter  o conjunto para lista.

#.union()
#.intersection()
#.difference
#.symmetric_difference()
#.issubset()
#.issuperset 
#.isdisjoint
# .add() #remendo
# .copy()
# .dicard()
# .pop()
# .remove()

#Dicionarios
#Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as cgaves são unicas em uma dada instancia do dicionário.
pessoa = {"nome":"Guilherma", "idade":28}
pessoa = dict(nome="Guilherme", idade=28)
pessoa["Telefone"] = "3333-1234"

#for chave, valor in contatos.items():
    #print(chave,valor)

#metodos 
# .clear()
# .copy()
# .fromkeys([])
# .get
# .items()
# .keys()
# .pop()
# .popitem()
# .setdefault()
# .update({})
# .values()
# in (Pecorre as listas, dicionarios e etc)
# del 
#trabalhando com funções
#Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâemtros podem ou não ter valores padrões

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print("Seja bem vindo{}!".format(nome))

def exibir_mensagem_3(nome="Isaque"):
    print("SejaBem vindo{}".format(nome))

def calcular_total(numeros):
    return sum(numeros)
calcular_total(numeros=[10,20])

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor
retorna_antecessor_e_sucessor(numero=10,)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="", modelo= "" , ano=2002 , placa="")
# ** dois pontos significa que você está passando um dicionário
# args e kwargs
# ags vem em tupla e kwargs retorna em dicionário
#  argumentos por posição / argumentos declarados (carro="uno")
#(*, obriga a nomear o argumento )

