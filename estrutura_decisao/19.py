# Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.

#    Observando os termos no plural a colocação do "e", da vírgula entre
# outros. Exemplo:
#    326 = 3 centenas, 2 dezenas e 6 unidades
#    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
# 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero_completo = int(input("Insira um número inteiro positivo: "))

unidade = numero_completo % 10
numero = (numero_completo - unidade) / 10
dezena = numero % 10
numero = (numero - dezena) / 10
centena = numero % 10
milhar = (numero - centena) / 10

unidade = int(unidade)
dezena = int(dezena)
centena = int(centena)
milhar = int(milhar)

if numero_completo >= 1000:
    if unidade == 1:
        un = "unidade"
    else:
        un = "unidades"

    if dezena == 1:
        dz = "dezena"
    else:
        dz = "dezenas"

    if centena == 1:
        cent = "centena"
    else:
        cent = "centenas"

    if milhar == 1:
        mil = "milhar"
    else:
        mil = "milhares"

    print(f"{numero_completo} - {milhar} {mil}, {centena} {cent}, "
          f"{dezena} {dz} e {unidade} {un}.")

elif numero_completo >= 100:
    if unidade == 1:
        un = "unidade"
    else:
        un = "unidades"

    if dezena == 1:
        dz = "dezena"
    else:
        dz = "dezenas"

    if centena == 1:
        cent = "centena"
    else:
        cent = "centenas"

    print(f"{numero_completo} - {centena} {cent}, {dezena} {dz} "
          f"e {unidade} {un}.")

elif numero_completo >= 10:
    if unidade == 1:
        un = "unidade"
    else:
        un = "unidades"

    if dezena == 1:
        dz = "dezena"
    else:
        dz = "dezenas"

    print(f"{numero_completo} - {dezena} {dz} e {unidade} {un}.")

else:
    if unidade == 1:
        un = "unidade"
    else:
        un = "unidades"

    print(f"{numero_completo} - {unidade} {un}.")

# print(f"{numero_completo} - {milhar} {mil}, {centena} {cent}, {dezena} {dz} "
#      f"e {unidade} { un}.")
