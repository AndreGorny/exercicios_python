
cardapio = {
    100: {"produto": "Cachorro-quente", "preço": 1.2},
    101: {"produto": "Bauru Simples", "preço": 1.3},

}

pedido = {}
total_pedido = 0

while 1:
    codigo = int(input("Digite o código do produto (ou digite 0" 
                       "para encerrar): "))
    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade desejada: "))
    if quantidade < 1:
        print("Quantidade inválida.")
        continue

    produto = cardapio[codigo]["produto"]
    preco_unit = cardapio[codigo]["preço"]
    preco_total = preco_unit * quantidade

    pedido[produto] = {
        "quantidade": quantidade,
        "preco_unit": preco_unit,
        "preco_total": preco_total
    }
    total_pedido += preco_total

    print(f"{quantidade} x {produto} - R${preco_total:,.2f}")

print(f"\nTotal do Pedido: R${total_pedido:,.2f}")

print("Detalhes do pedido:")
for produto, detalhes in pedido.items():
    quantidade = detalhes["quantidade"]
    preco_unit = detalhes["preco_unit"]
    preco_total = detalhes["preco_total"]
    print(f"{quantidade}x {produto} - R${preco_total:,.2f}")
