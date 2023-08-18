# 5. Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir
# a operação.

while 1:
    pop_a = int(input("Insira a população A: "))
    pop_b = int(input("Insira a população B: "))
    if pop_a > pop_b:
        print("A população A deve ser menor que a população B. Repita.")
    else:
        break

while 1:
    cresc_a = float(input("Insira a taxa de crescimento da população A: "))
    cresc_b = float(input("Insira a taxa de crescimento da população B: "))
    if cresc_b > cresc_a:
        print("Com essas taxas de crescimento, as população não se igualarão.")
    else:
        break

ano = 0
cresc_a = 1 + cresc_a/100
cresc_b = 1 + cresc_b/100

while pop_a <= pop_b:
    pop_a *= cresc_a
    pop_b *= cresc_b
    ano += 1

print(pop_a)
print(pop_b)
print(ano)
