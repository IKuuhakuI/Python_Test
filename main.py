# Importa os outros programas
import game
import send_questions

# Mensagem de entrada
print("Bem Vindo ao jogo de Perguntas e Respostas!")
print()
print("O objetivo e ver quem consegue acertar o maximo de perguntas sem errar!")
print("Voce acha que consegue quebrar o recorde?")
print()
print("Ou entao, voce pode contribuir para o jogo, informando novas perguntas!")
print("E entao, o que deseja fazer?")
print()

# Variavel de controle
opcao = 0

# Menu
while(opcao != 3):
    print("Caso queira jogar, digite 1")
    print("Caso queira adicionar uma pergunta, digite 2")
    print("Para sair, digite 3")
    print()
    
    # Opcao escolhida pelo User
    opcao = int(input())
    print() 
    
    # Verifica se a entrada e valida
    if(opcao != 1 and opcao != 2 and opcao != 3):
        print("Operacao invalida! Digite somente 1 ou 2 ou 3")
        print()
    
    # Comeca o jogo
    elif(opcao == 1):
        print("Carregando o jogo...")
        print()
        game.start_game()
        print()

    # Insere novas perguntas no jogo
    elif(opcao == 2):
        send_questions.send()
        print("Obrigado pela contribuicao!")
        print()

    # Sai do programa
    elif(opcao == 3):
        print("Obrigado por jogar!")
        break