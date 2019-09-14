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

print("Bem Vindo! Utilize esse programa para adicionar perguntas ao jogo!")
print()

parar = ""

while(parar != "parar"):
    print("Para cancelar a operacao, digite parar")
    print("Para continuar, digite qualquer outra coisa")    
    print()

    parar = input()
    print()
    
    if(parar != "parar"):
        # Faz conexao com o banco de dados para puxar a quantidade de perguntas
        db_quantidade_perguntas = firebase.database()
        quantidade_perguntas = db_quantidade_perguntas.child("Quantidade").get().val()
        
        print("Ok! Antes de comecar a adicionar uma pergunta, leia as regras atentamente!")
        print()
        
        # Regras para adicionar uma pergunta
        print("Regras:")
        print("1 - Voce ira primeiro inserir uma pergunta")
        print("2 - Apos isso, voce devera informar 4 possiveis respostas")
        print("3 - Das respostas, somente 1 podera ser a resposta correta")
        print("4 - Caso voce informe mais de 1 resposta correta, o programa ira recusar")
        print()
        
        print("Ok, agora iremos comecar entao!")
        print()

        # Pede para o usuario informar a pergunta
        pergunta_informada = input("Informe aqui a pergunta: ")
        print()

        # Cria uma lista com 4 posicoes para guardar as respostas
        lista_respostas = [""] * 4
        lista_isCorrect = [0] * 4

        # Pede para o usuario informar as respostas
        indice_resposta = 0
        
        # Verifica se existe uma e somente uma resposta verdadeira
        onlyOneTrue = 0

        while indice_resposta < 4:
            # Pede uma resposta para a pergunta informada e pergunta se ela e verdadeira ou falsa
            print("Insira a resposta numero", indice_resposta + 1,": ", end=(''))
            resposta_atual = input()
            
            #Pede para informar se a resposta e verdadeira ou falsa
            isCorrect = int(input("Digite 0 caso a resposta seja falsa e 1 caso seja verdadeira: "))
            print()

            # Verifica se a entrada e valida
            if(isCorrect != 0 and isCorrect != 1):
                print("Insira somente 0 ou 1")
                print()
                continue

            # Verifica se existe somente uma resposta correta
            elif(isCorrect == 1 and onlyOneTrue > 0):
                print("Somente uma resposta pode ser verdadeira!")
                print()
                continue
            
            # Verifica se existe uma e somente uma resposta verdadeira
            elif(indice_resposta == 3 and isCorrect == 0 and onlyOneTrue == 0):
                print("E necessario ter 1 resposta verdadeira!")
                print()
                continue
            
            # Indica que uma resposta verdadeira foi informada
            elif(isCorrect == 1):
                onlyOneTrue = 1
                lista_isCorrect[indice_resposta] = True
            
            #Caso resposta seja falsa
            else:
                lista_isCorrect[indice_resposta] = False 
            
            #Escreve a resposta na lista das respostas
            lista_respostas[indice_resposta] = resposta_atual
            
            #Mensagem de sucesso ao gravar a resposta
            print("Resposta numero", indice_resposta + 1,"gravada!")
            print()

            indice_resposta += 1
        
        #Lista com a ordem das letras das respostas
        letra_resposta = ["a" , "b" , "c" , "d"]

        #Faz a conexao com o db para poder guardar as respostas
        db_resposta = firebase.database()
        resposta = db_resposta.child("Respostas")  

        #Escreve todas as respostas no db
        nova_resposta = {
            str(quantidade_perguntas+1):{
                letra_resposta[0]:{
                    "isCorrect":lista_isCorrect[0],
                    "valor":str(lista_respostas[0])   
                },
                letra_resposta[1]:{
                    "isCorrect":lista_isCorrect[1],
                    "valor":str(lista_respostas[1])   
                },
                letra_resposta[2]:{
                    "isCorrect":lista_isCorrect[2],
                    "valor":str(lista_respostas[2])   
                },
                letra_resposta[3]:{
                    "isCorrect":lista_isCorrect[3],
                    "valor":str(lista_respostas[3])   
                }
            }
        }
        resposta.update(nova_resposta)
        
        # Faz a conexao com o db para poder enviar a pergunta
        db_pergunta = firebase.database()
        pergunta = db_pergunta.child("Perguntas")
        
        # Adiciona a pergunta no branch das Perguntas
        nova_pergunta = {
            str(quantidade_perguntas + 1):{
                "Pergunta":pergunta_informada
            }
        }

        # Atualiza o branch das Perguntas
        pergunta.update(nova_pergunta)

        # Faz a conexao com db para atualizar o valor da quantidade de perguntas
        db_update_quantidade_perguntas = firebase.database()
        db_update_quantidade_perguntas.update({"Quantidade":(quantidade_perguntas+1)})

        print("Ok! Sua pergunta ja esta disponivel no jogo!")
        print()




