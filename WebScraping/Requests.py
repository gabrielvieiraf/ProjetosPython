import math, time, json, collections, datetime, base64, html, io, requests, hashlib
from bson.objectid import ObjectId

# Site
# Aqui você deve saber como é a configuração o formulário de autentificação, no meu caso o site era em português.

credentials = {
      "login": "",
      "senha": ""
    }

formHeaders = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

API = ""   # Seu site vai aqui

def getDailyReport():
    session = requests.Session()
    auth = session.post(API, headers=formHeaders, data=credentials, timeout=5)
    assert auth.status_code == 200
    req = session.get(API + "resto do url")
    print(req.text) # Dê uma olhada no resultado :)

#getDailyReport()
