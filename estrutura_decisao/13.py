# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
# inválido.

while 1:
    n = int(input("Insira um número correspondente a um dia da semana: "))
    if n not in [1, 2, 3, 4, 5, 6, 7]:
        print("Número inválido, repita.")
    else:
        break

if n == 1:
    print("1 - Domingo")
elif n == 2:
    print("2 - Segunda")
elif n == 3:
    print("3 - Terça")
elif n == 4:
    print("4 - Quarta")
elif n == 5:
    print("5 - Quinta")
elif n == 6:
    print("6 - Sexta")
else:
    print("7 - Sábado")
