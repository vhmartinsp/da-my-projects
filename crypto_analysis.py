#%%
import re
from bs4 import BeautifulSoup
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import requests
from requests.exceptions import HTTPError


#%%
conteudo = None
URL = 'https://finance.yahoo.com/crypto/'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    conteudo = resposta.text  


#%%
pagina = BeautifulSoup(conteudo, 'html.parser')

tabela = pagina.find('table')
if tabela is not None:
    cabecalho = [th.get_text() for th in tabela.find_all('th')]
    linhas = tabela.find_all('tr')
    dados = []

    for linha in linhas[1:]:
        valores = [re.sub(r'\s+', ' ', td.get_text().strip()) for td in linha.find_all('td')]
        dados.append(valores)

    yahoo_crypto_df = pd.DataFrame(dados, columns=cabecalho)
    yahoo_crypto_df.replace(to_replace=[r'\$', r'\%'], value='', regex=True, inplace=True)

    # Comentando a linha de salvamento do arquivo CSV
    arquivo_csv = Path.cwd() / 'yahoo_crypto-limpo.csv'
    yahoo_crypto_df.to_csv(arquivo_csv, mode='w', encoding='utf8', sep=';', index=False)

    # Imprimir o DataFrame diretamente no console
    print(yahoo_crypto_df)

    print("Dados impressos com sucesso!")
else:
    print("Tabela não encontrada na página HTML.")


# %% Tratando os dados das colunas
yahoo_crypto_df.rename(columns={'Symbol': 'symbol'}, inplace=True)
yahoo_crypto_df.rename(columns={'Name': 'name'}, inplace=True)
yahoo_crypto_df.rename(columns={'Price (Intraday)': 'price_day'}, inplace=True)
yahoo_crypto_df.rename(columns={'Change': 'change'}, inplace=True)
yahoo_crypto_df.rename(columns={'% Change': 'change_percent'}, inplace=True)
yahoo_crypto_df.rename(columns={'Market Cap': 'market_value'}, inplace=True)
yahoo_crypto_df.rename(columns={'Volume in Currency (24Hr)': 'volume_currency_24h'}, inplace=True)
yahoo_crypto_df.rename(columns={'Total Volume All Currencies (24Hr)': 'total_volume_currency_24h'}, inplace=True)
yahoo_crypto_df.rename(columns={'Circulating Supply': 'circulating_supply'}, inplace=True)

yahoo_crypto_df.drop(columns = ['Volume in Currency (Since 0:00 UTC)'], inplace=True)
yahoo_crypto_df.drop(columns = ['52 Week Range'], inplace=True)
yahoo_crypto_df.drop(columns = ['Day Chart'], inplace=True)

yahoo_crypto_df['price_day'] = yahoo_crypto_df['price_day'].str.replace(',', '')  # Remover a vírgula
yahoo_crypto_df['price_day'] = yahoo_crypto_df['price_day'].astype(float) # Converte para float
yahoo_crypto_df['change_percent'] = pd.to_numeric(yahoo_crypto_df['change_percent'], errors='coerce')  # Converte para valores numéricos 

filtered_df = yahoo_crypto_df.query('change_percent > 0.00')


# Adicionar rótulos aos eixos do gráfico
plt.figure(figsize=(11, 6))
plt.scatter(filtered_df['market_value'], filtered_df['change_percent'], color='green', alpha=0.7)
plt.xlabel('Valor de Mercado')
plt.ylabel('Mudança Percentual')
plt.title('Relação entre Mudanças Percentuais Positivas e Valor de Mercado')
plt.grid(True)
plt.tight_layout()

# O laço for permitirá  iterar sobre as linhas do DataFrame, retornando o índice da linha (i) e os dados da linha (row) em cada iteração.
for i, row in filtered_df.iterrows():
    plt.annotate(row['name'], (row['market_value'], row['change_percent']),
                 textcoords="offset points", xytext=(0,8), ha='center')
    
# Inverter o eixo x para exibir em ordem crescente, pois o Matplotlib escolhe automaticamente a escala e os limites dos eixos e nesse caso o gráfico viria com o eixo x de forma decrescente.
plt.gca().invert_xaxis()

#Faz a exibição do gráfico 
plt.show()
#%%










