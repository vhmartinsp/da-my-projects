#%%
import requests
from requests.exceptions import HTTPError
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
from pathlib import Path

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


# %% Trantando os dados das colunas
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
yahoo_crypto_df['price_day'] = yahoo_crypto_df['price_day'].astype(float) #Converte para float
yahoo_crypto_df['change_percent'] = pd.to_numeric(yahoo_crypto_df['change_percent'], errors='coerce')  #Converte para valores numéricos 

filtered_df = yahoo_crypto_df.query('change_percent > 0.00')
# %%

# Plotar o gráfico de dispersão com a escala de cores aplicada pela coluna "change_percent"

sns.scatterplot(data=filtered_df, x="price_day", y="change_percent", hue="name", palette="viridis", alpha=0.7)

# Adicionar rótulos aos eixos
plt.title("Relação entre variação percentual e o preço do dia por crypto")
plt.xlabel('Preço do Dia')
plt.ylabel('Variação Percentual')
plt.legend(title="Nome da moeda")


# Exibir o gráfico  
plt.show()



# %%
