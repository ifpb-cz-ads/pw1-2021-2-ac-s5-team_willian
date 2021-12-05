def emprestimoCasa():
    valorCasa = int(input('Informe o valor da casa a comprar: '))
    salario = int(input('Informe o salário: '));
    anos = int(input('Informe a quantidade de anos a pagar: '));
    meses = (anos * 12);
    prestacao = (valorCasa / meses);
    parteSalario = (salario * 30 / 100);
    if (prestacao > parteSalario):
        print("Emprestimo aprovado.");
    if (prestacao < parteSalario):
        print("Emprestimo não será aprovado.");


emprestimoCasa();