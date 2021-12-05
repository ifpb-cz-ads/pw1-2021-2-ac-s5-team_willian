def precoDistancia():
    distancia = float(input('Informe a distancia em KM: '))
    if (distancia <= 200):
        valor = (distancia * 0.5);
        print('O valor da distancia sera de', valor);
    elif (distancia > 200):
        valor = (distancia * 0.45);
        print('O valor da distancia sera de', valor);


precoDistancia();
