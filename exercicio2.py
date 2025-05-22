# Faça um programa, utilizando Dicionários, que peça para o usuário inserir o
# nome de três produtos de mercado e seus respectivos preços e os mostre na
# tela.

dicionario = {}

for i in range(3):
    produto = input('qual o nome do produto? ')
    preço = int(input('digite o preço do produto? '))
    dicionario[produto] = preço

print(dicionario)
