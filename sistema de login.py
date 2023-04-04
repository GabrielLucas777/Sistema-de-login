from getpass import getpass
from time import sleep
import os

print('\tSISTEMA DE LOGIN')

escolha = input(
    'Escolha uma opção:\n 1 - [Fazer login]\n 2 - [Cadastrar novo usuario]')
while True:
    if escolha == '1':
        usuario = input("Insira seu nome: ")
        print(f'Bem-vindo ao sistema, {usuario}!')
    elif escolha == '2':
        nome_cadastro = input('Insira o nome a ser cadastrado: ')
        senha_cadastro = getpass('Digite a senha que deseja cadastrar: ')
        with open("usuario.txt", 'w') as arquivo:
            arquivo.write(nome_cadastro + ',' + senha_cadastro + os.linesep)
            print(f'Usuario {nome_cadastro} cadastrado com sucesso!')
    limite_tentativas = 3
    tentativas = 0
    while tentativas < limite_tentativas:
        senha = getpass('Digite sua senha: ')
        senha_acesso = '20031995'
        if senha == senha_acesso:
            print('Analisando sua senha, aguarde...')
            sleep(1)
            print('ACESSO EFETUADO COM SUCESSO!')
            break
        else:
            print('Analisando sua senha, aguarde...')
            sleep(1)
            print('SENHA INCORRETA, TENTE NOVAMENTE')
            tentativas += 1
    if tentativas == limite_tentativas:
     print('VOCÊ EXCEDEU O LIMITE MAXIMO DE TENTATIVAS!')
     break
