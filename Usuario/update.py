global mydb
from bson.objectid import ObjectId

def AtualizarUsuarioID(mydb):
    mycol = mydb.usuario
    print("\n#### Usuario Atualizado no Banco####") 
    filter = { "_id":ObjectId ("6321b71fe575e852c80aa762") }
    newvalues = { "$set": {"Nome":"Roberto Ribeiro Dos Santos",
    "Data_Nascimento":"2000-10-10",
    "Email":"Rodrigo.rsantos80@gmail.com",
    "Telefone":"123914545",
    "Cpf":"121.845.123-77",
    "lista_Desejo":[{"Produto_ID":{"id":"630f45304b88272631990c17"},
    "Nome":"Rodrigo Ribeiro ","Preco":"3500"},
    {"Vendedor_ID":{"$oid":"630f458c4b88272631990c18"},
    "Nome":"Mercado livre","Telefone":"1239256454"}],
    "Cidade":"Sp","Endereco":"Rua joaquim andrade n123"}
    }
    mycol.update_one(filter,newvalues)

    for x in mycol.find():
        print(x)  