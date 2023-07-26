# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês.

valor = float(input("Salário por hora: R$"))
tempo = int(input("Numero de horas trabalhadas: "))
salario = valor * tempo

print(f"Seu salário será de R${salario:,.2f}.")
