from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials
import json

cells = []

gc = gspread.authorize(GoogleCredentials.get_application_default())

sh = gc.open_by_key('SUA KEY DA PLANILHA AQUI')

# Abrindo Planilha na Primeira Página
worksheet = sh.sheet1

# Formatando Lista para JSON
json_format = json.dumps(cells) 

# Atualiza Dados
worksheet.update_cell(1, 1, cells)
