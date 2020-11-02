import pandas as pd

# Permite Importar dados do Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Caminho para dados do arquivo csv 
csv = '/content/drive/My Drive/Colab Notebooks/Alura/aluguel.csv'
dados = pd.read_csv(csv, sep = ";")
dados.head(10)

# Método para filtrar NaN numbers e tranformar em 0
dados = dados.fillna(0)

# Utilizando método query

# Casas com valor do Aluguel abaixo de 5000
dados.query("Valor < 5000 & Tipo == 'Casa'")

# Média do aluguel de casas
dados.query("Tipo == 'Casa'").Valor.mean()

# Tipos de Moradias
Tipos = sorted(tipos_de_dados.unique())

# Cria coluna para Tipos de dados
tipos_de_dados = pd.DataFrame(dados.dtypes, 
    columns = ['Tipos de Dados'])

# Cria coluna para as variáveis no index
tipos_de_dados.columns.name = 'Variáveis'
# Imprime Tipos de Dados
tipos_de_dados

# Importando dados HTML
df_html = pd.read_html('https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F01l_jz&gl=BR&ceid=BR%3Apt-419', decimal=",")
# Seleciona primeira Tabela do site
df_html[0]
# Remove Coluna
df_html = pd.DataFrame(df_html[0]).drop(columns=['Novos casos (Ãºltimos 60 dias)'])
# Renomeia Coluna
df_html = df_html.rename(columns={"Casos a cada um milhÃ£o de pessoas": "Casos a cada 1M de pessoas"})
# Imprime DataFrame
df_html
