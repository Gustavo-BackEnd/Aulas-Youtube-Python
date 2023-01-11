import pandas as pd
# desafio descobrir quantos cliente cancelaram(churn)

# Passo 1 - Importar base de dados
tabela = pd.read_csv("telecom_users.csv")

# Passo 2 - Visualizar base de dados
tabela = tabela.drop('Unnamed: 0', axis=1) # Excluindo coluna/ axis=0 é linha e 1 para coluna

# Passo 3 - Tratamento de dados
    # Resolver valores que estão sendo reconhecidos de forma
    # Transformando o valor da coluna para numérico
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
    # Resolver valores vazios (Colunas inteiras vazias exclui e linha com pelo menos 1 valor vazio)
tabela = tabela.dropna(how='all', axis=1) # pra todos os valores vazio 'all'
tabela = tabela.dropna(how='any', axis=0) # pra alguns valores vazio 'any'

# Passo 4 - Analise inicial
print(tabela['Churn'].value_counts())# contar os valores da tabela churn(cancelaram)
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))# mostrar em porcentagem

# Passo 5 - Analise detalhada
        # Comparar cada coluna da base  com a coluna Churn
import plotly.express as px  # Biblioteca para criar gráficos
    # Criar gráfico para cada coluna criar um gráfico que mostre os desistentes
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    # Exibir gráfico
    grafico.show()
