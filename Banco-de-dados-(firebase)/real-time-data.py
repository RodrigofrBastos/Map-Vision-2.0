import requests
import json

link = 'https://mapvision-2-default-rtdb.firebaseio.com/'

# para criar uma informação no banco de dados usamos o comando requests.post()
# para pegar uma informação no banco de dados usamos o comando requests.get()

requisicao = requests.get(f'{link}/.json')

print(requisicao)
print(requisicao.text)