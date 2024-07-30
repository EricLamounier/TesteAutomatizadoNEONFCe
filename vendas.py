from lib import *
from relatorios import *

def venda_avulsa_configurar_visualizar(void=''):
    maximizar_janela(0)
    click(613, 333) # Informe o produto
    sleep(0.2)
    
    press('f5') # Campo quantidade
    write('1') # Quantidade
    press('enter')
    write('1000000000016') # Produto 1
    press('enter')

    sleep(1)
    press('f9') # Finalizar Venda
    sleep(1)

    write('1') # Finalizadora Dinheiro
    press('enter')
    sleep(0.7)
    press(['tab', 'tab', 'tab']) # Campos visualizar

    xTop, yTop, xBottom, yBottom = 653, 612, 665, 624
    modulo = {
        'pasta': 'campos',
        'imagem': 'checked',
        'inicio': f'{xTop}x{yTop}',
        'fim': f'{xBottom}x{yBottom}'
    }

    sleep(0.4)
    if imagens_diferentes(modulo): #Marca
        press('space')
    press('tab')

    xTop, yTop, xBottom, yBottom = 757, 612, 769, 624
    modulo['inicio'] = f'{xTop}x{yTop}'
    modulo['fim'] = f'{xBottom}x{yBottom}'

    sleep(0.4)
    if imagens_diferentes(modulo): #Marca
        press('space')
    press('tab')

    xTop, yTop, xBottom, yBottom = 851, 612, 863, 624
    modulo['inicio'] = f'{xTop}x{yTop}'
    modulo['fim'] = f'{xBottom}x{yBottom}'

    sleep(0.4)
    if imagens_diferentes(modulo): #Marca
        press('space')

    press(['tab', 'tab', 'tab']) # Salvar
    sleep(0.2)
    press('enter') # Salvar
    sleep(10) # Abre a nota

    modulo = {
        'pasta': 'notas',
        'imagem': 'pdvavulso1',
        'inicio': '810x58',
        'fim': '1086x330'
    }

    chk = imagens_diferentes(modulo)
    sleep(0.5)

    press('esc')
    return chk

def dav_crediario(venda):
    press(['enter', 'enter', 'enter']) # Gera parcelas
    sleep(0.7)

    venda['validacaoFinanceiro'][1] = obter_data(1) 
    venda['validacaoFinanceiro'][7] = obter_data(2)
    sleep(1)
    if valida_grid('', venda['validacaoFinanceiro'], -1): 
        messagebox.showerror('Erro - DAV', 'Esperado: ' + str(venda['validacaoFinanceiro']))
        return True

    press('insert') # Salvar
    sleep(1)

    press('esc') # Sai Financeiro

def dav_avista(venda):
    # Na tela Baixa CR NOVA FUNCAO TODO
    click(867, 301) # Conta Mov
    write('1')
    sleep(0.5)
    click(499, 840) # Salvar
    sleep(2)
    press('esc') # Sai do CR

def dav(venda):
    maximizar_janela(1)
    sleep(0.5)
    
    entra_na_tela('sv001')
    sleep(0.2)

    press('insert') # Sai do filtro
    sleep(0.7)

    press('f2') # Novo
    sleep(1)

    press(['enter', 'enter', 'enter'])
    sleep(0.3)

    write(venda['cfop'])
    press('enter')
    write(venda['cliente'])
    press('enter')
    sleep(0.5)
    doubleClick(1028, 262) # Mensagem que aparece
    press('enter')
    write(venda['funcionario'])
    press('enter')
    write(venda['pagamento'])

    for _ in range(5): press('enter')
    sleep(0.5)

    for prod in venda['produtos']:
        write(prod['quantidade'])
        press('enter')
        write(prod['cod'])
        press(['enter', 'enter', 'enter'])
        write(prod['desconto'])
        press(['enter', 'enter'])

    sleep(0.5)
    # Valida o grid da venda
    if valida_grid('', venda['validacaoVenda'], -1): return True
    sleep(0.5)
    click(495, 851) # Estoque
    sleep(1)
    press('enter') # Financeiro
    sleep(3)

    dav_crediario(venda) if venda['pagamento'] == '2' else dav_avista(venda)
    sleep(1)

    hotkey('ctrl', 'f6')
    sleep(0.2)
    press('esc')
    sleep(0.5)
    rastro = paste()
    if rastro != 'SV001 - SV002': return True # Erro ao gerar as parcelas e sair ( Tela de Incluir DAV)
    
    if venda['pagamento'] == '2':
        for _ in range(4): press('tab')
        sleep(0.5)
        press('enter') # Gerar NFC-e
        sleep(6)

        # Cima nota
        modulo = {
            'pasta': 'notas',
            'imagem': 'dav1',
            'inicio': '810x58',
            'fim': '1086x340'
        }

        sleep(0.5)
        if imagens_diferentes(modulo): return True

        sleep(1)
        if notas(venda['nota']): return True
        sleep(0.5)
        maximizar_janela(1)

    sleep(0.5)
    press('esc')
    sleep(0.2)
    press('esc')
    
    if venda['pagamento'] == '2': sleep(2) 
    sleep(1)

    # chk = verifica_estoque_alterado(venda) # DESCOMENTE CASO A VENDA POSSUA MAIS DE UM PRODUTO
    entra_na_tela('sp001') # Tela Produtos
    sleep(0.1)
    keyboard.write(venda['produtos'][0]['produto']) # CASO TENHA MAIS DE UM PRODUTO NA VENDA EXCLUA AQUI
    sleep(0.2)
    press('insert') # Sai do filtro
    sleep(0.5)

    if valida_grid('', venda['produtos'][0]['validacao'], 18): return True # CASO TENHA MAIS DE UM PRODUTO NA VENDA EXCLUA AQUI
    press('esc')
    sleep(0.5)
    #return chk # CASO TENHA MAIS DE UM PRODUTO NA VENDA EXCLUA AQUI

def dav_rapido(venda):
    sleep(1)
    press('f2') # Novo
    sleep(6)

    if venda['abertura'] == 1:
        write('10') # Valor Abertura do Caixa
        press('insert')
        sleep(1)
        press('s')
        sleep(0.3)

    for prod in venda['produtos']:
        press('f5') # Campo quantidade
        write(prod['quantidade'])
        press('enter')
        write(prod['barras'])
        press('enter')

        if prod['barras'] == '100':# Produto Grade
            write(prod['variacao1']) # A1B1
            press('enter')
            write(prod['variacao2']) # A1B1
            press('insert')
            sleep(0.7)
    sleep(2)

    modulo = {
        'pasta': 'davrapido',
        'imagem': venda['tela1'],
        'inicio': '1433x175',
        'fim': '1913x917'
    }

    sleep(0.6)
    if imagens_diferentes(modulo): return True # Erro na primeira pagina do DAV Rapido

    press('f9') # Finalizar venda

    write(venda['funcionario'])
    press(['enter'])

    write(venda['pagamento'])
    press(['enter'])

    write(venda['cliente'])
    press(['enter'])
    sleep(0.6)
    clicaCentro()
    
    modulo = {
        'pasta': 'davrapido',
        'imagem': venda['tela2'],
        'inicio': '655x274',
        'fim': '1258x745'
    }
    
    sleep(0.8)
    if imagens_diferentes(modulo, (0, 419, 361, 467)): return True # Erro na primeira pagina do DAV Rapido

    if venda['pagamento'] == '2': # A prazo
        hotkey('ctrl', 'f9') # Gerar NFC-e
        sleep(5)

        write(venda['pagamento'])
        press('enter')

        
        press(['enter', 'enter', 'enter']) # Gera parcelas
        sleep(2)

        modulo = {
            'pasta': 'davrapido',
            'imagem': venda['tela3'],
            'inicio': '876x483',
            'fim': '1313x516'
        }

        sleep(1)
        #if imagens_diferentes(modulo): return True # Erro na primeira pagina do DAV Rapido VERIFICAO DAS IMAGENS DESATIVADA
        sleep(0.5)

        press('enter') # Salvar
        sleep(4)
        
        if comprovante_aprazo(venda['comprovante']): return True
        sleep(0.5)
        press('esc') # Nota
        sleep(6)
        modulo = {
                'pasta': 'notas',
                'imagem': venda['dav'],
                'inicio': '810x58',
                'fim': '1086x330'
        }

        if imagens_diferentes(modulo): return True
        sleep(1)

        if notas(venda['nota']): return True
        sleep(0.5)

        minimizar_janela('Neo NFC-e')
        sleep(0.6)
    else:
        click(812, 782) # Salvar DAV Rapido
        sleep(0.3)
        press('esc')

    click(905, 15)
    sleep(0.5)
    press('esc')
    sleep(0.5)
    press('esc')

    sleep(0.6)
    entra_na_tela('sp001') # Tela Produtos
    sleep(0.1)
    keyboard.write(venda['produtos'][0]['produto']) # CASO TENHA MAIS DE UM PRODUTO NA VENDA EXCLUA AQUI
    sleep(0.2)
    press('insert') # Sai do filtro
    sleep(0.5)

    """ CASO TENHA MAIS DE UM PRODUTO NA VENDA, DESCOMENTE AQUI
    for prod in venda['produtos']:
        hotkey('shift', 'backspace')
        if valida_grid(prod['produto'], prod['validacao'], 18): return True
    """

    if valida_grid('', venda['produtos'][0]['validacao'], 18): return True # CASO TENHA MAIS DE UM PRODUTO NA VENDA EXCLUA AQUI

    press('esc') # Sai da tela
    sleep(0.2)

    return False

def importar_para_nfce(venda, tipo=0):
    # TIPO = 0 => DAV | 1 => DAV RAPIDO
    sleep(1)
    maximizar_janela(0)

    sleep(2)

    hotkey('ctrl', 'r') if tipo else hotkey('ctrl', 'd')
    sleep(1.8)

    click(1055, 550)if tipo else click(1179, 642) # Filtra TODOS
    sleep(0.3)
    press('insert') # Sai do filtro
    sleep(0.5)

    press('f5') # Seleciona o DAV
    sleep(6)
    # Cima nota
    modulo = {
        'pasta': 'notas',
        'imagem': 'dav2',
        'inicio': '810x58',
        'fim': '1086x370'
    }

    if tipo: # DAV RAPIDO
        modulo['imagem'] = 'davrapido2'

    if imagens_diferentes(modulo): return True
    sleep(0.4)
    if notas(venda['nota']): return True

def venda_nfce_1(venda):
    maximizar_janela(0)
    sleep(0.6)
    click(613, 333) # Informe o produto
    sleep(0.2)
    for prod in venda['produtos']:
        press('f5') # Campo quantidade
        write(prod['quantidade'])
        press('enter')
        write(prod['barras'])
        press('enter')

        if prod['barras'] == '100': # Produto com variacao
            write(prod['variacao'])
            press('insert')
 
    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv1_tela1',
        'inicio': '965x242',
        'fim': '1904x756'
    }

    sleep(1)
    if imagens_diferentes(modulo): return True

    press('f9') # Finalizar Venda
    sleep(2)

    write(venda['finalizadora'])
    press('enter')
    
    press('enter') # Vai pro campo salvar

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv1_tela2',
        'inicio': '641x310',
        'fim': '1283x724'
    }

    sleep(0.6)
    if imagens_diferentes(modulo): return True

    press('enter') # Salvar
    click(953, 554)
    sleep(0.3)
    press('enter')
    sleep(7.5)

    modulo = {
        'pasta': 'notas',
        'imagem': 'pdv1',
        'inicio': '810x58',
        'fim': '1086x400'
    }

    if imagens_diferentes(modulo): return True
    
    sleep(3)
    press('esc')
    chk = verifica_estoque_alterado(venda)
    return chk

def venda_nfce_2(venda):
    maximizar_janela(0)
    sleep(0.6)
    click(613, 333) # Informe o produto
    sleep(0.2)
    for prod in venda['produtos']:
        press('f5') # Campo quantidade
        write(prod['quantidade'])
        press('enter')
        write(prod['barras'])
        press('enter')

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv2_tela1',
        'inicio': '965x242',
        'fim': '1904x756'
    }

    sleep(1)
    if imagens_diferentes(modulo): return True

    press('f9') # Finalizar Venda
    sleep(2)

    write(venda['finalizadora'])
    press('enter')
    
    write(venda['cliente'])
    press('enter')

    sleep(0.5)
    press('enter') # Vai pro campo salvar

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv2_tela2',
        'inicio': '641x310',
        'fim': '1283x724'
    }

    sleep(0.6)
    if imagens_diferentes(modulo): return True

    press('enter') # Salvar
    click(953, 554)
    sleep(1)

    hotkey('ctrl', 'f6')
    rastro = paste()

    if rastro != 'PP002 - SV118': return True # Erro ao abrir a tela de autorizar venda
    rastro = ''
    write('1')
    press('insert') # Autoriza
    sleep(1)

    write(venda['finalizadora']) # Forma de pagamento
    press(['enter', 'enter', 'enter']) # Gerar parcelas
    sleep(0.7)

    modulo = {
        'pasta': 'pdv',
        'imagem': 'financeiro_pdv2',
        'inicio': '879x482',
        'fim': '1313x518'
    }

    #if imagens_diferentes(modulo): return True # Erro ao gerar financeiro VALIDAR GERAR PARCELA DESATIVADO
    press('insert') # Salva

    sleep(3)
    if comprovante_aprazo(venda['comprovante']): return True
    sleep(0.7)
    press('esc')

    modulo = {
        'pasta': 'notas',
        'imagem': 'pdv2',
        'inicio': '810x58',
        'fim': '1086x350'
    }

    sleep(7.5)    
    if imagens_diferentes(modulo): return True

    if notas(venda['nota']): return True
    
    sleep(3)
    chk = verifica_estoque_alterado(venda)
    return chk

def venda_nfce_3(venda):
    maximizar_janela(0)
    sleep(0.6)

    hotkey('ctrl', 'shift', 'c')
    sleep(0.3)

    rastro = ''
    hotkey('ctrl', 'f6')
    rastro = paste()

    if rastro != 'PP027': return True # Tela contigencia
    
    press('enter')
    write('1')
    press('enter')
    write('1') # Quantidade Solicitada
    press('enter')
    write('Motivo de Teste')
    press('enter')
    press('enter') # Ativar
    sleep(0.5)

    click(613, 333) # Informe o produto
    sleep(0.2)
    for prod in venda['produtos']:
        press('f5') # Campo quantidade
        write(prod['quantidade'])
        press('enter')
        write(prod['barras'])
        press('enter')

        if prod['travaSistema']:
            modulo = {
                'pasta': 'terminal',
                'imagem': 'estoqueInsuficiente',
                'inicio': '566x418',
                'fim': '1350x625'
            }

            sleep(3)
            if imagens_diferentes(modulo): return True # Permitiu vender com estoque insuficiente
            press('esc') # Sai da tela
            sleep(0.5)
            press('backspace')
            press('f5') # Campo quantidade
            write(prod['quantidadeCorreta'])
            press('enter')
            write(prod['barras'])
            press('enter')

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv3_tela1',
        'inicio': '965x242',
        'fim': '1904x756'
    }

    sleep(1)
    if imagens_diferentes(modulo): return True

    press('f9') # Finalizar Venda
    sleep(2)

    sleep(0.8)
    write(venda['finalizadora'])
    press('enter')

    press('f11') # Tela de desconto
    sleep(0.5)
    write(venda['desconto'])
    sleep(0.7)
    press('tab')
    
    modulo = {
        'pasta': 'terminal',
        'imagem': 'telaDesconto',
        'inicio': '748x259',
        'fim': '1172x715'
    }

    sleep(0.6)
    if imagens_diferentes(modulo): return True # Erro na tela Desconto
    press('insert')
    sleep(1)

    press('enter')

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv3_tela2',
        'inicio': '641x310',
        'fim': '1283x724'
    }

    sleep(0.8)
    if imagens_diferentes(modulo): return True #
    press('enter')
    click(953, 554)
    sleep(1)

    hotkey('ctrl', 'f6')
    rastro = paste()

    if rastro != 'PP002 - SV118': return True # Erro ao abrir a tela de autorizar venda
    rastro = ''

    write('1')
    press('enter')
    write('1')
    press('insert') # Autoriza

    modulo = {
        'pasta': 'terminal',
        'imagem': 'semPermissao',
        'inicio': '786x584',
        'fim': '1100x628'
    }

    sleep(0.6)
    if imagens_diferentes(modulo): return True # Erro na mensagem de funcionario sem permissão
    rastro = ''
    sleep(0.8)
    hotkey('ctrl', 'f6')
    rastro = paste()

    if rastro != 'PP002 - SV118': return True # Tela de autorizar venda fechou
    sleep(0.7)
    press('esc')
    sleep(0.8)

    press('f11')
    sleep(0.7)

    write(venda['descontoCorreto'])
    press('insert')
    sleep(0.6)

    click(814, 563)
    sleep(0.6)
    press('enter')
    moveTo(957, 217)

    modulo = {
        'pasta': 'pdv',
        'imagem': 'pdv3_tela3',
        'inicio': '641x310',
        'fim': '1283x724'
    }

    sleep(0.8)
    if imagens_diferentes(modulo): return True # Erro na tela Desconto
    press('enter')
    click(953, 554)

    modulo = {
        'pasta': 'notas',
        'imagem': 'pdv3',
        'inicio': '810x58',
        'fim': '1086x400'
    }

    sleep(6.5)    
    if imagens_diferentes(modulo): return True
    
    sleep(3)
    press('esc')

    chk = verifica_estoque_alterado(venda)
    return chk
