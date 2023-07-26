# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for i in range(3):
    numeros.append(int(input(f"Insira o {i+1}º número: ")))

ordenado = sorted(numeros)

print(numeros)
print(ordenado)
