import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import ListaCase as ListaUsuario

#pip install dnspython
#pip install pymongo
#mongodb+srv://rodrigo:password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://rodrigo:Password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

global mydb
mydb = client.mercado_Livre

execucao = True
while execucao:
  print('''Escolha Uma Opção:\n
- [0]Parar Aplicacão\n
- [1]Menu Comprar\n
- [2]Menu Usuario\n
- [3]Menu Produto\n
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
    

