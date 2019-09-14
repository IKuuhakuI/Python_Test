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

#Quantas perguntas tem no jogo
quantidadePeguntas = db.child("Quantidade").get().val()
print(quantidadePeguntas)

#Lista que diz quais perguntas ja foram
perguntas_antigas = [0] * quantidadePeguntas

rodada = 1

while(rodada <= quantidadePeguntas):
    perguntaAtual = random.randrange(1, quantidadePeguntas + 1)
    if(perguntas_antigas[perguntaAtual - 1] == 1):
        continue
    else:
        print(perguntaAtual ,perguntas_antigas[perguntaAtual - 1])
        perguntas_antigas[perguntaAtual - 1] = 1
        rodada += 1

#print(quantidadePeguntas)