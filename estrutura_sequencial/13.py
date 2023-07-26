# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:

#    Para homens: (72.7*h) - 58
#    Para mulheres: (62.1*h) - 44.7

while 1:
    h = float(input("Insira a altura: "))
    s = input("Insira o sexo (M / F): ").upper()

    if s != "M" and s != "F":
        print("Sexo inválido. Tente novamente inserindo apenas M ou F.")

    else:
        break


if s == "M":
    peso = 72.7*h - 58
    print(f"O peso ideal é de {round(peso, 2)}kg.")

if s == "F":
    peso = 62.1*h - 44.7
    print(f"O peso ideal é de {round(peso, 2)}kg.")
