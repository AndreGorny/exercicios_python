# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados
# formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for
#  maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

lados = []

for i in range(3):
    lados.append(int(input(f"Insira o {i+1}º lado do triângulo: ")))

print(f"Lados: {lados}")
# tipo = None

if sum(lados) - max(lados) > max(lados):
    if lados[0] == lados[1] == lados[2]:
        tipo = "equilátero"
    elif lados[1] == lados[2] or lados[0] == lados[1] or lados[0] == lados[2]:
        tipo = "isósceles"
    elif lados[0] != lados[1] and lados[1] != lados[2]:
        tipo = "escaleno"

    print(f"Essas medidas formam um triângulo {tipo}")

else:
    print("Essas medidas não formam um triângulo.")

# if tipo:
#    print(f"Essas medidas formam um triângulo {tipo}")
