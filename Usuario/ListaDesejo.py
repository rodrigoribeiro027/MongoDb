from bson.objectid import ObjectId
import Usuario.FindQuery as buscaUser
import Produto.FindQuery as Buscar

def ListaDesejos(mydb):
    buscaUser.PegarUsuarios(mydb)
    Usuario =  input(str('Escreva Numero Do ID do USuario:'))
    Buscar.PegarProdutos(mydb)
    Produto  =  input(str('Escreva seu id do Produto que deseja Salvar:'))

    mycol = mydb.usuario
    mycol2 = mydb.Produtos
    mydoc = mycol.find_one({"_id":ObjectId (Usuario)})
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    
    
    newvalues = { "$push": {
    "lista_Desejo":mydoca
    }
    }
    print("\n#### lista de desejos Atualizada Com Sucesso. ####") 
    filter = { "_id":ObjectId (Usuario) }
    mycol.update_one(filter,newvalues)
    for x in mycol.find():
        print(x) 
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
                ListaDesejos(mydb)
            case '2':
                return