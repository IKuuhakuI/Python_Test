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

#Lista que diz quais perguntas ja foram
perguntas_antigas = [0] * quantidadePeguntas

#Contador para as rodadas
rodada = 1

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
        #Conexao com o banco de dados para puxar as perguntas
        db_perg = firebase.database()
        branchPerguntas = db_perg.child("Perguntas")

        #Variavel com a pergunta
        perguntaAtual = branchPerguntas.child(indicePerguntaAtual).child("Pergunta").get().val()
        
        #Informa a pergunta
        print("Pergunta ", rodada, ": ", perguntaAtual, " ?", sep='')
        
        #loop para evitar bug de valor nulo
        for n in range(4):
            #Conexao com o banco de dados para puxar as respostas
            db_resp = firebase.database()
            branchRespostas = db_resp.child("Respostas")

            #Condicionais que colocam as opcoes em ordem
            if(n == 0):
                #Opcao a
                respostaAtual = branchRespostas.child(indicePerguntaAtual).child("a").child("valor").get().val()
                print("\ta) ", respostaAtual)

            elif(n == 1):
                #Opcao b
                respostaAtual = branchRespostas.child(indicePerguntaAtual).child("b").child("valor").get().val()
                print("\tb) ", respostaAtual)

            elif(n == 2):
                #Opcao c
                respostaAtual = branchRespostas.child(indicePerguntaAtual).child("c").child("valor").get().val()
                print("\tc) ", respostaAtual)

            else:
                #Opcao d
                respostaAtual = branchRespostas.child(indicePerguntaAtual).child("d").child("valor").get().val()
                print("\td) ", respostaAtual)
        
        #Teste para aceitar somente entradas validas
        while(True):
            respostaInformada = input("Insira a sua resposta: ")
            if(respostaInformada != "a" and respostaInformada != "b" and respostaInformada != "c" and respostaInformada != "d"):
                print("Entrada invalida! Por favor responda com a ou b ou c ou d")
            else:
                break

        db_verifica = firebase.database()

        isCorrect = db_verifica.child("Respostas").child(indicePerguntaAtual).child(respostaInformada).child("isCorrect").get().val()

        #Quebra de linha
        print()

        if(isCorrect == True):
            pontos += 1
            print("Resposta Correta!!\n")

        elif(isCorrect == False):
            print("Resposta Errada!! Fim de Jogo :(")
            break

        #Adiciona a pergunta atual a lista de perguntas antigas
        perguntas_antigas[indicePerguntaAtual - 1] = 1
        
        #Incrementa o valor da rodada
        rodada += 1

#Informa a pontuacao alcancada nessa rodada
print()
print("Pontuacao:", pontos)
print()

db_high_score = firebase.database()

high_score = db_high_score.child("Highscore").get().val()

if(pontos > high_score):
    print("Novo recorde! Parabens!")

else:
    print("Que tal tentar mais uma vez? Talvez voce consiga quebrar o recorde atual!")
    print("Recorde atual:", high_score)