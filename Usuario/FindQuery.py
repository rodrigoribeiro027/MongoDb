from bson.objectid import ObjectId

def PegarUsuarios(mydb):
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)

def UsuariobyID(mydb):
    #Query
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "_id":ObjectId ("6321b71fe575e852c80aa762") }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)