# Bibliotecas 
import pyrebase

config = {
    "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
    "authDomain": "teste-python-67d43.firebaseapp.com",
    "databaseURL": "https://teste-python-67d43.firebaseio.com",
    "projectId": "teste-python-67d43",
    "storageBucket": "",
    "messagingSenderId": "581051665954",
    "appId": "1:581051665954:web:6f131448200a100689447b"
}

firebase = pyrebase.initialize_app(config)

# Faz conexao com o banco de dados para puxar a quantidade de perguntas
db_quantidade_perguntas = firebase.database()
quantidade_perguntas = db_quantidade_perguntas.child("Quantidade").get().val()

print("Bem Vindo! Utilize esse programa para adicionar perguntas ao jogo!")

parar = ""

while(parar != "parar"):
    print("Para cancelar a operacao, digite parar")
    print("Para continuar, digite qualquer outra coisa")    
    print()

    parar = input()
    print()
    
    if(parar != "parar"):
        print("Ok! Antes de comecar a adicionar uma pergunta, leia as regras atentamente!")
        print()
        
        # Regras para adicionar uma pergunta
        print("Regras:")
        print("1 - Voce ira primeiro inserir uma pergunta")
        print("2 - Apos isso, voce devera informar 4 possiveis respostas")
        print("3 - Das respostas, somente 1 podera ser a resposta correta")
        print("4 - Caso voce informe mais de 1 resposta correta, o programa ira reiniciar")
        print()
        
        print("Ok, agora iremos comecar entao!")
        print()

        pergunta_informada = input("Informe aqui a pergunta: ")

        # Faz a conexao com o db para poder enviar a pergunta
        db_pergunta = firebase.database()
        pergunta = db_pergunta.child("Perguntas")
        
        nova_pergunta = {
            str(quantidade_perguntas + 1):{
                "Pergunta":pergunta_informada
            }
        }

        pergunta.update(nova_pergunta)




