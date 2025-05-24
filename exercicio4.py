# Faça um programa, utilizando dicionários, que tenha as seguintes
# informações: nome, idade, cpf, endereço e rg. Peça ao usuário para digitar as
# informações. Mostre na tela primeiramente somente o dicionário, depois
# somente as chaves e depois somente os valores.


nome = input('qual o nome: ')
idade = int(input('qual a idade: '))
cpf = int(input('qual o cpf: '))
endereco = input('qual o endereço: ')
rg = int(input('qual o rg: '))


dicionario = {
    'nome': [nome],
    'idade': [idade],
    'cpf': [cpf],
    'endereço': [endereco],
    'rg': [rg] 
}


x = dicionario.keys()
y = dicionario.values()

print(' ')
print(dicionario)
print(' ')
print(x)
print(' ')
print(y)
print(' ')
