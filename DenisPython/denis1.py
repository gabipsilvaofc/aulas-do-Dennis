
repetidor = True
while repetidor:
    oper = (input('Qual operação você deseja realizar \n (1)Soma \n (2)Subtração \n (3)Multiplicação \n (4)Divisão \n (5)Sair'))
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    if oper == '1':
        soma = (num1 + num2)
        print(soma)
    elif oper == '2':
        subtração = (num1 - num2)
        print(subtração)
    elif oper == '3':
        multiplicação = (num1 * num2)
        print(multiplicação)
    elif oper == '4':
        divisão = (num1 / num2)
        print(divisão)
    elif oper == '5':
        print("Até a próxima!")
    else:
        print("Erro")