#importando as bibliotecas 
import pandas as pd
import matplotlib.pylot as plt
plt.style.use("seaborn")

#upload do arquivo 
from colab import files 
arq = files.upload()

#Criando dataframe
df = pd.read_excel("AdventureWorks.xlsx")

#Visualizando as 5 primeiras linhas 
df.head()

#quantidade de linhas e colunas
df.shape()

#Verificando os tipos de dados
df.dtypes

#Qual a receita total
df["Valor Venda"].sum()

#Qual o custo total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #criando a coluna de custo
df.head(1)

#Qual o custo total?
round(df["custo"].sum(), 2)

#Achando o lucro total
df["lucro"] = df["Valor Venda"] - df["Custo"]
df.head(1)

#Lucro Total
round(df["lucro"].sum(),2)

#Criando  uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
df.head(1)

#Tempo de envio para cada marca
#extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
df.head(1)

#Verificano o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

#Média do tempo de envio por marca
df.groupby("Marca")["Tempo_envio"].mean() #a média

#Verificar se existe valores ausentes 
df.isnull().sum()

#Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year,"Marca"])["Lucro"].sum()
pd.options.display.float_format ='{:20,.2f}'.format

#resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year,"Marca"])["Lucro"].sum().reset_index()
lucro_ano

#qual o total de produtos vendidos?
df.groupby("Produtos")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico total de produtos vendidos
dfgroupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")

#lucro por ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

#Selecionando as vendas para apenas 2009    
df_2009= df[df["Data Venda"].dt.year == 2009]
df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro X Mês")
plt.xlabel = ("Mês")
plt.ylabel = ("Lucro")

df_2009.groupby("Marca")["Lucro"].sum().plot(title="Lucro X Marca")
plt.xlabel = ("Marca")
plt.ylabel = ("Lucro")
plt.xticks(rotation= 'horizontal')

df_2009.groupby("Classe")["Lucro"].sum().plot(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

df["Tempo_envio"].describe()

#Gráfico de boxplot
plt.boxplot(df["Tempo_envio"])

#Histograma
plt.hist(df["Tempo_envio"])

#Tempo minimo de envio 
df["Tempo_envio"].min()
df["Tempo_envio"].max()

#identificando o Outlier 
df[df["Tempo_envio"]== 20]

df.to_csv("df_vendas_novo.csv", index=False)
#fim






