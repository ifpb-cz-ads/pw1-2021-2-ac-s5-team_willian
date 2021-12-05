num1 = int(input('Adicione um numero: '))
num2 = int(input('Adicione outro numero : '))
symbol = input( " (+) para soma \n (-) para subtracão \n (*) para multiplicação \n (/) para divisão. \n 'Adicione a operação:")
if (symbol == "+"):
    result = (num1 + num2);
    print("=",result)
elif (symbol == "-" ):
    result = (num1 - num2);
    print("=",result)
elif (symbol == "*"):
    result = (num1 * num2)
    print("=",result)
elif (symbol == "/"):
    result = (num1 / num2);
    print("=",result)
else:
   print("adicione um operador válido");