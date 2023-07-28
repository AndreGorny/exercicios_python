# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o
# tempo aproximado de download do arquivo usando este link (em minutos).

from math import ceil

tamanho = float(input("Insira o tamanho do arquivo (em MB): "))
velocidade = int(input("Insira a velocidade da internet (em Mbps): "))

# 1 megabyte = 8 megabit

tempo = tamanho / velocidade * 8

min = tempo / 60
seg = tempo % 60

print(f"O tempo de download será de {int(min)} minuto(s)"
      f" e {ceil(seg)} segundos.")
