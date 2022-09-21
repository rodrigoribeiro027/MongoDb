import Usuario.FindQuery as Procurar
import Produto.FindQuery as ProcurarProduto
from bson.objectid import ObjectId

def Compra(mydb):
    mycol = mydb.Compra
    mycol2 = mydb.Produtos
    mycol3= mydb.usuario
    Procurar.PegarUsuarios(mydb)
    Usuario =  input(str('escreva seu id do Usuario:'))
    ProcurarProduto.PegarProdutos(mydb)
    Produto  =  input(str('escreva seu id do Produto:'))

    mydoc = mycol3.find_one({"_id":ObjectId (Usuario)})
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    preco = mydoca["Preco"]
    vendedor = mydoca["Vendedor"]
    NomeVendedorid = vendedor["NomeVendedor"]
    Telefone = vendedor["Telefone"]
    
    mydict = {
        "Usuario_ID":{"_id":ObjectId (Usuario) },
        "Produto_ID":{"_id":ObjectId (Produto) },
        "Total_Compra":mydoca["Nome"],
        "Preco":preco,
        "NomeVendedor":NomeVendedorid,
        "Telefone":Telefone,
    }
    print(mydict)
    print("\n ##### insert Compra Inserido ###")

    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    execucao = True
    while execucao:
        print('''Deseja Continuar Comprando:\n
        - [0]Voltar\n
        - [1]Sim\n
        - [2]Não\n
        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                break
            case '1':
                Compra(mydb)
            case '2':
                return

