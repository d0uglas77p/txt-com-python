#===========================================#####=============================================================#
#Universidade de Mogi das Cruzes
#Programador: Douglas Pardim Ferreira  
#Turma: 1b ADS Noturno
#Data: 07/06/2023
#Programa:  Problema 5 (Reserva de Apartamento)
#===========================================#####=============================================================#

#################################################################### BIBLIOTECAS
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#################################################################### LISTA TXT
L1=[]
with open("historico.txt",'r') as db:
    for i in db:
        L1.append(i.rstrip().split(','))

################################################################### MENU INICIAL
while True:
    print("=============== Menu ================ ")
    print("[1] Calcular Diárias\n[2] Exibir Histórico\n[3] Limpar Histórico\n[4] Salvar\n[5] Sair")
    print("=====================================")
    opt=input("Selecione uma opção: ")
    
    if opt not in ["1","2","3","4","5"]:
        os.system('cls')
        print("Opção Inválida")
        input("Precione ENTER para voltar ao menu" )  

    ###################################################### MENU TABELA DE PREÇOS
    os.system("cls")
    if opt=="1":
        print("======================== Tabela de Preços  =======================")
        print('''Hóspedes      Apartamento Tipo 1(R$)      Apartamento Tipo 2 (R$)
    1                R$20,00                     R$25,00
    2                R$28,00                     R$34,00
    3                R$35,00                     R$42,00
    4                R$42,00                     R$50,00
    5                R$48,00                     R$57,00
    6                R$53,00                     R$63,00''')
        print("==================================================================")
    
        ################################################# TRATAMENTO DE ERRO TRY
        try:
            hospedes=int(input("Quantidade de Hóspedes: "))
            ap=int(input("Tipo de Apartamento: "))
            dias=int(input("Dias de Reserva: "))
            os.system("cls")
            
            ############################################### PROCESSO DOS VALORES
            if hospedes==1 and ap==1:
                diaria=20
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
                
            elif hospedes==1 and ap==2:
                diaria=25
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==2 and ap==1:
                diaria=28
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==2 and ap==2:
                diaria=34
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==3 and ap==1:
                diaria=35
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==3 and ap==2:
                diaria=42
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==4 and ap==1:
                diaria=42
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==4 and ap==2:
                diaria=50
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==5 and ap==1:
                diaria=48
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==5 and ap==2:
                diaria=57
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==6 and ap==1:
                diaria=53
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            elif hospedes==6 and ap==2:
                diaria=63
                valorDiaria=(diaria*dias*hospedes)
                print("=======================================================")
                print("Quantidade de Hóspedes:", hospedes)
                print("Apartamento Diário: R$%.2f" % (diaria))
                print("Dias de Reserva:", dias)
                print("Valor Total: R$%.2f" % (valorDiaria))
                L1.append([hospedes,diaria,dias,valorDiaria])
                print("=======================================================")
                input("Precione ENTER para voltar ao menu e salvar!" )
                os.system("cls")
            #################################################### FIM DO PROCESSO
            
        ############################################## TRATAMENTO DE ERRO EXCEPT    
        except:
            os.system("cls")
            opt2=input("Opção Incorreta! Digite qualquer tecla para voltar ao menu ou (F) para finalizar: ")
            if opt2 in ["F","f"]:
                break
            else:
                os.system("cls")
        ########################################### FIM DO MENU TABELA DE PREÇOS

    ######################################################### LISTA DE HISTÓRICO 
    elif opt=="2":
        try:
            os.system("cls")
            print("========================================================")
            print(f"{'Hóspedes':^10} {'Diaria':^10} {'Dias':^10} {'Valor Total':^10}")
            for i in L1:
                valor = locale.currency(float(i[2]), grouping=True, symbol=True)
                print(f"{i[0]:^10} {locale.currency(float(i[1])):^10} {i[2]:^10} {locale.currency(float(i[3])):^10}")
            print("========================================================")    
            input ("Precione ENTER para voltar ao menu" )
            os.system("cls")
        except NameError:
            os.system("cls")
            print("========================================================") 
            print("Nenhum histórico encontrado!")
            print("========================================================")    
            input ("Precione ENTER para voltar ao menu" )
            os.system("cls")
            
    ########################################################### LIMPAR HISTÓRICO
    elif opt=="3":
        try:
            os.system("cls")
            for i in L1:
                print("========================================================================") 
                opt2=input("Tem certeza que deseja limpar o histórico? [S] sim [N] não: ")
                if opt2 in ["S","s"]:
                    del L1
                    print("========================================================================") 
                    input ("Precione ENTER para voltar ao menu" )
                    os.system("cls")
                    break
                elif opt2 in["N","n"]:
                    print("========================================================================")  
                    input ("Precione ENTER para voltar ao menu" )
                    os.system("cls")
                    break
        except NameError:
            os.system("cls")
            print("========================================================") 
            print("Nenhum histórico encontrado!")
            print("========================================================")    
            input ("Precione ENTER para voltar ao menu" )
            os.system("cls")        
    
    
    ########################################################## SALVAR AS DIÁRIAS
    elif opt=="4":
        try:
            os.system("cls")
            with open("historico.txt",'w') as db:
                        for i in L1:
                            db.write(f'{i[0]},{i[1]},{i[2]},{i[3]}\n')
        except NameError:
            os.system("cls")
            print("========================================================") 
            print("Nenhum histórico encontrado!")
            print("========================================================")    
            input ("Precione ENTER para voltar ao menu" )
            os.system("cls")                     
    
    ####################################################################### SAIR
    elif opt=="5":
        print("====================================")
        print("Volte Sempre! :D")
        print("====================================")
        break