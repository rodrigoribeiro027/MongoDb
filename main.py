from unittest import case
import pymongo
from pymongo.server_api import ServerApi

#pip install dnspython
#pip install pymongo

client = pymongo.MongoClient("mongodb+srv://Usuario:'Passoword'@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

global mydb
mydb = client.mercado_Livre

def CadastrarUsuario():
    global mydb
    mycol = mydb.usuario
    print("\n #####insert Usuario Inserido ###")
    mydict = {
    "Nome":"Rodrigo Ribeiro Dos Santos",
    "Data_Nascimento":"2000-10-10",
    "Email":"Rodrigo.rsantos80@gmail.com","Telefone":"123914545","Cpf":"121.845.123-77",
    "lista_Desejo":[{"Produto_ID":{"id":"630f45304b88272631990c17"},
    "Nome":"Rodrigo Ribeiro ","Preco":"3500"},{"Vendedor_ID":{"$oid":"630f458c4b88272631990c18"},
    "Nome":"Mercado livre","Telefone":"1239256454"}],"Cidade":"Sp","Endereco":"Rua joaquim andrade n123"
}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def CadastrarProduto():
    global mydb
    mycol = mydb.Produtos
    print("\n #####insert Produto Inserido ###")
    mydict = {
        "Nome":"Notebook Intel",
        "Data_Produto":"Fri Jan 07 2000 00:00:00 GMT-0200 (Hora de verão de Brasília)",
        "Descricao":"Core I3 4Gb 1Tb - 15,6Hd","Preco":"3500","Quantidade_Estoque":"12",
        "Vendedor":{"Vendedor":"Mercado Livre","ID":{"$oid":"630f42a739b7d96c7564173a"}}}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def Compra():
    global mydb
    mycol = mydb.Compra
    print("\n #####insert Compra Inserido ###")
    mydict = {"Usuario_ID":{"ID":{"$oid":"630e96c226d1f4b1ba9c5787"},
    "Nome":"Rodrigo Ribeiro Dos Santos","Email":"Rodrigo.rsantos70@gmail.com",
    "Cpf":"123912-2121","Cidade":"SP","Endereco":"Rua joaquim andrade n123"},
    "Produto_ID":[{"id":{"$oid":"630df511ce8a5651c630916a"},
    "Nome":"Notebook Intel","Preco":"6300","Quantidade":"1"}],
    "Vendedor_ID":{"ID":{"$oid":"630e964d26d1f4b1ba9c5786"},
    "Nome":"Mercado livre","Cpf/Cnpj":"423.878.888-99"},
    "Total_Compra":{"Total":"1000",
    "Data_Compra":"10/02/2000"}
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


print('''Escolha Uma Opção:\n
  - Comprar\n
  - CadastrarProduto\n
  - CadastrarUsuario\n
''')
escolha = input(str('escolha Uma Obção:'))
match escolha:
    case 'Comprar':
      Compra()
    case 'CadastrarProduto':
      CadastrarProduto()
    case 'CadastrarUsuario':
      CadastrarUsuario()
      