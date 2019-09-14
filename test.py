import pyrebase
import random

#Configuracoes importantes para linkar ao projeto do Firebase
config = {
    "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
    "authDomain": "teste-python-67d43.firebaseapp.com",
    "databaseURL": "https://teste-python-67d43.firebaseio.com",
    "projectId": "teste-python-67d43",
    "storageBucket": "",
    "messagingSenderId": "581051665954",
    "appId": "1:581051665954:web:6f131448200a100689447b"
}

#Faz conexao com Firebase
firebase = pyrebase.initialize_app(config)

#Faz a conexao com o banco de dados externo
db = firebase.database()

#Variavel que recebe todos os dados do no principal
dados = db.get()

#Conta quantas perguntas existem no banco de dados
quantidadePeguntas = 0

#Para cada pergunta, incrementa o valor em 1
for perguntas in dados.each():
    quantidadePeguntas += 1

perguntaAtual = random.randrange(1, quantidadePeguntas+1)

print(perguntaAtual)