"""Faça um programa para a leitura de duas notas parciais
de um aluno.
O programa deve calcular a média alcaçada por aluno e apresentas:

    A mensagem "Aprovado" se a média alcanãda for maior ou igual a sete;
    A mensagem "Reprovado" se a média for menor do que sete;
    A mensagem "Aprovado Com distinção" se a média for igual a dez.
    """

notas = []

notas.append(float(input("Insira a 1ª nota: ")))
notas.append(float(input("Insira a 2ª nota: ")))

media = sum(notas) / len(notas)

print(notas)
print(media)

if media == 10:
    print(f"Média {media}. Aprovado com distinção!")
elif media >= 7:
    print(f"Média {media}. Aprovado!")
else:
    print(f"Média {media}. Reprovado.")

# Outra solução seria:

if media >= 7 and media < 10:
    print("Aprovado")
