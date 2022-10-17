
global mydb


def CadastrarUsuario(mydb):
    Nome = input(str('escreva seu Nome:'))
    Data_Nascimento = input(str('escreva sua Data_Nascimento:'))
    Email = input(str('escreva seu Email:'))
    Senha = input(str('escreva seu Senha:'))
    Telefone = input(str('escreva seu Telefone:'))
    Cpf = input(str('escreva seu Cpf:'))
    Cidade = input(str('escreva seu Cidade:'))
    Endereco = input(str('escreva seu Endereco:'))
    mycol = mydb.usuario
    print("\n #####insert Usuario Inserido Com Sucesso. ###")
    mydict = {
    "Nome":Nome,
    "Data_Nascimento":Data_Nascimento,
    "Email":Email,
    "Senha":Senha,
    "Telefone":Telefone,
    "Cpf":Cpf,
    "lista_Desejo":[],
    "Cidade":Cidade,
    "Endereco":Endereco
}
    x = mycol.insert_one(mydict)
    
    print(x.inserted_id)