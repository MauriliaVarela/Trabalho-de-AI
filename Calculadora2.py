def calculadora():
    lista_contas =[]
    while True:
        print("-*" * 25)
        print("                  MENU DE OPÇÕES                     ")
        print("-*" * 25)
        print("Soma : + ")
        print("Subtração : - ")
        print(" Multiplicção : * ")
        print("Divisão : / ")
        print("Saída : s ")
        print("hist")

        Operador=input("Escolha uma opção")

        
        #Sair
        if Operador == "s":
            break

        # Exibir histórico
        elif Operador == "hist":
            if lista_contas:
                print("Histórico de operações:\n")
                print(lista_contas)
                print(" Ao todo foram feitas ", len(lista_contas) ,"operações")
            else:
                print("Ainda não foram realizadas operações.")
            continue  # Volta ao menu


    # função principal

        #Entrada de números
        num1=float(input("Insira o primeiro numero: "))
        num2=float(input("Insira o segundo numero: "))

        #Operações
        if Operador == "+" :
            result = num1 + num2
            print(" A soma dos números inseridos é : " + str(result))
            lista_contas.append( str(num1) + " + " + str(num2) + " = " + str(result))

        elif Operador == "-" :
            result = num1-num2
            print(" A subtração dos números inseridos é : " + str(result))
            lista_contas.append(str(num1) + " - " + str(num2) + " = " + str(result))

        elif Operador == "/":
            result = num1/num2
            print(" A divisão dos número inseridos é : " + str(result))
            lista_contas.append( str(num1) + " / " + str(num2) + " = " + str(result))

        elif Operador == "*":
            result = num1*num2
            print(" A Multiplicação dos números inseridos é : " + str(result))
            lista_contas.append( str(num1) + " * " + str(num2) + " = " + str(result))


calculadora()

