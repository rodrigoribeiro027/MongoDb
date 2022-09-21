global mydb
from bson.objectid import ObjectId
import Compra.FindQuery as BuscarCompras

def DeletarCompraID(mydb):
    BuscarCompras.PegarCompras(mydb)
    _id =  input(str('escreva seu id do Compra:'))
    mycol = mydb.Compra
    print("\n#### Compra Deletada do Banco ####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)  
    execucao = True
    while execucao:
            print('''Deseja Continuar Cancelando as Compras:\n
            - [0]Voltar\n
            - [1]Sim\n
            - [2]Não\n
            ''')
            escolha = input(str('Escolha Uma Obção:'))
            match escolha:
                case '0':
                    return
                case '1':
                    DeletarCompraID(mydb)
                case '2':
                    return