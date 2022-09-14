global mydb
from bson.objectid import ObjectId

def DeletarUsuarioID(mydb):
    mycol = mydb.Produtos
    print("\n#### Usuario Deletado do Banco####") 
    filter = { "_id":ObjectId ("6322508fa480134c8bd68ebc") }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)  