# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
kwh = int(input('Adicione a quantidade em Kwh consumida: '))
tipo = input( " (r) para residencial \n (c) para subtracão \n (i) para industrial \n 'Adicione o tipo de instalação:")
if (tipo == "r"):
    if(kwh<=500):
        result = (kwh * 0.40);
        print("O valor a pagar é de ",result);
    elif(kwh>500 and kwh<1000):
        result = (kwh * 0.65);
        print("O valor a pagar é de", result);
    else:
        print("Valor de kwh e tipo de instalação não coincidem")
if (tipo == "c"):
    if(kwh<=1000 and kwh > 500):
        result = (kwh * 0.55);
        print("O valor a pagar é de ",result);
    elif(kwh>1000 and kwh<5000):
        result = (kwh * 0.60);
        print("O valor a pagar é de", result);
    else:
        print("Valor de kwh e tipo de instalação não coincidem")
if (tipo == "i"):
    if(kwh>1000 and kwh<=5000):
        result = (kwh * 0.55);
        print("O valor a pagar é de ",result);
    elif(kwh>5000):
        result = (kwh * 0.60);
        print("O valor a pagar é de", result);
    else:
        print("Valor de kwh e tipo de instalação não coincidem")