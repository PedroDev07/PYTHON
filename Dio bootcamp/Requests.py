from tkinter.tix import MAIN
from black import main
import requests

response= requests.get('https://viacep.com.br/ws/01001000/json/')
print(response.status_code)

#------------------------------------
print(response.text)
print(type(response.text))
#------------------------------------
print(response.json())
print(type(response.json()))
#------------------------------------
dados_cep = response.json()
print(dados_cep['logradouro'])

