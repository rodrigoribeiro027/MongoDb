from bson.objectid import ObjectId

def PegarUsuarios(mydb):
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)
    return mydoc

def UsuariobyID(mydb):
    #Query
    PegarUsuarios(mydb)
    _id =  input(str('escreva seu id do Usuario:'))
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    return mydoc