# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.


def ano_bissexto(ano):
    if ano % 4 == 0:
        return True
    else:
        return False


mes_31 = [1, 3, 5, 7, 8, 10, 12]

while 1:
    data = input("Insira uma data (dd/mm/aaaa): ")
    dia, mes, ano = data.split("/")

# validar formato dd/mm/aaaa

    if len(dia) > 2 or len(mes) > 2 or len(ano) > 4:
        print("Formato inválido.")
        continue

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

# validar mês

    if mes > 12 or mes < 1:
        print("Mês inválido.")
        continue

# validar dia

    if mes == 2 and ano_bissexto(ano) is True and dia > 29:
        print("Data inválida. Repita")
    elif mes == 2 and ano_bissexto(ano) is False and dia > 28:
        print("Data inválida. Repita")
    elif mes not in mes_31 and dia >= 31 or mes in mes_31 and dia > 31:
        print("Data inválida. Repita")
    else:
        print("".join(data))
        break
