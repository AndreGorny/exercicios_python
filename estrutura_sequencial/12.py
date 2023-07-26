# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

h = float(input("Insira a altura: "))
peso = 72.7*h - 58

print(f"O peso ideal para essa pessoa é de {round(peso, 2)}kg.")
