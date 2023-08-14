# Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito
#      Entre 9.0 e 10.0        A
#      Entre 7.5 e 9.0         B
#      Entre 6.0 e 7.5         C
#      Entre 4.0 e 6.0         D
#      Entre 4.0 e zero        E

#    O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
# ou “REPROVADO” se o conceito for D ou E.

notas = []

n = int(input("Quantas notas deseja inserir: "))

for i in range(1, (n+1)):
    while 1:
        a = (float(input(f"Insira a {i}ª nota: ")))
        if a >= 0 and a <= 10:
            notas.append(a)
            break
        else:
            print("Nota inválida. Insira novamente.")

media = sum(notas)/len(notas)
if 0 <= media < 4:
    conceito = "E"
elif 4 <= media < 6:
    conceito = "D"
elif 6 <= media < 7.5:
    conceito = "C"
elif 7.5 <= media < 9:
    conceito = "B"
elif 9 <= media <= 10:
    conceito = "A"

print(f"Notas: {notas}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")

if conceito in "ABC":
    print("Aprovado!")
else:
    print("Reprovado.")
