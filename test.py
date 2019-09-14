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
db_perg = firebase.database()
db_resp = firebase.database()

#Quantas perguntas tem no jogo
quantidadePeguntas = db.child("Quantidade").get().val()

#Lista que diz quais perguntas ja foram
perguntas_antigas = [0] * quantidadePeguntas

#Contador para as rodadas
rodada = 1

#Referencia ao branch das Perguntas no banco de dados
branchPerguntas = db_perg.child("Perguntas")
branchRespostas = db_resp.child("Respostas")

#Variavel que guarda a quantidade de perguntas acertadas
pontos = 0

#Contador de perguntas
while (rodada <= quantidadePeguntas):
    #Gera um numero aleatorio para definir a pergunta atual
    indicePerguntaAtual = random.randrange(1, quantidadePeguntas + 1)
    
    #Caso a pergunta seja repetida 
    if(perguntas_antigas[indicePerguntaAtual - 1] == 1):
        continue

    #Jogo    
    else:
        #Variavel com a pergunta
        perguntaAtual = branchPerguntas.child(indicePerguntaAtual).child("Pergunta").get().val()

        print("Pergunta ", rodada, ": ", perguntaAtual, " ?", sep='')
        
        #Opcao a
        respostaAtual = branchRespostas.child(indicePerguntaAtual).child("a").child("valor").get().val()
        print(respostaAtual)

        #Adiciona a pergunta atual a lista de perguntas antigas
        perguntas_antigas[indicePerguntaAtual - 1] = 1
        
        #Incrementa o valor da rodada
        rodada += 1
