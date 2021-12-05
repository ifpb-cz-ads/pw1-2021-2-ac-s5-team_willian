def maior(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max


def menor(num1, num2, num3):
    min = num1
    if num2 < min:
        min = num2
    if num3 < min:
        min = num3

    return min


def MaiorMenor():
    num1 = int(input('Informe um numero:'));
    num2 = int(input('Informe outro numero:'));
    num3 = int(input('Informe mais um numero:'));

    print("Maior: ", maior(num1, num2, num3));
    print("Menor: ", menor(num1, num2, num3));


MaiorMenor()
