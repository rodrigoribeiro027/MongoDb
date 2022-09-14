from bson.objectid import ObjectId

def PegarProdutos(mydb):
    mycol = mydb.Produtos
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)

def ProdutosbyID(mydb):
    #Query
    mycol = mydb.Produtos
    print("\n####QUERY####")
    myquery = { "_id":ObjectId ("63225317be00eafd70feb51a") }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)