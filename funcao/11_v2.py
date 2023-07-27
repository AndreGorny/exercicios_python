# Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso
# de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja
# inválida.


def data_por_extenso(data):
    dias_meses = {
        1: {"nome": "Janeiro", "dias": 31},
        2: {"nome": "Fevereiro", "dias": 28},
        3: {"nome": "Março", "dias": 31},
        4: {"nome": "Abril", "dias": 30},
        5: {"nome": "Maio", "dias": 31},
        6: {"nome": "Junho", "dias": 30},
        7: {"nome": "Julho", "dias": 31},
        8: {"nome": "Agosto", "dias": 31},
        9: {"nome": "Setembro", "dias": 30},
        10: {"nome": "Outubro", "dias": 31},
        11: {"nome": "Novembro", "dias": 30},
        12: {"nome": "Dezembro", "dias": 31}
    }

    partes_data = data.split("/")
    dia = int(partes_data[0])
    mes = int(partes_data[1])
    ano = int(partes_data[2])

    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        dias_meses[2]["dias"] = 29

    if dia < 1 or dia > dias_meses[mes]["dias"]:
        return None

    mes_extenso = dias_meses[mes]["nome"]
    return f"{dia} de {mes_extenso} de {ano}"


print(data_por_extenso("01/01/1950"))
