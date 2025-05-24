#Faça um programa, utilizando dicionários, peça para o usuário inserir o
#nome dos três funcionários e mostre-os na tela. Posteriormente peça para o
#usuário demitir um funcionário e mostre os funcionários restantes na tela.


dicionario = {}

valor1 = input('qual o nome do 1 funcionario: ')
valor2 = input('qual o nome do 2 funcionario: ')
valor3 = input('qual o nome do 3 funcionario: ')

dicionario['funcionario1'] = valor1
dicionario['funcionario2'] = valor2
dicionario['funcionario3'] = valor3

print(dicionario)

demicao = input('escolha qual funcionario vai ser demitido, digite o nome do funcionario: ')

if demicao == valor1:
    print('o funcionario', valor1, 'foi demitido')
    del dicionario['funcionario1']
    print(dicionario)

elif demicao == valor2:
    print('o funcionario', valor2, 'foi demitido')
    del dicionario['funcionario2']
    print(dicionario)

elif demicao == valor3:
    print('o funcionario', valor3, 'foi demitido')
    del dicionario['funcionario3']
    print(dicionario)

else:
    print('nome do funcionario não reconhecido, certifique-se que foi escrito corretamente')

