# Faça um programa, utilizando dicionários, que cadastre todos os
# integrantes de uma família. Cada integrante tem as seguintes informações:
# nome, idade, endereço e grau de parentesco. Para resolver esse exercício crie
# um dicionário aninhado. Mostre todo o dicionário na tela e peça para o usuário
# uma informação específica que queira de algum integrante. Siga as seguintes
# orientações: deve possuir um dicionário família, dentro desse dicionário deve
# ter o nome dos integrantes (cada nome também será um dicionário).

q_familia = int(input('quantas pessoas tem na familia: '))

familia = {}

for i in range(q_familia):
    nome = input(f'qual o nome do {i+1} membro da familia: ')

    idade = int(input(f'qual a idade do {nome} :' ))

    endereco = input(f'qual o endereço do {nome} :' )

    parentesco = input(f'qual o grau de parentesco do {nome}:' )


    dici_membro = {
        'nome' : nome,
        'idade': idade,
        'endereço' : endereco,
        'grau de parentesco' : parentesco   
    }
 
    familia[nome] = dici_membro


print(familia)


membro = input('de qual membro da familia voce quer informação: ')
info = input(f'que informaçao voce quer sobre {membro}, ex: nome, idade, endereço. grau de parentesco : ')


        
if membro in familia:
    if info in familia[membro]:
        print(f"{info} de {membro}: {familia[membro][info]}")
    else:
        print(f"A informação '{info}' não existe para {membro}.")
else:
    print(f"O membro '{membro}' não foi encontrado na família.")
