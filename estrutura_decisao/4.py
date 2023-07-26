# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
alfa = "abcdefghijklmnopqrstuvwxyz".upper()

while 1:
    letra = input("Insira uma letra qualquer: ").upper()
    if letra not in alfa:
        print("Digitação errada. Tente novamente.")
    else:
        break

if letra in "AEIOU":
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
