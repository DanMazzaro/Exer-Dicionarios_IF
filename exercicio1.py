# Faça um programa que possua um dicionário, adicione elementos ao
# dicionário e os mostre na tela. O dicionário deve ser criado vazio.

dicionario = {}

opcao = int(input('quer criar alguma chave? digite 1 para sim e 2 para nao: '))

while True:

    if opcao == 2:
        break

    elif opcao == 1:
        chave = input('de um nome a chave que quer add ao dicionario: ')
        valor = input('qual o valor que voce quer add na chave do dicionario: ')
        dicionario[chave] = valor
        
    opcao = int(input('quer criar alguma chave? digite 1 para sim e 2 para nao: '))


print(dicionario)