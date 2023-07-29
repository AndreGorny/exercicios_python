import pathlib

BASE_DIR = pathlib.Path(__file__).parent

try:
    arquivo = open(BASE_DIR / "teste.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()

    numero = int(conteudo)
    print(numero)
except FileNotFoundError as e:
    print(f"{type(e).__name__} - Arquivo não encontrado.")
except ValueError:
    print("O valor não pode ser convertido para int")
