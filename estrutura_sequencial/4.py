# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

a = float(input("Insira a primeira nota: "))
b = float(input("Insira a segunda nota: "))
c = float(input("Insira a terceira nota: "))
d = float(input("Insira a quarta nota: "))

media = (a+b+c+d)/4
print(f"A média bimestral foi {media:.2f}.")
