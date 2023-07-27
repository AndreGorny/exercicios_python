# Reverso do número. Faça uma função que retorne o reverso de
#    um número inteiro informado.
#    Exemplo: 127 -> 721


def reverso(num):
    num = str(num)
    return int(num[::-1])


print(type(reverso(127)))
