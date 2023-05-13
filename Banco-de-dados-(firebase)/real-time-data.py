import requests
import json
# from python_lib.functions import plate_database

link = 'https://mapvision-2-default-rtdb.firebaseio.com/'

# para criar uma informação no banco de dados usamos o comando requests.post()
# para pegar uma informação no banco de dados usamos o comando requests.get()

requisicao = requests.get(f'{link}/plates/.json')
# print(requisicao.text)
dic_requisicao = requisicao.json()
print(dic_requisicao)

for id_placas in dic_requisicao:
    placa = dic_requisicao[id_placas]
    if placa == "RDB2I1":
        print("Plate:{0} \nID:{1}".format(placa,id_placas))
        break
    else:
        pass
        


# plate_database()