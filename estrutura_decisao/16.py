# Faça um Programa que peça um número correspondente a um determinado ano e em
# seguida informe se este ano é ou não bissexto.

ano = int(input("Insira um ano qualquer: "))

if ano % 4 != 1:
    print("Ano bissexto")
else:
    print("Ano não é bissexto.")
