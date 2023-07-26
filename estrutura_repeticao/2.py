# Faça um programa que leia um nome de usuário e a sua senha e não aceite
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

while 1:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print("Usuário e senha não podem ser iguais. Tente novamente.")
    else:
        break

print("Cadastrado com sucesso")
