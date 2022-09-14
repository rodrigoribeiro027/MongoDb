
def Compra( mydb):
    
    mycol = mydb.Compra
    print("\n #####insert Compra Inserido ###")
    mydict = {{
        "_id":{"$oid":"630df33dce8a5651c6309164"},
        "Usuario_ID":{"ID":{"$oid":"630e96c226d1f4b1ba9c5787"},
        "Nome":"Rodrigo Ribeiro Dos Santos",
        "Email":"Rodrigo.rsantos70@gmail.com",
        "Cpf":"123912-2121","Cidade":"SP",
        "Endereco":"Rua joaquim andrade n123"},
        "Produto_ID":[{"id":{"$oid":"630df511ce8a5651c630916a"},
        "Nome":"Notebook Intel","Preco":"6300","Quantidade":"1"}],
        "Vendedor_ID":{"ID":{"$oid":"630e964d26d1f4b1ba9c5786"},
        "Nome":"Mercado livre","Cpf/Cnpj":"423.878.888-99"},
        "Total_Compra":{"Total":"1000","Data_Compra":"10/02/2000"}}
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)