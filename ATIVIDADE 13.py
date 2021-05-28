#Criando uma lista vazia chamada "usuarios"
from os import openpty
import hashlib
import hmac
h = hashlib.new('sha256')

h.update(b"passwordn")
h.hexdigest()

usuarios = []

#Criando um usuario como dicionario com name, username e password
usuario1 = {
    "name1" : "Clark Kent",
    "username1" : "kent",
    "password1" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
}
# Inclui este usuario na lista de usuarios
usuarios.append(usuario1)

#Criando um usuario como dicionario com name, username e password
usuario2 = {
    "name2": "Bruce Wayne",
    "username2" : "wayne",
    "password2" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
}

# Inclui este usuario na lista de usuarios
usuarios.append(usuario2)

#Criando um usuario como dicionario com name, username e password
usuario3 = {
    "name3": "Christopher Walker",
    "username3" : "walker",
    "password3" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
}

# Inclui este usuario na lista de usuarios
usuarios.append(usuario3)

#KENT

# Insira seu username = username input"Insira seu username:")

# Variavel que servira para recever opçoes 
op = "usuarios"

# Enquanto o usuario nao digitar a opção de saida
while(op!= "kent"):
   op = input("Insira seu username: ")

#Quando o usuario digitar a opção correta
op = input("Insira sua senha: ")

#SENHA KENT

password = input()

sha256_pass = hashlib.sha256(b"password").hexdigest()


while not sha256_pass : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
input('Insira sua senha: ')

if sha256_pass : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"

print ("'name1' logado!")