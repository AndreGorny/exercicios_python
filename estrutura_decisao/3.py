# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

while 1:
    sexo = input("Insira o sexo (M/F): ").upper()
    if sexo in "MF":
        break
    else:
        print("Sexo inválido. Repita.")

if sexo == "M":
    print("Sexo Masculino.")
else:
    print("Sexo Feminino.")
