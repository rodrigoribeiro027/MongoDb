from bson.objectid import ObjectId

def PegarProdutos(mydb):
    mycol = mydb.Produtos
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)
    return mydoc

def ProdutosbyID(mydb):
    #Query
    PegarProdutos(mydb)
    _id =  input(str('escreva seu id do Produto:'))
    mycol = mydb.Produtos
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find_one(myquery)
    print(mydoc)
    return mydoc