from bson.objectid import ObjectId

def PegarCompras(mydb):
    mycol = mydb.Compra
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)
    return mydoc

def ComprasbyID(mydb):
    PegarCompras(mydb)
    _id =  input(str('escreva seu id da Compra:'))
    mycol = mydb.Compra
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    return mydoc
