# Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso
# de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja
# inválida.


def converte_mes(mes):
    meses = ["0", "janeiro", "fevereiro", "março",
             "abril", "maio", "junho",
             "julho", "agosto", "setembro",
             "outubro", "novembro", "dezembro"
             ]
    return meses[mes]


data = input("Insira a data desejada: ")

data = data.split("/")
mes = int(data[1])

print(f"{data[0]} de {converte_mes(mes)} de {data[2]}")
