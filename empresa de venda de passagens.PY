print('ALUNOS: \nAna Carolina Morelli Chaves e Luiz Gustavo Pinto Da Silva \nRA: \n23017617 e 23013028 ')

passagens = {}
count = 1
senha = 890

print('\n----------- BEM VINDOS A AIRWHERE --------------')

while count > 0:
    while True:
        try:
            digite_senha = int(input('\nDIGITE A SENHA PARA ENTRAR NO SISTEMA: '))
            if digite_senha == senha:
                print(f'\n-------- BEM VINDO AO SISTEMA DA AIRWHERE---------')
                break 
            else:
                print('\nSENHA INCORRETA')
        except ValueError:
            print('\nDIGITE UM VALOR VÁLIDO')
    while True:
        try: 
            opc = int(input('1. CADASTRAR VOO \n2. ALTERARA INFORMAÇÕES DE UM VOO \n3. APAGAR VOO \n4. BUSCAR VOOS'))
            break
        except ValueError:
            print('\nDIGITE UM VALOR VÁLIDO')

    if opc == 1:
        print('CADASTRO DE VOOS')
        while True:
            try:
                qtd_voos =  int(input('Quantos voos deseja cadastrar: '))
                for i in range(qtd_voos):
                    while True:
                        try:
                            cod_voo = int(input('DIGITE O CÓDIGO DO VOO: '))
                            break
                        except ValueError:
                            print('DIGITE UM VALOR VÁLIDO')
                    cidade_origem = input('DIGITE A CIDADE ORIGEM: ')
                    cidade_destino = input('DIGITE A CIDADE DESTINO: ')
                    while True:
                        try:
                            num_escalas = int(input(f'DIGITE QUANTAS ESCALAS O VOO DE CÓDIGO {cod_voo} TERÁ: '))
                            break
                        except ValueError:
                            print('DIGITE UM VALOR VÁLIDO')
                    for i in range (num_escalas):
                        cidade_escala = input('DIGITE AS CIDADES EM QUE OCORRERA A ESCALA: ')
                break
            except ValueError:
                print('\nDigite um valor inteiro')
        
    if opc == 2:
        print('ALTERAÇÃO DAS INFORMAÇÕES DO VOO')
    if opc == 3:
        print('APAGAR VOOS')
    if opc == 4:
        print('BUSCAR UM VOO')