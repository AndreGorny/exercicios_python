# Faça um Programa que leia três números e mostre o maior e o menor deles.

n = []

for i in range(3):
    n.append(float(input(f"Insira o {i+1}º número: ")))

print(f"{max(n)} é o maior dos 3 número digitados. {min(n)} é o menor.")
