# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:

#   a) o produto do dobro do primeiro com metade do segundo .
#   b) a soma do triplo do primeiro com o terceiro.
#   c) o terceiro elevado ao cubo.

n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))
n3 = float(input("Insira um número real: "))

a = (2*n1) * (n2/2)
b = 3*n1 + n3
c = n3**3

print(f"O produto do dobro do primeiro com metade do segundo é {a}")
print(f"A soma do triplo do primeiro com o terceiro é {b}")
print(f"O terceiro elevado ao cubo é {c}")
