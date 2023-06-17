#===========================================#####=============================================================#
#Universidade de Mogi das Cruzes
#Programador: Douglas Pardim Ferreira 
#Turma: 1b ADS Noturno
#Data: 16/06/2023
#Programa: Criação de E-mail 
#===========================================#####=============================================================#

import locale
import os 
import datetime
from getpass import getpass
from time import sleep

L1=[]
with open("dados.txt","r") as db:
    for i in db:
        L1.append(i.rstrip().split(','))
        
data = datetime.datetime.now() #Data Atual

# TABELA DO MENU INICIAL
while True:
    print('''****************** Menu *******************
|             1 - Logar                   |
|             2 - Criar Conta             |
|             3 - Recuperar Senha         |
|             4 - Registros               |
|             5 - Sair                    |
*******************************************''')
    opt=input("Selecione uma opção: ")
    
    if opt not in ["1","2","3","4","5"]: # Verifica se a opção está correta
        os.system("clear")
        print("Opção Inválida!")
        input("Pressione ENTER para voltar ao menu" )

#1-LOGAR
    os.system("clear")
    if opt == "1":
        
        print("********************* Login *********************")
        email = input("GDB E-mail: ")
        senha=getpass("Senha: ")
        encontrado = False
    
        # Verifica se e EMAIL e a SENHA estão na lista
        for i in L1:
            if email == i[3] and senha == i[4]:
                print("*************************************************")
                print("GDB E-mail localizado, logado com sucesso!")
                encontrado = True
                input("\nPressione ENTER para entrar!")
                os.system("clear")
        
            # Delay na menssagem de boas vindas! 
                delay=1
                contador=0
                while contador<5:
                    print("\033[01;32mBem vindo ao GDB E-mail! :D\033[m")
                    sleep(delay)
                    contador=contador+1
                    if contador==5:
                        os.system("clear")
        
                                            
                # TABELA DO SUBMENU LOGIN
                print('''*************** GDB E-mail ****************
|             1 - (em breve)              |
|             2 - Exclui Conta            |
|             3 - (em breve)              |
|             4 - Sair                    |
*******************************************''')
                opt_login=input("Selecione uma opção: ")
                
                if opt_login not in ["1","2","3","4"]: # Verifica se a opção está correta
                    os.system("clear")
                    print("Opção Inválida!")
                    input("Pressione ENTER para voltar ao menu" )
                
                # Excluir Conta
                if opt_login == "2":
                    os.system("clear")
                    email_excluir = input("Digite o e-mail da conta que deseja excluir: ")
                
                    # Verificar se o e-mail existe na lista e excluir o E-mail
                    for i, conta in enumerate(L1):
                        if email_excluir == conta[3]:
                            confirmacao = input("Tem certeza de que deseja excluir a conta? (S/N): ")
                            if confirmacao.upper() == "S":
                                del L1[i]
                                with open("dados.txt", "w") as db:
                                    for dados in L1:
                                        db.write(",".join(dados) + "\n")
                                print("Conta excluída com sucesso!")
                                print("*************************************************\n")
                            else:
                                print("*************************************************\n")
                                print("Exclusão de conta cancelada.")
                                input("\nPressione ENTER para voltar ao menu")
                                break
                        else:
                            print("*************************************************\n")
                            print("E-mail não encontrado.")
                            input("\nPressione ENTER para voltar ao menu")

                
                # Sair do SUBMENU    
                if opt_login == "4":
                    break
                    
        # Erro se o EMAIL e a SENHA estiverem errados
        if not encontrado:
            print("*************************************************")
            print("GDB E-mail não localizado!")
            print("Verifique o E-mail e a Senha se estão corretos!\n")
            input("Pressione ENTER para voltar ao menu")
            
#2-CRIAR CONTA 
    os.system("clear")
    if opt=="2":
        print("************** Criando Conta **************")
        nome=input("Nome: ")
        gdb="@gdb.com"
        if nome.replace(" ", "").isalpha(): # Verifica se o nome é apenas letras e espaços
            try:
                # DADOS
                idade=int(input("Informe sua idade: "))
                celular=int(input("Número de celular: "))
                
                email= nome+str(idade)+gdb # Adiciona o nome+idade, para criar o email completo
                email= nome.replace(" ", "")+str(idade)+gdb # Remove o "ESPAÇO" do nome
                
                for account in L1: # Verifica se já tem um E-mail igual
                    if account[3] == email:
                        print("*******************************************")
                        print("Esse email já está em uso.\n")
                        print("Por favor, altere o seu nome com letra maiúscula ou minúscula.")
                        print("Se persistir no erro coloque o nome completo ou apenas o sobrenome.")
                        opt2 = input("\nPressione ENTER para voltar ao menu!")
                        os.system("clear")
                        break
                
                print("\nSeu GDB E-mail será:", email)
                senha=getpass("Agora digite à sua senha: ") # A senha fica oculta
                if senha.strip() == "":
                    raise ValueError("Senha não pode ser em branco")
                print("*******************************************")
                
                # Incluir conta na LISTA 
                L1.append([nome,idade,celular,email,senha,data.strftime('%d-%m-%Y')]) #DATA.STRFTIME adiciona a data formatada
                with open("dados.txt",'w') as db:
                        for i in L1:
                            db.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]}\n')
                            
                
                # Conta Criada
                print("\nConta criada com sucesso!")
                opt3=input("Pressione ENTER para voltar ao menu!" )
                os.system("clear")
                    
            # Tratamento de erro da criação da conta
            except:
                os.system("clear")
                print("Dados inválidos!")
                opt2=input("Pressione ENTER para voltar ao menu!" )
                os.system("clear")
        else:
            os.system("clear")
            print("O Nome deve conter apenas letras!")
            opt2=input("Pressione ENTER para voltar ao menu!" )
            os.system("clear")


#3-Recuperação de SENHA 
    elif opt=="3":
        os.system("clear")
        print("*********************** Recuperar Senha ***********************\n")
        email=input("Digite o seu GDB E-mail: ")
        idade=input("Digite a sua idade: ")
        celular=input("Digite o seu número de celular: ")
        encontrado = False
        
        for i in L1: # Verifica se e EMAIL e os DADOS estão na lista
            if email == i[3] and idade ==i[1] and celular ==i[2]:
                print("\nGDB E-mail localizado!")
                print("\n***************************************************************")
                encontrado = True
                print("A senha associada a este e-mail é:", i[4])
                print("***************************************************************")
                input("\nPressione ENTER para voltar ao menu")
                os.system("clear")
        
        # Erro se o EMAIL e o DADOS estiverem errados       
        if not encontrado:
            print("\n***************************************************************")
            print("GDB E-mail não encontrado!")
            input("\nPressione ENTER para voltar ao menu")
            os.system("clear")


#4-Registro das contas criadas
    elif opt=="4":
        os.system("clear")
        print("*********************** Registro de Contas Criadas ***********************\n")
        for i in L1:
            print(f"Nome:{i[0]}    E-mail:{i[3]}    Data da Criação:{i[5]}")
        print("\n**************************************************************************")
        input ("Pressione ENTER para voltar ao menu!")
        os.system("clear")


#5- SAIR
    elif opt=="5":
        print("------------------------------------")
        print("Volte Sempre!")
        print("------------------------------------")
        break
