import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import ListaCase as ListaUsuario

#pip install dnspython
#pip install pymongo
#mongodb+srv://rodrigo:password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://rodrigo:senha@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

global mydb
mydb = client.mercado_Livre


def ListaDesejosUsuario():
    global mydb
    mycol = mydb.usuario
    print("\n #####insert Usuario Inserido ###")
    myquery = { "Nome": "Rodrigo Ribeiro Dos Santos" }
    mydict = {
    "lista_Desejo":[{"Produto_ID":{"id":"630f45304b88272631990c17"},
    "Nome":"Rodrigo Ribeiro ","Preco":"3500"},{"Vendedor_ID":{"$oid":"630f458c4b88272631990c18"},
    "Nome":"Mercado livre Brasil","Telefone":"1239256454"}],"Cidade":"Sp","Endereco":"Rua joaquim andrade n123"
}
    mydoc = mycol.find(myquery).insert_one(mydict)
    for x in mydoc:
        print(x)


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
          break
      case '2':
          ListaUsuario.CaseUsuario(mydb)
      case '3':
          ListaUsuario.CaseProduto(mydb)
    

