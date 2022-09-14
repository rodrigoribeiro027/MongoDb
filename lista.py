# dic = {'semente':'abacate',{'sementeB':'laranja'}}
# dic ['semente']
# dic ['sementeB']
# print(dic)


import json
teste = []
for i  in range(1,11):
    aux = {'nome':i, 'id':i}
    teste.append(aux)

print(json.dumps(teste, indent=2))