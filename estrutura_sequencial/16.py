# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total.

from math import ceil

area = float(input("Insira a área a ser pintada (em metros quadrados): "))
litros = area / 3
latas = ceil(litros / 18)
valor = latas*80

print("="*80)
print(f"Área: {area}m²")
print(f"Quantidade de tinta necessária: {litros:.2f} litros.")
print(f"Quantidade de latas necessárias: {latas} latas de 18 litros.")
print(f"Considerando o valor de R$80.00 por lata, o custo total será de"
      f" R${valor:,.2f}.")
print("="*80)
