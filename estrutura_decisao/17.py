# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.


def ano_bissexto(ano):
    if ano % 4 != 1:
        return True
    else:
        return False


mes_31 = [1, 3, 5, 7, 8, 10, 12]

while 1:
    data = input("Insira uma data (dd/mm/aaa): ")
    dia, mes, ano = data.split("/")

    if ano_bissexto(ano) is True:
        if mes == 2 and dia > 29:
            print("Data inválida. Repita")

"""    if mes in mes_31 and dia > 30:
        print("Data inválida")
    elif mes == 2 and dia > 29:
        pass

    dia, mes, ano = data.split("/")

print(dia, mes, ano)"""

#corrije saporra