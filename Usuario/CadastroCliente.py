
global mydb


def CadastrarUsuario(mydb):
    mycol = mydb.usuario
    print("\n #####insert Usuario Inserido ###")
    mydict = {
    "Nome":"Jorge Ribeiro Dos Santos",
    "Data_Nascimento":"2000-10-10",
    "Email":"Rodrigo.rsantos80@gmail.com","Telefone":"123914545","Cpf":"121.845.123-77",
    "lista_Desejo":[{"Produto_ID":{"id":"630f45304b88272631990c17"},
    "Nome":"Rodrigo Ribeiro ","Preco":"3500"},{"Vendedor_ID":{"$oid":"630f458c4b88272631990c18"},
    "Nome":"Mercado livre","Telefone":"1239256454"}],"Cidade":"Sp","Endereco":"Rua joaquim andrade n123"
}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)