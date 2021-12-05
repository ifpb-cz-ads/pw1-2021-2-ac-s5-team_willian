velocidade = int(input('Informe a velocidade do carro:'));
multa = 0;
if (velocidade > 80):
    while (velocidade > 80):
      multa = multa + 5
      velocidade = velocidade - 1
    print('A multa será de R$',multa)
else:
     print('O veiculo está na velocidade adequada');
