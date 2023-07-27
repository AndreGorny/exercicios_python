
def pegar_preco(produto):
    return produto["preco"]


produtos = []

for i in range(1, 4):
    nome = input(f"Digite o nome do produto {i}: ")
    preco = float(input(f"Digite o preço do produto {nome}: "))
    produtos.append({"nome": nome, "preco": preco})

produto_mais_barato = min(produtos, key=lambda produto: produto["preco"])
nome, preco = produto_mais_barato.values()
print(nome)
print(preco)
