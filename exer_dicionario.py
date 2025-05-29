while True:
    print('menu de atividades:')
    print('atividade 1')
    print('atividade 2')
    print('atividade 3')
    print('atividade 4')
    print('atividade 5')

    opcao = (input('escolha uma atividade digitando um numero de 1 a 5: '))

    if opcao == '1':
        
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

    elif opcao == '2':

        dicionario = {}

        for i in range(3):
            produto = input('qual o nome do produto? ')
            preço = int(input('digite o preço do produto? '))
            dicionario[produto] = preço

        print(dicionario)


    elif opcao == '3':

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


    elif opcao == '4':

        nome = input('qual o nome: ')
        idade = int(input('qual a idade: '))
        cpf = int(input('qual o cpf: '))
        endereco = input('qual o endereço: ')
        rg = int(input('qual o rg: '))


        dicionario = {
            'nome': nome,
            'idade': idade,
            'cpf': cpf,
            'endereço': endereco,
            'rg': rg
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



    elif opcao == '5':

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

else:
    print('erro tente novamente')