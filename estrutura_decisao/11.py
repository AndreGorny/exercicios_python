"""11. As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
    a. Salários até R$ 280,00 (incluindo): Aumento de 20%
    b. Salários entre R$ 280,00 e R$ 700,00: Aumento de 15%
    c. Salários entre R$ 700,00 e R$ 1500,00: Aumento de 10%
    d. Salários de R$ 1500,00 em diante: Aumento de 5%
Após o aumento ser realizado, informe na tela:
    a. O salário antes do reajuste;
    b. O percentual de aumento aplicado;
    c. O valor do aumento;
    d. O novo salário, após o aumento."""

while 1:
    salario = float(input("Insira o salário atual: "))
    if salario <= 0:
        print("Valor inválido. Informe novamente.")
    else:
        break

# aumento = None

if salario > 0 and salario <= 280:
    aumento = 0.2
elif salario > 280 and salario <= 700:
    aumento = 0.15
elif salario > 700 and salario <= 1500:
    aumento = 0.10
elif salario > 1500:
    aumento = 0.05
# else:
#    print("Valor inválido")


# valor_aumento = salario * aumento
# novo_salario = salario + aumento
# if aumento:
print("="*50)
print(f"Salário atual: R${salario:,.2f}")
print((f"Percentual de aumento: {aumento * 100:.0f}%"))
print(f"Valor do aumento: R${salario * aumento:,.2f}")
print(f"Novo salário: R${salario * (1 + aumento):,.2f}")
print("="*50)
