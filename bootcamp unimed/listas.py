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