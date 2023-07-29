"""Utilizando tratamento de exceções, crie um programa que, dado um valor
inteiro informado pelo usuário, retorne a divisão de 1 por este. Se o valor
informado for zero, o programa deve informar “Infinito” como resultado.
Caso o valor informado não seja um número, o programa deve informar o usuário
e continuar solicitando valores até que este seja."""


def dividir(numero):
    numero = int(numero)
    return 1 / numero


while 1:
    numero = (input("Informe um número inteiro: "))

    if not numero.isdigit():
        print("Não é um numero inteiro. Insira novamente.")
    else:
        break

try:
    divisao = dividir(numero)
except ZeroDivisionError:
    print("Não pode ser dividido por zero.")
else:
    print(divisao)
