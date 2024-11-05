def calculadora():
    while True:
        print("-*" * 25)
        print("                  MENU DE OPÇÕES                     ")
        print("-*" * 25)
        print("Soma : + ")
        print("Subtração : - ")
        print(" Multiplicção : * ")
        print("Divisão : / ")
        print("Saída : s ")

        Operador=input("Escolha uma opção")

        #Sair
        if Operador == "s":
            break

    # função principal

        #Entrada de números
        num1=float(input("Insira o primeiro numero: "))
        num2=float(input("Insira o segundo numero: "))

        #Operações
        if Operador == "+" :
            result = num1 + num2
            print(" A soma dos números inseridos é : " + str(result))
            

        elif Operador == "-" :
            result = num1-num2
            print(" A subtração dos números inseridos é : " + str(result))
            
        elif Operador == "/":
            result = num1/num2
            print(" A divisão dos número inseridos é : " + str(result))
            
        elif Operador == "*":
            result = num1*num2
            print(" A Multiplicação dos números inseridos é : " + str(result))
            

calculadora()


    
