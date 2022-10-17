import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import ListaCase as ListaUsuario
import redis

#pip install dnspython
#pip install pymongo
#mongodb+srv://rodrigo:password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://rodrigo:senha@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
conR = redis.Redis(host='redis-11226.c246.us-east-1-4.ec2.cloud.redislabs.com',
                  port=11226,
                  password='senha')
global mydb
mydb = client.mercado_Livre

execucao = True
while execucao:
  print('''Escolha Uma Opção:\n
- [0]Parar Aplicacão\n
- [1]Menu Comprar\n
- [2]Menu Usuario\n
- [3]Menu Produto\n
- [4]Menu Redis\n
''')
  escolha = input(str('escolha Uma Obção:'))
  match escolha:
      case '0':
          break
      case '1':
        ListaUsuario.CaseCompra(mydb)
      case '2':
          ListaUsuario.CaseUsuario(mydb)
      case '3':
          ListaUsuario.CaseProduto(mydb)
      case '4':
        ListaUsuario.Caseredis(mydb,conR)

