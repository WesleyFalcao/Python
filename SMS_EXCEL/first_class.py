import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC74f1b01136aba2e41647854c5c38194c"
# Your Auth Token from twilio.com/console
auth_token  = "3e83e9743e1de20cf3e1d90f4d3e5ec6"
# Connection
client = Client(account_sid, auth_token)


list_docs = ['document1', 'document2', 'document3', 'document4']

for doc in list_docs:
    table = pd.read_excel(f'{doc}.xlsx')
    if (table['DATA'] < 2022).any():
        localidade = table.loc[table['DATA'] < 2022, 'Município_UF'].values[0]
        idade = table.loc[table['DATA'] < 2022, 'IDADE'].values[0]
        print(f'No arquvio: {doc} ,tem uma data menor que 2022, localidade: {localidade}, idade: {idade}')
        message = client.messages.create(
            to="+5528999533290", 
            from_="+18787686189",
            body=f"No arquvio: {doc} ,tem uma data menor que 2022, localidade: {localidade}, idade: {idade}")
        print(message.sid)