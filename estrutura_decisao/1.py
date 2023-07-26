# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Insira um número: "))
n2 = float(input("Insira outro número: "))

if n1 > n2:
    print(f"O primeiro número ({n1}) é maior")
elif n1 == n2:
    print("Os números são iguais.")
else:
    print(f"O segundo número ({n2}) é maior.")
