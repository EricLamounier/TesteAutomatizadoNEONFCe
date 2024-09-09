from lib import *
from validacao import *

def cadastro_pessoa(pessoa):
    press('f2')
    
    copy(pessoa['doc']) # copia CPF/CNPJ

    write(pessoa['tipoPessoa'])
    press('enter')

    hotkey('ctrl', 'v') # CPF/CNPJ
    press(['enter', 'enter', 'enter'])

    keyboard.write(pessoa['nome']) # Nome
    press('enter')

    keyboard.write(pessoa['nomeUsual']) # Nome usual
    press('enter')

    write(pessoa['cep']) # CEP
    sleep(0.5)
    press('enter')

    keyboard.write(pessoa['logradouro']) # Logradouro
    sleep(0.5)
    press('enter')

    write(pessoa['numero'])
    sleep(0.5)
    press(['enter', 'enter'])

    keyboard.write(pessoa['bairro']) # Bairro
    sleep(0.5)
    press('enter')

    press('enter')

    write(pessoa['municipio']) # Município
    sleep(0.5)

    press('enter') # Seleciona o municipio
    sleep(0.5)

    press('alt') # Aba Pessoa Física
    sleep(0.5)
    press('p')

    sleep(0.5)
    press(['enter', 'enter'])

def logar_com_usuario(usuario):
    sleep(1)

    hotkey('ctrl', 'f4') # Sai do NEO
    sleep(2)


    write(dados.banco['nomeBanco']) # Digita o nome do banco do Teste Automatizado do NEOPLUS
    press('enter') # Seleciona o banco

    write(usuario['login']) # Digita o Login
    press('enter')

    write(usuario['senha']) # Digita a Senha
    press('enter') # Tenta entrar

    sleep(4) # Aguarda entrar

    hotkey('ctrl', 'f10')
    sleep(0.1)
    hotkey('ctrl', 'f6')
    press('esc')

    chk = ''
    chk = paste()

    if chk.lower() != 'pp014': # Erro
         return True # Para a execucao
    return False

def cadastro_classificacao_cliente(classificacao):
    sleep(0.5)
    press('f2')

    keyboard.write(classificacao['classificacao']) # Adiciona o nome da classificacao
    press(['enter', 'enter'])

    keyboard.write(classificacao['mensagem']) # Campo mensagem
    press('enter')

    write(classificacao['bloqueiaVendaAPrazo'])
    press('enter')

    write(classificacao['bloqueiaAtraso'])
    press('enter')

    if classificacao['bloqueiaAtraso'] in ['avisa', 'bloqueia']:
        keyboard.write(classificacao['mensagem'])
        press('enter')
    write(classificacao['bloqueiaLimiteCredito'])

    if classificacao['bloqueiaLimiteCredito'] in ['avisa', 'bloqueia']:
        press('enter')
        keyboard.write(classificacao['mensagem'])

    sleep(1)

    clicaEsquerdo(849, 608) # Replica para todas as guias
    sleep(0.5)
    clicaEsquerdo(849, 608)
    sleep(0.6)

    press('insert') # Salva
    sleep(0.8)

    chk = valida_grid(classificacao['classificacao'], 'centroDireito', classificacao['validacao'])
    sleep(0.5)

    press('esc')

    return chk # Nao deu erro

def cadastro_cliente_5(cliente):
    sleep(0.3)
    press('insert') # Sair do filtro
    sleep(0.5)
   
    press('f2') # Novo
    sleep(0.5)

    copy(cliente['doc']) # copia CPF/CNPJ

    write(cliente['tipoPessoa'])
    press('enter')

    hotkey('ctrl', 'v') # CPF/CNPJ
    press(['enter', 'enter', 'enter'])

    keyboard.write(cliente['nome']) # Nome
    press('enter')

    keyboard.write(cliente['nomeUsual']) # Nome usual
    press('enter')

    write(cliente['cep']) # CEP
    sleep(0.5)
    press('enter')

    keyboard.write(cliente['logradouro']) # Logradouro
    press('enter')

    write(cliente['numero'])
    press(['enter', 'enter'])

    keyboard.write(cliente['bairro']) # Bairro
    press('enter')

    press('enter')
    write(cliente['municipio']) # Município
    sleep(0.2)

    press('enter') # Seleciona o municipio
    sleep(0.2)

    for _ in range(4):
        press('enter')

    press('space')
    sleep(0.2)
    press('enter')
    sleep(0.2)
    press('space')
    sleep(0.2)
    press('enter')
    sleep(0.2)

    sleep(0.1)
    press('enter')
    sleep(0.2)
    write('3')
    hotkey('shift', 'tab')
    sleep(0.3)

    press('alt') # Aba Cliente
    sleep(0.5)
    press('l')
    sleep(0.5)
    
    write('2') # Limite de credito
    press('enter')

    write('100') # Limite de credito
    sleep(0.5)
    press('insert') # Salva a pessoa
    sleep(0.3)

    chk = valida_grid(cliente['doc'], 'centroDireito', cliente['validacao'], [20, 21])

    sleep(0.3)
    press('esc')

    return chk # Nao deu erro