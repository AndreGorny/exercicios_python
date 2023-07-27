"""arquivo = open("teste.txt", "w")
arquivo.write("Olá!\nTudo bem?")
arquivo.close()

print(arquivo)
"""

arquivo = open("teste.txt", "a")
arquivo.write("\nNova linha.")
arquivo.close()
