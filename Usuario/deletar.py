global mydb
from bson.objectid import ObjectId

def DeletarUsuarioID(mydb):
    mycol = mydb.usuario
    print("\n#### Usuario Deletado do Banco####") 
    filter = { "_id":ObjectId ("63224677762a6a0b03a44c16") }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)  