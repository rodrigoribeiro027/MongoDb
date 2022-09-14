global mydb

def CadastrarProduto(mydb):
    mycol = mydb.Produtos
    print("\n #####insert Produto Inserido ###")
    mydict = {
        "Nome":"Notebook Intel",
        "Data_Produto":"Fri Jan 07 2000 00:00:00 GMT-0200 (Hora de verão de Brasília)",
        "Descricao":"Core I3 4Gb 1Tb - 15,6Hd","Preco":"3500","Quantidade_Estoque":"12",
        "Vendedor":{"Vendedor":"Mercado Livre","ID":{"$oid":"630f42a739b7d96c7564173a"}}}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)