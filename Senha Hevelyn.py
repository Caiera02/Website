import tkinter as tk
import stdiomask
from getpass import getpass

#Definindo uma função ( 1- Escolher o nome da função
#                       2- Passar os paraemetros caso tenha () 
#                       3- print o resultado da função        )

# Menu

def exibir_menu():
    print('     Seja Bem vida \nEscolha uma opção \n[1] New Cadastro\n[2] Fazer Login\n[3] Exit')
    opcao= int(input(" Digite a opção desejada: "))

    return(opcao)
# -----------------------------------------------------------
# Tela de Login
'''
def Tela_login():
    # Janela 
    raiz = tk.Tk()
    raiz.geometry("300x320")
    raiz.title('Tela_login')
    
    #criando o texto que vai ser exebido
    label = tk.Label( text="Usuário", 
                      fg="green")
    #estilizaão da minha label
    label.pack(side="top")

    #criando a caixa, no caso meu input que vai ser exebido
    usuario = tk.Entry()
    #criando o texto que vai ser exebido
    usuario.pack(side="top")

    raiz.mainloop()
'''
#---------------------------------------------------------------------

# Cadastro

def novo_cadastro():
    Login= input("Digite um usuario: ")
    Senha= stdiomask.getpass(prompt="Senha: ", mask='*')

    Db = [Login,Senha]

     # escrevendo em arquivo txt
    
    # with open("senha.txt",'a',newline='') as file:
    #     Login= (f'{Login} {Senha }' )
    #     file.writelines(Login)  
    #     for i in range():
    #         Login.append(i)
    #     print(i)

    print('Cadastro realizado com sucesso')
    return(Login,Senha)

def realizar_login():
    login2= input(" Usuario: ")
    senha2= stdiomask.getpass(prompt='Senha: ', mask='*')
    '''
    with open("senha.txt") as file:
        if Login2 == Login and senha2== Senha:
            print(" Login realizado !!")
        else:
            print('Usuario ou senha Invalida !!!')
    '''
    
# perguntas
def encontro():
    print ("Quando foi nosso primeiro encontro ?")
    resposta= int(input('R:Digite apenas os numeros:  '))
    
    if resposta != 11032022:
        print('Resposta errada')
        resposta= 'Digite novamente: '
    return(resposta)

# Algumas perguntar para interagir com usuario
def date():
    print('                                 Seja bem vinda ao System Hevelyn  \n                              ')
    print( ' Quando foi nosso primeiro encontro ? ' )
    print(' \nEscolha uma opção \n[1] 11/03/2023 \n[2] 28/07/2022 \n[3] 11/03/2022')
    respost=int(input('Digite a opção desejada: '))
    while True:
        if respost == 3 or 2 or 1:
            print('\nresposta errada')
            print('\npessima namorada, você errou nosso primeiro date')
            print('\nEscolha a opção certa:\n[1] 11/05/2023 \n[2] 28/07/2022 \n[3] 11/03/2022\n')
            a=int(input('Tente novamente: '))
            while a != 3:
                a=int(input('Tente novamente: '))
                if a == 3:
                    print("\nVocê acertou, só queria te sacanear mesmo\n")
                elif a == 2 or 1:
                    print("Errou !!")
            return(a)
#-------------------------------------------------------------------------------------------
def My_niver():
    print('--------------------------------------------------------')
    print('                              \n Proxima pergunta  \n                              ')
    print( ' Quando é meu aniversario ? ' )
    quenstions=int(input('Digite apenas os numeros: '))
    while True:
        if quenstions == 28072003:
            print('Você acertou')
        else:
            print('Você errou,pessima namorada')
        
            print('Digite apenas os numeros')
            a= int(input('Tente novamente: '))
            if quenstions == 28072003:
                print('Você acertou')

        return(quenstions)
#============================================================================================
def affair():
    print('---------------------------------------------------------')
    print('                              \n Proxima pergunta  \n                              ')
    print( 'Qual é data do nosso namoro ? ' )
    r= int(input('Digite apenas os numeros: '))
    while True:
        if r == 28082022:
            print('acertou mizera')
            break
        else:
            print('Você errou,pessima namorada')
            print('Digite apenas os numeros: ')
            r= int(input("Tente novamente:"))
#====================================================================================            
def ultimate_question():
      print('                              \n Ultima pergunta  \n                              ')
      print( 'Qual é o da mulher da minha vida  ? ' )
      print(' \nEscolha a opção certa:\n \n[1]Hevelyn\n \n[2]Ana Paula\n \n[3] Bia\n \n[4]Laura\n \n[5]Nair\n')
      resposta= int(input('Digite a opção desejada: '))
      while True:
          # Primerio bloco
          if resposta == 1 or 2 or 3 or 4 or 5 :
              print('---------')
              print('| Errou |')
              print('---------')
              print('-------------------------------------------------------------------------------------')
              # Segundo bloco
              print(' \nEscolha a opção certa:\n \n[1]Ana Paula\n \n[2] Bia\n \n[3]Laura\n \n[4] Nair\n')
              resposta= int(input('Digite a opção desejada: '))
              if resposta == 1 or 2 or 3 or 4  :
                print('---------')
                print('| Errou |')
                print('---------') 
                print('-------------------------------------------------------------------------------------')
                # Terceiro bloco
                print(' \nEscolha a opção certa:\n \n[1]Ana Paula\n \n[2] Bia\n \n[3]Laura\n')
                resposta= int(input('Digite a opção desejada: '))
                if resposta == 1 or 2 or 3  :
                    print('---------')
                    print('| Errou |')
                    print('---------')
                    print('-------------------------------------------------------------------------------------')
                    # Quarto bloco
                    print(' \nEscolha a opção certa:\n \n[1]Ana Paula\n \n[2]Laura\n')
                    resposta= int(input('Digite a opção desejada: '))
                    if resposta == 1 or 2  :
                        print('---------')
                        print('| Errou |')
                        print('---------')
                        print('-------------------------------------------------------------------------------------')
                    # Quinto bloco, aqui acabou a brincaderia
                        print(' \nEscolha a opção certa:\n \n[1]Laura\n')
                        resposta= int(input('Digite a opção desejada: '))
                        if resposta == 1:
                            print('FIM')
                        
                            print(' \nBrincadeira\n, \nVOCÊ QUE É O MAIOR AMOR DA MINHA VIDA\n')
                            print('-------------------------------------------------------------------------------------')
                        return(resposta)

                                # Começo do programa 
#opcao = exibir_menu()
#teste= affair() 

if opcao == 1:
      Cadastro = novo_cadastro()
      print()
      print("\nVamos as perguntasz\n")
      Primeira= date()
      Segunda=  My_niver()
      Terceiro= affair()
      Quarto=   ultimate_question()  

# if opcao == 2:
#      login = realizar_login()