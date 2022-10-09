import re 

def grava_contas(contas):
    with open(NOME_ARQUIVO, "w") as arq:
        for conta in contas:
            arq.write(str(conta[0]) + ";" + conta[1] + ";" + str(conta[2]) + "\n")
    print("Arquivo gravado")            

def le_contas(contas):
    contas = []
    with open(NOME_ARQUIVO, "r") as arq:
        conta = arq.readline()
        while (conta != ""):
            conta = conta.strip("\n")
            conta = conta.split(";")
            conta[0], conta[2] = int(conta[0]), float(conta[2])
            contas.append(conta)
            conta = arq.readline()
    return contas

def valida_float():
    dado_ok = False
    while not dado_ok:
        try:
            num = float(input())
            dado_ok = True
        except (ValueError):
            print('Caractere inválido, por favor coloque um número')
    return num

def valida_string(): 
    pattern = "[0-9!@#$%¨&*()/+-]"
    nome = input()
    while (re.search(pattern, nome)):
        print('Caracteres Inválidos')
        nome = input()
    return nome
    
def valida_inteiro():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input(''))
            dado_ok = True
        except (ValueError):
            print('Caractere inválido, coloque um número inteiro')
    return num

def menu():
    print('Olá, bem vindo ao Conta-Banco, escolha uma das seguintes opções:')
    print('Digite 1 para para criar uma nova conta ')
    print('Digite 2 para alterar o saldo ')
    print('Digite 3 para excluir uma conta ')
    print('Digite 4 para ver relatórios gerenciais ')
    print('Digite 5 para sair deste programa ')
    num = valida_inteiro()
    return num

def inclusao_conta():
    print('Digite o número de sua nova conta abaixo:')
    conta_num = valida_inteiro()
    while search_conta_inclusao(contas, conta_num):
        print('Este número de conta já existe, por favor escolha outro. ')
        conta_num = valida_inteiro()
    print('Número de conta disponível!')
    return conta_num

def search_conta_inclusao(contas, num_conta):    
    search_ok = False
    for conta in contas:
        if (conta[0] == num_conta):
            search_ok = True
            break
    return search_ok
    
def inclusao_saldo():
    print('Digite abaixo o seu saldo: ')
    saldo = valida_float()
    while (saldo < 0):
        print ('Por favor, coloque um saldo maior ou igual a 0.')
        saldo = valida_float()
    print('Sucesso!')
    return saldo

def inclusao_nome_test():
    print('Coloque abaixo seu nome e sobrenome, por favor (Ex: "Maria Matos").')
    nome = valida_string()
    car_nome = nome.split(' ')
    while len(car_nome) <= 1:
        print('Por favor coloque nome e sobrenome separados:')
        nome = valida_string()
        car_nome = nome.split(' ')
    return nome

def add_account(contas):
    conta_num = inclusao_conta()
    conta_nome = inclusao_nome_test()
    conta_saldo = inclusao_saldo()
    nova_conta = [conta_num, conta_nome, conta_saldo]
    contas.append(nova_conta)
    print(nova_conta)
    print(contas)

def credito_debito_change():
    valid_options = (1, 2)
    while True:
        print('Para selecionar Crédito, digite 1:''\n''Para selecionar Débito, digite 2: ')
        option = valida_inteiro()
        if option in (valid_options):
            return option
        else:
            print('Opção inválida.')

def credito_debito_positivo():
    valor = valida_float()
    while (valor <= 0):
        print('Por favor, coloque um número maior que 0 para débito e crédito')
        valor = valida_float()
    return valor

def change_account(contas):
    print('Digite o número de sua conta abaixo:')
    conta_num = valida_inteiro()
    pos = find_conta_alterar_excluir(contas, conta_num)
    if (pos != -1):
        option = credito_debito_change()
        if (option == 1):
            print('Você selecionou a opção crédito. ') 
            print('Digite o valor que você deseja adicionar ao saldo: ')
            credito = credito_debito_positivo()
            contas[pos][2] += credito
            print(f'Você tem {contas[pos][2]} de saldo')
        elif (option == 2):
            print('Você selecionou a opção débito. ')
            print ('Digite o valor que você deseja debitar do saldo: ')
            debito = credito_debito_positivo()
            contas[pos][2] -= debito
            print(f'Você tem {contas[pos][2]} de saldo')
    else:
        print('Este número de conta não existe, tente novamente.')

def resp_delete(): 
    while True:
        resp = input('Você deseja mesmo excluir sua conta? Digite "S" para sim e "N" para não: ').upper()
        if resp == ('S'):
            return resp
        elif resp == ('N'):
            break
        else:
            print('Opção inválida: Digite "S" para sim e "N" para não')

def delete_account(contas):
    print('Digite o número da sua conta abaixo:')
    conta_num = valida_inteiro()
    pos = find_conta_alterar_excluir(contas, conta_num)
    if (pos!= -1):
        print(f'Bem vindo {contas[pos][1]}!')
        resp = resp_delete()
        if resp == ('S'):
            if (contas[pos][2] == 0):
                print (f'O usuário {contas[pos][1]} teve sua conta deletada.''\n''Obrigado por usar nosso serviço.')
                contas.remove(contas[pos])
                print(contas)
            else:
                print('Você tem saldo positivo, não podemos excluir sua conta.')
    else:
        print('Esta conta não existe')

def report_files_account():
    print('Relatório gerenciais''\n''Escolha uma das seguintes opções:')
    print('Digite 1 para para listar clientes com saldo negativo ')
    print('Digite 2 para listar clientes com saldo acima de um valor escolhido ')
    print('Digite 3 para listar todas as contas ')
    while True:
        num = valida_inteiro()
        if (num == 1):
            relatorios_negativo()
        elif (num == 2):
            relatorios_above_value()
        elif (num == 3):
            relatorios_all()
    return num

def relatorios_negativo():
    for i in range (len(contas)):
        if (contas[i][2] < 0):
            print(contas[i])

def relatorios_above_value():
    print('Digite um valor para listar todos os saldos acima:')
    value = valida_float()
    for i in range (len(contas)):
        if contas[i][2] > value:
            print(f'Cliente {contas[i][1]} possui saldo maior que o valor selecionado. ')

def relatorios_all():
    for conta in contas:
        all_accounts = conta[0], conta[1], conta[2]
        print(all_accounts)

def find_conta_alterar_excluir(contas, conta_num):
    pos = -1
    for i in range (len(contas)):
        if contas[i][0] == conta_num:
            pos = i
            break
    return pos

NOME_ARQUIVO = "contas.txt"
contas = []
contas = le_contas(contas)

while True:
    num = menu()
    if (num == 1):
        add_account(contas)
    elif (num == 2):
        change_account(contas)
    elif (num == 3):
        delete_account(contas)
    elif (num == 4):
        report_files_account()
    elif (num == 5):
        print('Obrigado! Volte sempre.')
        break
    else:
        print('\n''Digite um número válido de opção, por favor.''\n')

grava_contas(contas)
