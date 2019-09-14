#Bibliotecas 
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

#Faz conexao com o banco de dados para puxar a quantidade de perguntas
db_quantidade_perguntas = firebase.database()
quantidade_perguntas = db_quantidade_perguntas.child("Quantidade").get().val()

print("Bem Vindo! Utilize esse programa para adicionar perguntas ao jogo!")
print(quantidade_perguntas)


