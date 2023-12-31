# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:

#    salário bruto.
#    quanto pagou ao INSS.
#    quanto pagou ao sindicato.
#    o salário líquido.
#    calcule os descontos e o salário líquido, conforme a tabela abaixo:

#    + Salário Bruto : R$
#    - IR (11%) : R$
#    - INSS (8%) : R$
#    - Sindicato ( 5%) : R$
#    = Salário Liquido : R$

#    Obs.: Salário Bruto - Descontos = Salário Líquido.

vl_hora = float(input("Valor recebido por hora: R$"))
horas = int(input("Quantidade de horas trabalhadas: "))

salario_bruto = vl_hora * horas
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
ir = salario_bruto * 0.11

liquido = salario_bruto - inss - sindicato - ir

print("===============================================\n"
      f"   + Salário Bruto:    R${salario_bruto:,.2f}\n"
      f"   - IR (11%):         R${ir:,.2f}\n"
      f"   - INSS (8%):        R${inss:,.2f}\n"
      f"   - Sindicato (5%):   R${sindicato:,.2f}\n"
      f"   = Salário Líquido:  R${liquido:,.2f}\n"
      "===============================================")
