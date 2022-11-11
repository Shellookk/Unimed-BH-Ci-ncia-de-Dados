#o que seria um etl
#  ETL é um tipo de data integration em três etapas (extração,transformação,carregamento) usado para combinar dados de diversas fontes. ele é comumente utilizado para construir um data warehouse.

# Extratc (Extrair)
# - Importar dados de diversos tipos e formatos como:
# pasta de trabalho, diversos banco de dados, scv, txt, json, etc.

# Transform (Transformar):
# -colunas,linhas
# Tipos de dados
# mesclar, acrescentar
# Listas, tabelas

# Load (Carregar)
# - Para o modelo de dados

# 1 - extração de dados:
# O processo de extração de dados consiste em se comunicar com outros sistemas ou bacnos de dados para capturar os dados que serão inseridos no destino, seja uma staging area ou outro sistema

# 2- transformação:
# O processo de transformação de dados é composto por várias etapas: padronização,limpeza,qualidade. dados vindos de sistemas diferentes tem padrões diferentes seja nomenclatura ou mesmo de tipos
# de dados (VARCHAR2 Oracle ou VARCHAR Sql server).

# 3- Processo de carregamento:
# O processo de Load é a etapa final onde os dados são lidos das areas de staging e preparação de dados, carregados no data warehouse ou data mart final. 

# Algumas vantagens para ETL
# Garantia significativa da qualidade dos dados
# A ferramenta de ETL, através de sequencias de operações e instruções tem condições de solucionar problemas de maior complexidade.

# Vantagens para ETL
# - Garantia sifnificativa da qualidade dos dados
# - Funcionalidade de execução
# - Desenvolvimento das cargas 
# - Manutenção das cargas
# - metainformação:
# os metadados (Informações uteis para identificar, localizar, entender e gerenciar os dados )
# são gerados e mantidos de forma automática com a ferramenta, evitando problemas de geração de informações incorretas na finalização do processo.

# -performace:
# OS métodos mais usados para trabalhar com grandes volumes conseguem extrair, transofrmar e carregar dados com maior velocidade e menos recursos,  como gravações em bloco e operações não logadas.

# Transferencia:
# ferramentas de ETl podem ser deslocadas de um servidor mais facilmente ou distruibuidas entre vários servidores.

# conectividade:
# A conexão de uma ferramenta de ETL com multiplas fontes de dados é transparente. Caso sejam precisas mais fontes como o SAP,VSAM, ainframe ou qualquer outra,
# basta a aquisição do conector sem a necessidade de codificar um.

# Reinicialização:
# pode reiniciar a carga de dados de onde parou

# Segurança e estabilidade:


# Ferramentas utilizadas:
# As ferramentas são softwares utilizados para facilitar o processo de itnegração de dados. Inicialmente muito usados em projetos de data WareHouse e Business Intelligence em geral, ultimamente 
# tem sido utilizados em processos de integração de software, bancos de dados, etc.

# IBM data stage 
# POwer ConnectionErrorSQl server integration
# Talend ETL 

# ETL para BIG DATA 
# SQOOP - Ferramenta para movimentar dados dentre bancos de dados relacionais e o ambiente Hadoop
# HIVE - Ambiente de SQL sobre um cluster Hadoop
# PIG - Ferramenta de script para transofrmação e processamento de dados.
# SPARK - framework de processamento em memória.

# Hadoop é uma plataforma de software em java de computação distribuida voltada para clusters e processamento de grandes volumes de dados, com atençaõ a tolerância a falhas.

#Serie é uma matriz unidimensional que contem uma sequenia de valores que apresentam uma indexação(que podem ser numéricos inteiros ou rotulos)
#DataFrame é uma estrutura de dados tabular, semelhante a planilha de dados do excel, em que tanto as linha quanto as colunas apresentam rotulos.

# Dataframe

# df.head(n=4)
# df.shape #retorna oque tem na planilha(linhas e colunas)
# df.info() #retorna quais dados tem na planilha
# df.isnull().sum() #retorna dados faltantes em nosso conjunto    
# df['setor'].unique() #retorna dados unicos no conjuto
# df['setor'].value_counts().plot(kind='bar')
 
#Biblioteca Scikit-learn
# from sklearn.datsets import make_regression 
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
#gerando uma massa de dados:
# x, y = make_regression(n_samples=200,n_features=1,noise=30) 
#mostrando no gráfico:
# plt.scatter(x,y)
# plt.show() 
#Criação do modelo
# modelo = LinearRegression()

# modelo.predict(x)
# plt.scatter(x,y)
# plt.plot(x, modelo.predict(x), color ='red', linewidth=3) 
# plt.show() 


#pandas 
#import pandas as pd
#url = ''
#df1 = pd.read_csv('url')

#url2 = 'url'
#sf = pd.read_csv(url2)
#salaries CSV
#sf.head()

# Framework luigi para etl com python
# task:
# require() - está função membro da classe tas contém todas as instâncias de tarefas que devm ser executdas antes da tarefa atual.
# output() - Este métoodo contém o destino ontem a saída da tarefa será armazenada. Isso pode conter um ou mais objetos de destino.
# run() - Esté método contém a lógica real para executar uma tarefa.
#obs: entrar no localhost:8082