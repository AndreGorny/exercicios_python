# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produtos = {}

for i in range(3):
    produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço de {produto}: "))
    produtos[produto] = preco

print(produtos)

menor_preco = min(produtos.values())

# comprar = [i for i in produtos if produtos[i] == menor_preco]

comprar = []
for i in produtos:
    if produtos[i] == menor_preco:
        comprar.append(i)
    print(i)

print(comprar)
print(f"O produto de menor valor é {comprar[0]}, que custa "
      f"R${menor_preco:,.2f}.")
