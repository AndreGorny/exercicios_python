import pathlib

""" 01. Faça um programa que leia um arquivo texto contendo uma
    lista de endereços IP e gere um outro arquivo, contendo um
    relatório dos endereços IP válidos e inválidos.
    O arquivo de entrada possui o seguinte formato:
        200.135.80.9
        192.168.1.1
        8.35.67.74
        257.32.4.5
        85.345.1.2
        1.2.3.4
        9.8.234.5
        192.168.0.256
    O arquivo de saída possui o seguinte formato:
        [Endereços válidos:]
        200.135.80.9
        192.168.1.1
        8.35.67.74
        1.2.3.4

        [Endereços inválidos:]
        257.32.4.5
        85.345.1.2
        9.8.234.5
        192.168.0.256
"""


def validar_ip(ip):
    numeros = ip.split(".")
    if len(numeros) != 4:
        return False
    for numero in numeros:
        if not numero.isdigit() or int(numero) < 0 or int(numero) > 255:
            return False
    return True


BASE_DIR = pathlib.Path(__file__).parent

arquivo = open(BASE_DIR / "ips.txt", "r")
ips = arquivo.readlines()
arquivo.close()
print(ips)

validos = []
invalidos = []

for linha in ips:
    ip = linha.strip()
    if validar_ip(ip):  # validar_ip(ip) == True OU validar_ip(ip) is True
        validos.append(ip + "\n")
    else:
        invalidos.append(ip + "\n")

saida = open(BASE_DIR / "ips_relatorio.txt", "w")
saida.write("[Endereços válidos:]\n")
saida.writelines(validos)
saida.write("\n[Endereços inválidos:]\n")
saida.writelines(invalidos)
saida.close()
