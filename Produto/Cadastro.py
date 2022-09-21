global mydb

def CadastrarProduto(mydb):
    Nome =  input(str('escreva seu Nome Produto:'))
    Data_Produto =  input(str('escreva seu Data do Produto:'))
    Descricao =  input(str('escreva sua Descrição:'))
    Preco =  input(str('escreva seu Preço:'))
    Quantidade_Estoque =  input(str('escreva Quantidade Estoque desse Produto:'))
    NomeVendedor =  input(str('escreva O Nome do Vendedor:'))
    Telefone =  input(str('escreva O Telefone do Vendedor:'))
    NumeroInscricao =  input(str('escreva O NumeroInscricao do Vendedor:'))

    mycol = mydb.Produtos
    
    print("\n #####insert Produto Inserido ###")
    mydict = {
        "Nome":Nome,
        "Data_Produto":Data_Produto,
        "Descricao":Descricao,
        "Preco":Preco,
        "Quantidade_Estoque":Quantidade_Estoque,
        "Vendedor":{"NomeVendedor":NomeVendedor,"Telefone":Telefone,"NumeroInscricao":NumeroInscricao}}
        
    x = mycol.insert_one(mydict)
    print(x.inserted_id)