global mydb
from bson.objectid import ObjectId

def AtualizarProdutoID(mydb):
    mycol = mydb.Produtos
    print("\n#### Usuario Atualizado no Banco####") 
    filter = { "_id":ObjectId ("6322541a6456f65039f6687e") }
    newvalues = { "$set": {
    "Nome":"Xbox",
    "Data_Produto":"Fri Jan 07 2000 00:00:00 GMT-0200 (Hora de verão de Brasília)",
    "Descricao":"Core I3 4Gb 1Tb - 15,6Hd","Preco":"3500","Quantidade_Estoque":"12",
    "Vendedor":{"Vendedor":"Mercado Livre","ID":{"$oid":"630f42a739b7d96c7564173a"}}}
    }
    mycol.update_one(filter,newvalues)

    for x in mycol.find():
        print(x)  