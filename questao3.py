def aumentoSalario():
    salario = int(input('Informe o salário: '))
    if (salario > 1250):
        salario = (salario * 10 / 100);
        print('O aumento do seu salário será de R$:', salario);
    else:
        salario = (salario * 15 / 100);
        print('O aumento do seu salário será de R$:', salario);


aumentoSalario();