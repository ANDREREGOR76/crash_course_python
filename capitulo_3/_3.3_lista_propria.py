prompt = 'Vamos falar sobre meios de transporte?'
prompt += '\nEscolha um meio de transporte dentre as opções abaixo:'
prompt += '\n\tbicicleta'
prompt += '\n\tcarro'
prompt += '\n\tmetrô'
prompt += '\n\tônibus'
prompt += '\nPara sair do programa, digite "quit".\n\n'
transportes = ['bicicleta', 'carro', 'metrô', 'ônibus', 'quit']

mensagem = ''
while mensagem != 'quit':
    mensagem = input(prompt)
    if mensagem in transportes:
        if mensagem == 'bicicleta':
            print(f'Atualmente, a {transportes[0]} é considerado o meio de transporte mais utilizado no mundo\n\n')
        elif mensagem == 'carro':
            print(f'Você sabia que o ano de 1886 é considerado como o ano de nascimento do {transportes[1]} moderno?\n\n')
        elif mensagem == 'metrô':
            print(f'O primeiro sistema de {transportes[2]} do mundo foi o Metropolitan Railway, que era parcialmente subterrâneo e foi inaugurado como uma ferrovia convencional em 1863, mas agora faz parte do metrô de Londres.\n\n')
        elif mensagem == 'ônibus':
            print('O conceito de {transportes[3]} como modalidade de transporte público tem sua origem na cidade de Nantes, França.\n\n')
    else:
        print('\nVocê tem que escolher uma das opções!\n\n')
