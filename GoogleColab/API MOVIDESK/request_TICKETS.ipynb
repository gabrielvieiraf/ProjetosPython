import requests
import json
from datetime import date

URL_API = 'https://api.movidesk.com/public/v1/tickets?'
TOKEN_API = "token= SUA CHAVE AQUI"
ID_TICKET = "&id=1"
LISTA_TICKETS = "&$select=id,status"
LISTA_SERVICOS = "&$expand=owner"

from IPython.display import HTML, display

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))

get_ipython().events.register('pre_run_cell', set_css)

# Lógica para pegar a data e reconhecer o primeiro dia do mês atual.
data_atual = date.today()
data = '{}-{}-{}'.format(data_atual.year,data_atual.month,data_atual.day)
inicio_mes = '{}-{}-{}'.format(data_atual.year,data_atual.month,'01')

FILTRO_DATA = ",createdDate&$filter=createdDate gt " + inicio_mes + "T00:00:00.00z&$orderby=id"

print("Acessando:",end='')
print(URL_API + TOKEN_API + LISTA_TICKETS + LISTA_SERVICOS + LISTA_SERVICOS ,end='\n\n')
print("Janela do evento:",end= inicio_mes + ' até ')
print(data,end="\n\n")

response = requests.get(URL_API + TOKEN_API + LISTA_TICKETS +  FILTRO_DATA + LISTA_SERVICOS )
response_JSON = response.json()

for i in range(len(response_JSON)):
  try:
    print(response_JSON[i])
  except:
    print("Erro na requisição")

print("\nQuantidade de Tickets:")
print(len(response_JSON))
