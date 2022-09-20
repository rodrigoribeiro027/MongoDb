import Usuario.FindQuery as Procurar
import Produto.FindQuery

def Compra(mydb):

    Usuario= Procurar.UsuariobyID(mydb)
    Produto = Produto.FindQuery.ProdutosbyID(mydb)
    
    mycol = mydb.Compra
    print("\n #####insert Compra Inserido ###")
    mydict = {{
        "Usuario_ID":Usuario,
        "Produto_ID":Produto,
        "Total_Compra":{"Total":"1000","Data_Compra":"10/02/2000"}}
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

