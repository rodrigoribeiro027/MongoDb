## MongoDb
### Instalações necessarias
<strong>Python version: 3.10</strong>
```bash
pip install dnspython
```
```bash
pip install pymongo
```

## Adição de Nome do banco de dados no MongoDB e senha

#### Exemplo
```bash
mongodb+srv://'Rodrigo':'minhaSenha'
```
```bash
 client = pymongo.MongoClient("mongodb+srv://Rodrigo:'minhaSenha'@rodrigo.8fj9sjv.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
```

## E por Fim basta entrar na pasta da aplicação e rodar a aplicação.
```bash
Python main.py
```
