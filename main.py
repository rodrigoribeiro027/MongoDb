from ast import Delete
from unittest import case
import pymongo
from pymongo.server_api import ServerApi
import Usuario.CadastroCliente as CadastroCliente
import Usuario.FindQuery as BuscarUsuario
from bson.objectid import ObjectId
import Usuario.deletar  as DeletarUsuario
import Usuario.update as AtualizacaoUsuario
import Produto.Cadastro as CadastroProduto
import Produto.deletar as DeletarUsuario
import Produto.FindQuery as BuscarProdutos
import Produto.update as AtualizarProdutoByID
import Produto.Cadastro as Comprar

#pip install dnspython
#pip install pymongo
#mongodb+srv://rodrigo:password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://rodrigo:password@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

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




print('''Escolha Uma Opção:\n
  - [1]Comprar\n
  - [2]CadastrarProduto\n
  - [3]CadastrarUsuario\n
  - [4]PegarUsuarios\n
  - [5]UsuariobyID\n
  - [6]DeletarUsuarioID testar\n
  - [7]Atualizar Usuario\n
  - [8]ListaDesejosUsuario testar\n
  - [9]Deletar Produto\n
  - [10]Pegar Produtos\n
  - [11]buscar Produto por ID\n
  - [12]Atualizar Produto por ID\n
''')
escolha = input(str('escolha Uma Obção:'))
match escolha:
    case '1':
      Comprar.Compra(mydb)
    case '2':
      CadastroProduto.CadastrarProduto(mydb)
    case '3':
      CadastroCliente.CadastrarUsuario(mydb)
    case '4':
      BuscarUsuario.PegarUsuarios(mydb)
    case '5':
      BuscarUsuario.UsuariobyID(mydb)
    case '6':
      DeletarUsuario.DeletarUsuarioID(mydb)
    case '7':
      AtualizacaoUsuario.AtualizarUsuarioID(mydb)
    case '8':
      ListaDesejosUsuario() 
    case '9':
      DeletarUsuario.DeletarUsuarioID(mydb)
    case '10':
      BuscarProdutos.PegarProdutos(mydb)
    case '11':
      BuscarProdutos.ProdutosbyID(mydb)
    case '12':
      AtualizarProdutoByID.AtualizarProdutoID(mydb)
