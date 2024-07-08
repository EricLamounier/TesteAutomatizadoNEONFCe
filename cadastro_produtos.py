from lib import *
from dados import *

def cadastro_produto_padrao(produto):
    sleep(0.3)
    press('insert') # Sair do filtro

    sleep(0.7)
    hotkey('ctrl', 'tab') # Aba complementar

    sleep(0.5)
    hotkey('alt', 'p')

    sleep(1.8)
    press('enter') # Código de barras

    press('enter') # Código de fabricante

    keyboard.write(produto['nome']) # Preenche o nome
    press('enter')

    keyboard.write(produto['marca']) # Preenche a marca
    keyboard.press('enter')
    sleep(0.2)
    
    keyboard.write(produto['unidade']) # Preenche a unidade
    keyboard.press('enter')
    sleep(0.2)

    keyboard.write(produto['grupo']) # Preenche o subgrupo
    keyboard.press('enter')
    sleep(0.2)
    
    keyboard.write(produto['subgrupo']) # Preenche o subgrupo
    keyboard.press('enter')
    sleep(0.2)
    
    press(['enter', 'enter'])
    
    write(produto['venda']) # Preenche o preço de venda

    press('insert') # Salva

    sleep(0.5)

    press('esc') # Sair
    
    return False

def cadastro_produto(produto):
    sleep(0.3)
    keyboard.write(produto['nome'])
    sleep(0.2)
    press('insert') # Sai do filtro
    sleep(0.6)

    press('f2') # Novo
    sleep(2)

    write(produto['barras']) # Código de barras
    press('enter')

    press('enter') # Pula Código de fabricante

    keyboard.write(produto['nome']) # Preenche o nome
    press('enter')

    sleep(0.5)
    press(['enter', 'enter','enter', 'enter'])

    write(produto['controlaEstoque']) # Grade
    press(['enter', 'enter'])

    press('delete')
    write(produto['venda']) # Preenche o preço de venda
    sleep(0.9)

    press('alt')
    sleep(0.7)
    press('f') # Aba fiscal
    sleep(0.5)
    press('tab')

    write(produto['cfop'])
    press('tab')

    write(produto['cst'])
    press('tab')

    write('8')
    press('tab')

    write(produto['aliquotaICMS'])
    press('tab')

    write(produto['nfce'])
    press('tab')
    sleep(0.2)
    press('tab')

    if produto['cst'] == '900':
        press('tab')

    write('10011900')
    sleep(0.3)
    
    press('insert') # Salva
    sleep(0.5)

    chk = valida_grid('', produto['validacao'], 18)

    if chk:
        messagebox.showerror('Erro - Produto - ' + produto['cod'], ' Esperado: ' + str(produto['validacao']))

    sleep(0.5)
    press('esc')
    sleep(0.8)
    return chk

def ajustar_estoque(produto): # Ajusta estoque do produto variação
    sleep(0.3)
    keyboard.write(produto['nome'])
    sleep(0.2)
    press('insert') # Sai do filtro
    sleep(0.3)

    press('f9') # Ajustar estoque
    sleep(0.3)

    press(['down', 'down'])
    sleep(0.3)

    keyboard.write('1') # Preenche motivo do ajuste
    press('enter')

    write(produto['cod'])
    press('enter')
    
    write(produto['quantidadeEstoque']) # Preenche a quantidade
    press('enter')

    write(produto['ultimoCusto']) # Preenche último custo
    press('insert') # Salva

    if produto['controlaEstoque'] == 'grade':
        cadastro_variacao_produto(produto3Var1)
        cadastro_variacao_produto(produto3Var2)
        press('enter') # Salvar

    sleep(0.5)
    press('esc') # Sai
    sleep(0.6)

    chk = valida_grid('', produto['validacaoAjusteEstoque'], 18)
    if chk:
        messagebox.showerror('Erro - Ajuste Produto - ' + produto['cod'], 'Esperado: ' + str(produto['validacao']))
        return chk

    sleep(0.3)
    press('esc') # Sai

    return chk

def cadastro_variacao_produto(variacao):
    sleep(0.5)

    write(variacao['quantidade']) # Preenche a quantidade
    press('enter')  
    write(variacao['barras']) # Preenche barras
    press('enter')
    sleep(0.1)
    press('enter')
    sleep(0.1)
    press('enter') # Incluir    
    sleep(0.2)
    press('enter') # Incluir     

def cadastro_unidade_tributavel(unidadeTributavel):
    
    sleep(0.8)
    keyboard.write(unidadeTributavel['produto'])
    sleep(0.5)
    press('insert') # Sai do filtro
    sleep(0.8)
    """
    hotkey('ctrl', 'tab') # Complementar
    sleep(1)

    click(1099, 334) # Unidade Tributavel
    sleep(0.5)
    write('0')
    sleep(0.3)
    press('enter')
    sleep(0.5)
    press('f2') # Novo
    sleep(0.3)
    write(unidadeTributavel['unidade'])
    sleep(0.3)
    press('enter')
    write(unidadeTributavel['simbolo']) # Simbolo
    sleep(0.3)
    press('insert') # Salva
    sleep(0.5)
    press('f5')
    sleep(0.5)
    write(unidadeTributavel['barras'])
    sleep(0.2)
    press('enter')
    sleep(0.2)
    write(unidadeTributavel['quantidade'])
    sleep(0.2)
    press('insert')
    sleep(1)
    """

    # VALIDA PRODUTO
    chk = valida_grid('', unidadeTributavel['validacao'], 18)
    if chk:
        messagebox.showerror('Erro', 'Erro - Produto com Unidade Tributável Errada!')
        return True

    press('esc')
    sleep(1)
    print('oi')
    return True

    rastro = ''
    hotkey('ctrl', 'f6')
    rastro = paste()

    if rastro != '': 
        messagebox.showerror('Erro - Unidade Tributável', 'Ocorreu um erro ao cadastrar a unidade tribuável')
        return True
    return False

def valida_estoque_final(produtos):
    sleep(00.6)
    press('insert') # Sai do filtro
    sleep(0.5)

    for prod in produtos['produtos']:
        hotkey('shift', 'backspace')
        if valida_grid(prod['produto'], prod['validacao'], 18): 
            messagebox.showerror('Erro - Produto - ' + prod['produto'], 'Esperado: ' + str(prod['validacao']))
            return True
        
    press('esc')
    return False