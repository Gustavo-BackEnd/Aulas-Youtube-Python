import pandas as pd
from twilio.rest import Client

account_sid = "ACe4038fda0465aa2653bc48278ba89f6f"
auth_token  = "6cbefd52640757399c1870d12e34ebb7"
client = Client(account_sid, auth_token)

# Passo a passo de solução:
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

# Verificar se algum valor na coluna Vendas é maior que 55.000,00
    if (tabela_vendas['Vendas'] > 50000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 50000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 50000, 'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor {vendedor} vendeu um valor de {vendas}')

# Se for maior que 55.000,00 envia um SMS com o nome, o mês e o valor das vendas do vendedor
        message = client.messages.create(
        to="+5511997080572",
        from_="+16802103936",
        body=f"No mês de {mes} o vendedor {vendedor} vendeu um valor de {vendas}")

        print(message.sid)