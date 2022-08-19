import pandas as pd

#DataFrame é um tabela em Python
vendas = {'data': ['15/07/2021', '16/02/2021'], 'valor': [500, 300], 'qtde': [50, 70]}

vendas_df = pd.DataFrame(vendas)

#--------------------------------------------------------------------------------------

#MÉTODOS PARA VISUALIZAR TABELAS

#Exibe as primeiras 10 linhas
print(vendas_df.head(10))

#Exibe a quantidade de linhas e colunas
print(vendas_df.shape)

#Exibe resumo dos dados da tabela
print(vendas_df.describe())

#Recupera os dados das duas colunas passadas
itens = vendas_df[['Produto', 'ID loja']]

#Exibe linhas específicas de uma tabela, no casa da linha 1 até a 5
print(vendas_df.loc[1:5])

#Exibir linhas específicas que esteja de acordo com a condição, exemplo abaixo: me traga todas as linhas onde a coluna ID loja seja igual a Norte Shopping
print(vendas_df.loc[vendas_df['ID loja'] == 'Norte Shopping'])

#Exibe uma linha expecífica
print(vendas_df.loc[1, 'Produto'])

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#ADICINAR VALORES

#Criando uma coluna a partir de outra que já existe, da forma abaixo se já existir a colunas ele subistitui pelos novos valoes, se não ele cria.
nova_coluna = vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05
print(nova_coluna)

#Criando uma coluna com um valor fixo, o ' : ' quer dizer tudo, no caso todas as linhas
nova_coluna_fixa = vendas_df.loc[:, "Imposto"] = 0
print(nova_coluna_fixa)

#Adicionando linhas, imagine que eu tenha uma tabela de vendas até novembro e tenho uma outra tabela que contém as vendas de dezembro, como faço pra juntar as duas?
vendas_dezembro = pd.read_excel('Venda - Dez.xlsx')
print(vendas_dezembro)

vendas_df = vendas_df.append(vendas_dezembro)
print(vendas_df)

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#EXCLUIR VALORES

#exclua a coluna Imposto, o "axis" é o Eixo. Eixo 1 é coluna, eixo 0 é linha.
vendas_df = vendas_df.drop("Imposto", axis= 1)

#exclua a primeira linha, linha 0 eixo 0, se não for passado o eixo, vai ser tentado exluir uma linha.
vendas_df = vendas_df.drop(0, axis = 0)

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#TRATATIVAS 

#Excluir linhas completamente vazias 'Nan'
vendas_df = vendas_df.dropna(how='all')

#Excluir todas as colunas com os valores completamente vazios 'Nan'
vendas_df = vendas_df.dropna(how='all', axis = 1)

#Excluir linhas que contenham pelo menos um valor 'Nan'
vendas_df = vendas_df.dropna()

#Preencher valores vazios com o primeiro valor acima
vendas_df = vendas_df.ffill()

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#MÉTODOS

# -Values Counts

#contador de valores, imagine que vc tem uma tabela de transações de várias lojas(cada vez que uma loja faz uma venda essa transação é adicionada na tabela )
#e eu quero saber quando quantas transações eu tenho por loja.

transacoes_loja = vendas_df['ID Loja'].value_counts()
print(transacoes_loja)

# -Groupby

# Ex.: agrupa todos os registro de cada loja pelo produto em apenas um linha e some todos os valores.
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum
print(faturamento_produto)


#- Merge
#Ex.: quero mesclar uma tabela que tem os gerentes e suas lojas com a tabela de transções por lojas, já relacionando cada gerente com cada loja.
#Esse relacionamento só é possível pq em ambas as tabelas tem a coluna "Id Loja", que serve como "chave_primária" e o pamdas já entende.
gerentes_df = pd.read_excel('Gerentes.xlsx')

vendas_df = vendas_df.merge(gerentes_df)

#--------------------------------------------------------------------------------------