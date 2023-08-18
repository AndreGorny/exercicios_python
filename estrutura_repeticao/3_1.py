clientes = []

while True:
    cliente = {}

    while True:
        nome = input("Nome: ")
        if len(nome) <= 3:
            print("Nome muito curto. Repita.")
        else:
            cliente["nome"] = nome
            break

    while True:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 150:
            print("Idade inválida. Repita.")
        else:
            cliente["idade"] = idade
            break

    while True:
        salario = float(input("Salário: "))
        if salario < 0:
            print("Salário inválido. Repita.")
        else:
            cliente["salario"] = salario
            break

    while True:
        sexo = input("Sexo (M/F): ").upper()
        if sexo not in "MF":
            print("Sexo inválido. Insira M ou F.")
        else:
            cliente["sexo"] = sexo
            break

    while True:
        estado_civil = input("Estado civil (c, s, v ou d): ").upper()
        if estado_civil not in "CSVD":
            print("Insira apenas a inicial(C- Casado, S- Solteiro)"
                  "V- Viúvo ou D- Divorciado")
        else:
            cliente["estado_civil"] = estado_civil
            break

    clientes.append(cliente)

    continuar = input("Deseja adicionar outro cliente? (S/N): ").upper()
    if continuar != "S":
        break

print(clientes)
