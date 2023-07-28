import os

"""02. A ACME Inc., uma empresa de 500 funcionários, está
tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o administrador de rede
precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da internet, ele conseguiu
gerar o seguinte arquivo, chamado "usuarios.txt":
    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres.
A partir deste arquivo, você deve criar um programa que gere
um relatório, chamado "relatório.txt", no seguinte formato:
    ACME Inc.         Uso do espaço em disco pelos usuários
    -------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso

    1    alexandre       434,99 MB             16,85%
    2    anderson       1187,99 MB             46,02%
    3    antonio         117,73 MB              4,56%
    4    carlos           87,03 MB              3,37%
    5    cesar             0,94 MB              0,04%
    6    rosemary        752,88 MB             29,16%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados
armazenados em memória, caso sejam necessários, de forma a
agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes
deverá ser feita através de uma função separada, que será chamada
pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de
uma função, que será chamada pelo programa principal."""


# Função que converte bytes para megabytes
def bytes_para_megabytes(espaco_em_bytes):
    return espaco_em_bytes / (1024 * 1024)


# Função que calcula a porcentagem de espaço utilizado por cada usuário
def calcular_porcentagem(valor_individual, valor_total):
    return (valor_individual / valor_total) * 100


# Obtendo o diretório atual do arquivo em execução
BASE_DIR = os.path.dirname(__file__)

# Abrir o arquivo com os dados iniciais para leitura
arquivo = open("usuarios.txt", "r")
# Lê todas as linhas do arquivo para uma lista, cada valor da lista é uma
# linha (string)
linhas = arquivo.readlines()
# Fecha o arquivo após a utilização
arquivo.close()

# Cria uma lista de tuplas com o nome do usuário e o espaço utilizado em bytes
usuarios = []
total_espaco_utilizado = 0

for linha in linhas:
    # Separar o nome do usuário e o espaço utilizado em bytes
    nome, espaco = linha.split()
    espaco = int(espaco)
    # Adiciona uma tupla com nome do usuário e o espaço utilizado em bytes
    usuarios.append((nome, espaco))
    # Adiciona o espaço utilizado pelo usuário ao total do espaço do sistema
    total_espaco_utilizado += espaco

# Ordena a lista de usuários pelo espaço utilizado em ordem decrescente
usuarios = sorted(usuarios, key=lambda usuario: usuario[1], reverse=True)

# Cria o arquivo de relatório e abre para escrita
relatorio = open("relatorio.txt", "w")
# Escreve o cabeçalho do relatório
relatorio.write("ACME Inc. - Uso do espaço em disco pelos usuários\n")
relatorio.write("-" * 49 + "\n")
txt_nr = "Nr."
txt_usuario = "Usuário"
txt_espaco = "Espaço Utilizado"
txt_porcentagem_uso = "% do uso"
relatorio.write(
    f"{txt_nr:<5}{txt_usuario:<15}{txt_espaco:<21}{txt_porcentagem_uso:<8}\n\n"
)

# Escreve as informações do usuário no relatório
posicao = 0
for usuario, espaco_bytes in usuarios:
    # Convertendo o espaço utilizado em bytes para megabytes
    espaco_megabytes = bytes_para_megabytes(espaco_bytes)
    # Calculando a porcentagem do espaço utilizado pelo usuário atual
    porcentagem = calcular_porcentagem(espaco_bytes, total_espaco_utilizado)

    # Formatando as informações em strings
    txt_espaco_megabytes = f"{espaco_megabytes:.2f} MB"
    txt_porcentagem = f"{porcentagem:.2f} %"
    posicao += 1

    # Escreve as informações do usuário atual no relatório
    relatorio.write(
        f"{posicao:<5}{usuario:<15}{txt_espaco_megabytes:<21}"
        f"{txt_porcentagem:<8}\n"
    )

# Calcula e escreve as informações gerais no relatório
total_espaco_megabytes = bytes_para_megabytes(total_espaco_utilizado)
espaco_medio_megabytes = total_espaco_megabytes / posicao
relatorio.write(f"\nEspaço total ocupado: {total_espaco_megabytes:.2f} MB\n")
relatorio.write(f"Espaço médio ocupado: {espaco_medio_megabytes:.2f} MB")
relatorio.close()
