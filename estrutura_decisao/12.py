"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que
os descontos são do Imposto de Renda, que depende do salário bruto (conforme
tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas
no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

    Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) Sindicato (3%)              : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""

while 1:
    valor = float(input("Insira o valor da hora: "))
    horas = int(input("Insira a quantidade de horas trabalhadas: "))

    if valor <= 0 or horas <= 0:
        print("Valor inválido. Repita.")
    else:
        break

salario_bruto = valor * horas
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

# calcular IR

if salario_bruto <= 900:
    aliquota = 0
elif salario_bruto <= 1500:
    aliquota = 0.05
elif salario_bruto <= 2500:
    aliquota = 0.1
elif salario_bruto > 2500:
    aliquota = 0.2

print("="*80)
print(f"  Salário Bruto: (R${valor:.2f} x {horas})"
      f"      : R$ {salario_bruto:,.2f}")
print(f"  (-) IR ({aliquota*100:.0f}%)"
      f"      : R$ {salario_bruto*aliquota}")
print(f"  (-) Sindicato (3%)"
      f"      : R$ {sindicato:,.2f}")
print(f"FGTS (11%)              : R$ {fgts:,.2f}")
print(f"Total de descontos                   "
      f"           : R$ {salario_bruto}")
print("="*80)
