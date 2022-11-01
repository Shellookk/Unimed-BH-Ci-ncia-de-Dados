#importa a biblioteca
import pandas as pd

#leitura dos arquivos
df1 = pd.read_excel
df2 = pd.read_excel
df3 = pd.read_excel
df4 = pd.read_excel
df5 = pd.read_excel

#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#exibindo as 5 primeiras linhas
df.head()

#exibindo as ultimas 5 linhas
df.tail()

#verificando o tipo de cada coluna
df.dtypes()

#alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("objetc")
df.dtypes

df.head()
#Tratando de valores faltantes
#Consultando linhas com valores faltantes
df.isnull().sum()

#substituindo os valores nulos pela média
df["vendas"].fillna(df["Vendas"].mean(), inplace=True)
df["vendas"].mean()
df.isnull().sum()

#substituindo os valores nulos por zero
df["vendas"].fillna(0, inplace=True)
df["vendas"].mean()
df.isnull().sum()

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["vendas"], inplace=True)

#removendo linhas que estejam com valores faltantes em todas as colunas 
df.dropna(how="all", inplace=True)

#Criando colunas novas

#criando a coluna de receita
df["receitas"] = df["vendas"].mul(df["Qtde"])
df.head()
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
df.head()
#Retornando a maior receita
df["Receita"].max()
#Retornando a menor receita
df["Receita"].min()
#nlargest retornar as 3 linhas com maiores receitas
df.nlargest(3,"Receita")
#nsamllest retornar as 3 linhas com menores receitas
df.nsmallest(3,"Receita")
#Agrupamento por cidade 
df.grouppby("Cidade")["Receita"].sum()

#ordenando o conjunto de dados
df.sort_values("Receita",ascending=False).head(10)

#Trabalhando com datas

#Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#verificando o tipo de dado de cada coluna
df.dtypes

#transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])
df.dtypes

#Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year
df.sample(5)

#Extraindo o Mes e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month,df["Data"].dt.day)
df.sample(5)

#retornando a data mais antiga
df["Data"].min()

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
 
#crianco a coluna de trimestre

#filtrando as vendas de 2019do mês de março
vendas_maco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.moth ==3)]
vendas_maco_19