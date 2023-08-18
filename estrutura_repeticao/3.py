# Faça um programa que leia e valide as seguintes informações:

#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd';

clientes = []

while 1:
    while 1:
        nome = input("Nome: ")
        if len(nome) <= 3:
            print("Nome muito curto. Repita.")
        else:
            break

    while 1:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 150:
            print("Idade inválida. Repita.")
        else:
            break

    while 1:
        salario = float(input("Salário: "))
        if salario < 0:
            print("Salário inválido. Repita.")
        else:
            break

    while 1:
        sexo = input("Sexo (M/F): ").upper()
        if sexo not in "MF":
            print("Sexo inválido. Insira M ou F.")
        else:
            break

    while 1:
        estado_civil = input("Estado civil (c, s, v ou d): ").upper()
        if estado_civil not in "CSVD":
            print("Insira apenas a inicial(C- Casado, S- Solteiro)"
                  "V- Viúvo ou D- Divorciado")
        else:
            break

    clientes.append({"nome": nome,
                     "idade": idade,
                     "salario": salario,
                     "sexo": sexo,
                     "estado_civil": estado_civil
                     })

    if input("Nova entrada? S/N").upper() == "N":
        break

print(clientes)
