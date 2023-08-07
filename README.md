# Projeto de Web Crawling e Scraping para Análise de Criptomoedas no Yahoo Finance

Este é um projeto focado na coleta de dados e análise de informações sobre criptomoedas usando as bibliotecas requests, pandas, seaborn, matplotlib, e BeautifulSoup. O principal objetivo é extrair dados relevantes do Yahoo Finance, criar um DataFrame para análise e gerar gráficos interativos que ilustram a relação entre os preços diários e as variações percentuais positivas das criptomoedas.

## Funcionalidades:

- Utiliza a biblioteca requests para coletar informações atualizadas das criptomoedas no Yahoo Finance.
- Faz uso da biblioteca BeautifulSoup para realizar o parsing e scraping das páginas.
- Cria um DataFrame utilizando a biblioteca pandas para facilitar a manipulação e análise dos dados.
- Gera gráficos interativos usando as bibliotecas seaborn e matplotlib para visualizar a relação entre preços e variações percentuais.
- Filtra e destaca as criptomoedas com variação percentual positiva, oferecendo uma visão rápida das performances favoráveis.
- Apresenta uma legenda colorida no gráfico, associando cores a cada criptomoeda.

## Como Usar

Máquina Local
1. Faça o clone deste repositório para sua máquina local.
2. Instale as bibliotecas necessárias listadas no arquivo `requirements.txt` utilizando o comando: `pip install -r requirements.txt`.
3. Execute o script principal `crypto_analysis.py` para iniciar a coleta de dados e geração dos gráficos.
4. O DataFrame gerado estará disponível para análise e manipulação no código.
5. O gráfico interativo será exibido na interface gráfica usando as bibliotecas seaborn e matplotlib.

Google Colab
1. Faça o download do crypto_analysis.ipynb para seu ambiente no Google Drive (clicando no botão de download no canto direito).
2. Abra o Google Colab, caso tenha conta faça o login, senão faça o cadastro na plataforma.
3. Clique em arquivo no canto superior esquerdo e então vá em "Fazer upload de Notebook.
4. Navegue até o diretório onde o notebook foi baixado e então faça o upload dele.
5. Conecte o novo ambiente de execução, clicando no botão conectar no canto superior direito do Google Colab.
6. Execute cada célula.

## Observações

- Certifique-se de estar conectado à internet durante a execução, uma vez que o Web Crawling requer acesso ao Yahoo Finance.
- Este projeto foi desenvolvido com propósitos educacionais, enfatizando a compreensão de Web Crawling, Scraping e visualização de dados.
- Contribuições e sugestões são bem-vindas para aprimorar este projeto. Sinta-se à vontade para criar problemas ou solicitações de incorporação.

---

# Web Crawling and Scraping Project for Cryptocurrency Analysis on Yahoo Finance

This is a project focused on collecting data and analyzing information about cryptocurrencies using the `requests`, `pandas`, `seaborn`, `matplotlib`, and `BeautifulSoup` libraries. The main goal is to extract relevant data from Yahoo Finance, create a DataFrame for analysis, and generate interactive charts that illustrate the relationship between daily prices and positive percentage changes of cryptocurrencies.

## Functionalities:

- Makes use of the `requests` library to collect up-to-date cryptocurrency information from Yahoo Finance.
- Makes use of the `BeautifulSoup` library to perform parsing and scraping of pages.
- Creates a DataFrame using the `pandas` library to facilitate data manipulation and analysis.
- Generates interactive charts using the `seaborn` and `matplotlib` libraries to visualize the relationship between prices and percentage changes.
- Filters and highlights cryptocurrencies with positive percentage change, offering a quick view of favorable performances.
- Displays a colored legend on the chart, associating colors with each cryptocurrency.

## How to Use

Local Machine
1. Clone this repository to your local machine.
2. Install the necessary libraries listed in the `requirements.txt` file using the command: `pip install -r requirements.txt`.
3. Run the main script `crypto_analysis.py` to start collecting data and generating graphs.
4. The generated DataFrame will be available for analysis and manipulation in the code.
5. The interactive graph will be displayed in the graphical interface using the `seaborn` and `matplotlib` libraries.

Google Colab
1. Download crypto_analysis.ipynb to your environment from Google Drive (by clicking the download button in the right corner).
2. Open Google Colab, if you have an account log in, otherwise register on the platform.
3. Click on file in the top left corner and then go to "Upload from Notebook.
4. Navigate to the directory where the notebook was downloaded and then upload it.
5. Connect the new runtime environment by clicking the connect button in the top right corner of Google Colab.
6. Run each cell.

## Remarks

- Make sure you are connected to the internet during execution, since Web Crawling requires access to Yahoo Finance.
- This project was developed for educational purposes, emphasizing the understanding of Web Crawling, Scraping and data visualization.
- Contributions and suggestions are welcome to improve this project. Feel free to create issues or incorporation requests.
