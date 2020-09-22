# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def tela():
    print("\n******************* Python Calculator *******************")
    print("*** BY MAURÍCIO GAUBEUR : gaubeur.m@gmail.com ***")
    print("*** DATA SCIENCE ACADEMY - PROFESSOR DANIEL MENDES ***")
    print("\nQual Operação Matemática Deseja Realizar?")
    print("Informe a Opção Numérica")
    print("1 -> Soma")
    print("2 -> Subtração")
    print("3 -> Multiplicacao")
    print("4 -> Divisão")
    print("9 -> Encerrar")
    return;

def soma(num1,num2):
    result = num1 + num2
    return result;

def subtracao(num1,num2):
    result = num1 - num2
    return result;

def multiplicacao(num1,num2):
    result = num1 * num2
    return result;

def divisao(num1,num2):
    try:
        result = num1 // num2
    except ZeroDivisionError:
        result == 0
    return result;

var_loop = 0
    
while var_loop == 0:
    tela()
    var_opcao = input("Estou aguardando sua opção:")
    
    if (var_opcao != '1') and (var_opcao != '2') and (var_opcao != '3') and (var_opcao != '4') and (var_opcao != '9'):
        print("Opção Inválida")
        
    #soma
    if var_opcao == '1':

        try:
            num1 = int(input("Informe o Primeiro Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        try:
            num2 = int(input("Informe o Segundo Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        var_resultado = soma(num1,num2)
        print("")
        print("O Resultado da Soma : " + str(var_resultado))
        print("")
        print("")
        
    #subtração
    if var_opcao == '2':

        try:
            num1 = int(input("Informe o Primeiro Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        try:
            num2 = int(input("Informe o Segundo Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        var_resultado = subtracao(num1,num2)
        print("")
        print("O Resultado da Subtração : " + str(var_resultado))
        print("")
        print("")
    
    
    #multiplicacao
    if var_opcao == '3':

        try:
            num1 = int(input("Informe o Primeiro Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        try:
            num2 = int(input("Informe o Segundo Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        var_resultado = multiplicacao(num1,num2)
        print("")
        print("O Resultado da Multiplicação : " + str(var_resultado))
        print("")
        print("")
    
    #divisão
    if var_opcao == '4':

        try:
            num1 = int(input("Informe o Primeiro Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        try:
            num2 = int(input("Informe o Segundo Número : "))
        except ValueError:
            print('\nEntrada Inválida')
            continue

        var_resultado = divisao(num1,num2)
        
        print("")
        print("O Resultado da Divisão : " + str(var_resultado))
        print("")
        print("")
    
    if var_opcao == '9':
        var_loop = int(var_opcao)
    
print("Obrigado por participar do experimento")
print("agradecimentos a DSA - Data Science Academy - Curso Python")
quit()
      
     





