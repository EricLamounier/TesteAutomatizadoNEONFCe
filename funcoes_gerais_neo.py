from lib import *
import ctypes
import xml.etree.ElementTree as ET

def parametros_gerais(arg=''):
    excluir_arquivo_acbr()
    sleep(5)
    doubleClick(615, 272) # Principal
    sleep(0.5)

    click(1068, 583) # Campo PFV/NFC-e
    sleep(0.5)
    write('nao') # PFV/NFC-e
    sleep(0.2)
    press('enter')
    sleep(1)

    modulo = {
        'pasta': 'parametrosgerais',
        'imagem': 'campopdvnfce',
        'inicio': '1012x571',
        'fim': '1139x590'
    }

    if imagens_diferentes(modulo): return True

    doubleClick(615, 272)
    sleep(0.3)
    write('vend') # Vendas
    sleep(0.5)

    for _ in range(5): # Navegue até o campo Envia DAV Cupom
        press('enter')
    sleep(0.3)

    write('sim') # Envia DAV Cupom
    sleep(0.3)
    press('enter')
    sleep(1)

    modulo = {
        'pasta': 'parametrosgerais',
        'imagem': 'campoenviadavcupom',
        'inicio': '1170x266',
        'fim': '1325x311'
    }

    if imagens_diferentes(modulo): return True

    for _ in range(6): # Navegue até a barra leteral
        hotkey('shift', 'tab')
    sleep(0.3)

    write('fina') # Financeiro
    sleep(0.5)
    
    for _ in range(6): # Navegue até o campo Caixa Automático
        press('enter')
    sleep(0.3)
 
    write('sim') # Caixa Automático
    sleep(0.3)
    press('enter')
    sleep(1)

    modulo = {
        'pasta': 'parametrosgerais',
        'imagem': 'campocaixaautomatico',
        'inicio': '740x316',
        'fim': '849x349'
    }

    if imagens_diferentes(modulo): return True

    for _ in range(7): # Navegue até a barra lateral
        hotkey('shift', 'tab')
    sleep(0.3)

    write('nf') # PDV/NFC-e
    sleep(0.5)

    press('enter')
    write('sim') # Usa terminal
    press('enter')
    write('nfc') # Tipo Terminal
    press('enter')
    write('manual') # Tipo de Sincronização
    press('enter')
    press('enter')

    # Impressão de turno
    press('space')
    press('enter')
    press('space')
    press('enter')
    press('space')
    press('enter')
    
    for _ in range(5): # Navegue até o campo Ambiente NFC-e
        press('enter')
    sleep(0.3)

    write('homo') # Ambiente NFC-e
    sleep(0.3)
    press('enter')

    write('000001') # ID CSC
    sleep(0.3)
    press('enter')
    sleep(0.3)

    # Inativa o caps lock
    if ctypes.windll.user32.GetKeyState(0x14) & 1 != 0: press('capslock')

    write('1378d2d704218d2d59a3110a3863d188') # CSC
    sleep(0.7)

    for _ in range(2):
        hotkey('shift', 'tab') # Volta
    sleep(1)

    modulo = {
        'pasta': 'parametrosgerais',
        'imagem': 'pdvnfce',
        'inicio': '737x264',
        'fim': '1340x571'
    }

    if imagens_diferentes(modulo): return True

    press('insert') # Salva

    copy('') # Copie e cole para verificar o aparecimento da tela de Usuários do Banco de Dados
    sleep(0.5)
    hotkey('ctrl', 'f6')
    sleep(0.5)
    rastro = paste()

    if rastro != '': # Se a tela de Usuários do Banco de Dados aparecer, volte
        press('esc')
        sleep(0.3)
        press('left')
        sleep(0.3)
        press('enter')

    return False

def parametros_contabilizacao(arg=''):
    sleep(3)

    doubleClick(611, 285) # Principal
    sleep(0.5)

    write('dav r') # DAV Rápido
    press('enter')
    sleep(0.5)

    write('7') # Abertura de Caixa
    press('enter')
    write('9') # Plano de Contas Saída
    press('enter')
    write('7') # Plano de Contas Entrada
    press('enter')
    write('7') # Fecha Caixa
    press('enter')
    sleep(0.6)

    modulo = {
        'pasta': 'parametroscontabilizacao',
        'imagem': 'davrapido',
        'inicio': '737x307',
        'fim': '968x469'
    }

    if imagens_diferentes(modulo): return True

    press('insert') # Salva

    copy('') # Copie e cole para verificar o aparecimento da tela de Usuários do Banco de Dados
    sleep(0.5)
    hotkey('ctrl', 'f6')
    sleep(0.5)
    rastro = paste()

    if rastro != '': # Se a tela de Usuários do Banco de Dados aparecer, volte
        press('esc')
        sleep(0.3)
        press('left')
        sleep(0.3)
        press('enter')

    return False

def cadastro_operadora_cartao(operadora):
    sleep(0.5)

    press('f2') # Novo
    sleep(0.5)

    write('155') # Plano de Contas
    press('enter')

    write('1') # Operadora
    press('enter')

    write('2') # Conta Movimento

    press('insert') # Salvar

    chk = valida_grid(operadora['operadora'], operadora['validacao'], -1)
 
    if chk: messagebox.showerror('Erro - Operadora Cartão', 'Esperado: ' + str(operadora['validacao']))

    press('esc') # Sair

    return chk

def incluir_transacao(transacao):

    keyboard.write(transacao['transacao'])
    sleep(0.1)
    press(['enter', 'enter'])
    sleep(0.1)

    write(transacao['taxa'])
    sleep(0.1)
    press(['enter', 'enter'])
    sleep(0.1)

    write(transacao['tipo'])
    sleep(0.1)
    press('enter')
    sleep(0.1)

    if transacao['qtdParcelas'] != -1:
        write(transacao['qtdParcelas'])
        press('enter')

    press(['enter', 'enter'])
    sleep(1)

def cadastro_transacao(arg=''):
    sleep(0.5)

    press('insert') # Sai do Filtro
    sleep(0.3)

    press('f2') # Novo
    sleep(0.5)

    write('155') # Operadora
    press('enter')

    write('6') # Bandeira
    press('enter')

    press('enter') # Salvar
    sleep(0.5)

def cadastro_finalizadora(finalizadora):
    sleep(0.7)

    press('f2') # Novo
    sleep(0.5)

    keyboard.write(finalizadora['finalizadora'])
    press('enter')

    write(finalizadora['tipo'])
    press('enter')

    write(finalizadora['utilizacao'])
    press('enter')

    if(finalizadora['geraCR'] != -1):
        write(finalizadora['geraCR'])
        press('enter')
    
    if(finalizadora['geraTEF'] != -1):
        write(finalizadora['geraTEF'])
        press('enter')

    if(finalizadora['informaCliente'] != -1):
        write(finalizadora['informaCliente'])
        press('enter')
        sleep(0.3)

    press('enter')
    write(finalizadora['teclaAtalho'])
    press('enter')

    if(finalizadora['transacao'] != -1):
        write(finalizadora['transacao'])
        press('enter')

    write(finalizadora['desconto'])
    press('enter')

    write(finalizadora['habPromocao'])
    press('enter')
    sleep(0.1)

    write(finalizadora['meioPagamento'])
    press('enter')
    sleep(0.1)

    press('insert')
    sleep(0.5)

    chk = valida_grid(finalizadora['finalizadora'], finalizadora['validacao'], -1)
    sleep(0.5)

    if chk: messagebox.showerror('Erro - Finalizadora', 'Esperado: ' + str(finalizadora['validacao']))

    press('esc')

    return chk

def cadastro_forma_pagamento(formaPagamento):

    sleep(0.3)
    press('f2')
    sleep(0.5)

    keyboard.write(formaPagamento['forma']) # Nome da forma de pagamento
    press('enter')

    keyboard.write(formaPagamento['tipo']) # Seleciona o tipo da forma de pagamento
    press('enter')

    if formaPagamento['qntParcela'] != '-1': # Se parcela for habilitada
        write(formaPagamento['qntParcela'])
        press('enter')

    if formaPagamento['entrada'] != '-1': # Se entrada for habilitado
        write(formaPagamento['entrada'])
        press('enter')
        

    if formaPagamento['diasEntrada'] != '-1': # Se dias entrada for habilitado
        write(formaPagamento['diasEntrada'])
        press('enter')
        
    if formaPagamento['tipoVencimento'] != '-1': # Se tipo vencimento for habilitado
        write(formaPagamento['tipoVencimento'])
        press('enter')

    if formaPagamento['tipoJuros'] != '-1': # Se tipo juros for habilitado
        press('enter')
        

    if formaPagamento['juros'] != '-1': # Se juros for habilitado
        write(formaPagamento['juros'])
        press('enter')
        

    if formaPagamento['utiliza'] != '-1': # Se utiliza for habilitado
        press('enter')
        

    if formaPagamento['ajusteCentavos'] != '-1': # Se ajuste centavos for habilitado
        press('enter')
        

    write(formaPagamento['desconto']) # Adiciona desconto
    press('enter')
    sleep(0.4)

    if formaPagamento['forma'] == 'a prazo':
        press('enter')
        sleep(0.4)

    keyboard.write(formaPagamento['meioPagamento']) # Seleciona o meio de pagamento
    sleep(0.7)
    press('enter')
    sleep(0.1)
    press(['enter', 'enter'])
    sleep(0.2)
    write(formaPagamento['finalizadora'])

    press('insert') # Salva
    sleep(0.6)

    chk = valida_grid(formaPagamento['forma'], formaPagamento['validacao'], -1)
    sleep(0.2)

    if chk: messagebox.showerror('Erro - Forma Pagamento', 'Esperado: ' + str(formaPagamento['validacao']))

    press('esc')
    return chk # Nao há erro

def cria_terminal(arg=''):
    abre_exe_pdv()
    sleep(2)

    click(847, 477) # Login
    sleep(0.05)
    hotkey('ctrl', 'a') # Seleciona tudo
    sleep(0.05)
    press('delete') # Apaga
    sleep(0.05)
    press(['enter', 'enter']) # Entra no NEO PDV

    sleep(4) # TODO VERIFICAR AQUI SE FUNCIONOU!!!!
    press('n') # Para pular pedido de atualizar nova versão caso apareça

    sleep(20) # Espera atualizar
    hotkey('ctrl', 'a') # Seleciona tudo
    sleep(0.5)
    write(dados.banco['ip_maquina'])
    sleep(0.5)
    press('enter') # Salvar
    sleep(4.5)

    modulo = {
        'pasta': 'terminal',
        'imagem': 'terminalconfigurado',
        'inicio': '858x492',
        'fim': '1105x579'
    }

    if imagens_diferentes(modulo): return True # Terminal nao foi configurado
    sleep(0.3)
    press('enter') # Configurado com sucesso OK
    sleep(0.7)

    press('s') # Sincronizar terminais
    sleep(35)

    # Verifica se foi criado
    modulo = {
        'pasta': 'terminal',
        'imagem': 'sincronizado',
        'inicio': '843x485',
        'fim': '1077x582'
    }

    if imagens_diferentes(modulo): return True # Terminal nao foi sincronizado
    sleep(0.7)

    press('enter') # O sistema precisa ser reiniciado "OK"
    click(955, 560) # Preocaução "OK"
    sleep(0.5)

    return False

def configurar_terminal(sincronizacao):
    excluir_arquivo_acbr()
    maximizar_janela(1)
    sleep(0.5)

    entra_na_tela('sp156')
    sleep(0.5)

    press('f3') # Editar o terminal

    for _ in range(5):
        press('enter')

    serie = numero_aletorio()

    write(serie) # Serie NFC-r
    press('enter')
    write(serie) # Numero inicial
    sleep(0.2)
    press('insert')
    sleep(0.2)
    press('esc')
    sleep(0.3)

    entra_na_tela('sm010') # Parametros gerais
    sleep(5)

    doubleClick(615, 272) # Principal
    sleep(0.5)

    write('nf')
    sleep(0.5)

    press(['enter', 'enter']) # Campo Tipo de Sincronização
    sleep(0.3)

    write('aut') # Automatica
    sleep(0.3)

    press('insert') # Salva

    copy('') # Copie e cole para verificar o aparecimento da tela de Usuários do Banco de Dados
    sleep(0.5)
    hotkey('ctrl', 'f6')
    sleep(0.5)
    rastro = paste()

    if rastro != '': # Se a tela de Usuários do Banco de Dados aparecer, volte
        press('esc')
        sleep(0.3)
        press('left')
        sleep(0.3)
        press('enter')
    sleep(1)
    entra_na_tela('sp164') # Sincronizacao
    sleep(1.5)

    click(583, 727) # Sincronizar agora
    sleep(0.5)
    click(583, 727) # Sincronizar agora
    sleep(6)

    click(619, 591)
    sleep(0.2)
    hotkey('ctrl', 'a') # Seleciona tudo
    sleep(0.5)
    hotkey('ctrl', 'c') # Copia

    content = paste()
    content = content.split('\r')

    #chk =  content != sincronizacao['rapida'] # TODO IMPLEMENTAR AQUI AINDA
    chk = False

    press('esc')

    return chk

def entrar_no_terminal(usuario):

    abre_exe_pdv()
    sleep(1.5)

    click(847, 477) # Login
    sleep(0.3)
    hotkey('ctrl', 'a')
    sleep(0.3)
    write(usuario['login'])

    press('tab')
    write(usuario['senha'])

    press(['enter', 'enter']) # Entra no NEO PDV
    sleep(6)

    press('n') # Para pular pedido de atualizar nova versão caso apareça TODO VRRIFICAR SE FUNCIONOU
    sleep(2)

    hotkey('ctrl', 'f6') # Pega rastro da tela
    rastro = waitForPaste()
    if rastro != 'PP004': return True # Erro ao entrar no PDV

    write('10') # Valor incluir caixa
    sleep(0.2)

    press('insert') # Salvar

def valida_transacoes(transacoes):
    chk = valida_grid('', transacoes['validacao'])
    if chk: messagebox.showerror('Erro - Transação', 'Esperado: ' + str(transacoes['validacao']))
    return chk

def conferir_notas():
    press('insert') # Sai do filtro
    sleep(1)

    modulo = {
        'pasta': 'pdv',
        'imagem': 'conferencia_notas',
        'inicio': '356x161',
        'fim': '1163x315'
    }

    return imagens_diferentes(modulo)

def fecha_xml():
    press('esc')
    sleep(0.2)
    press('esc')
    sleep(0.5)
    clicaCentro()
    sleep(0.3)
    hotkey('shift', 'backspace')

def verifica_xml(venda):

    try:
        xml_str = waitForPaste()[2:].replace('-', '') # Remove o espaco no inicio e os tracos
        root = ET.fromstring(xml_str)
        uTrib_esperado = venda['utrib']
        cEAN_esperado = venda['cean']
        uTrib_capturado = []
        cEAN_capturado = []
        aux = False
    except Exception as err:
        messagebox.showerror('XML invalido!', 'Verifique se possui um XML válido na sua área de transferência!')
        return True

    for elem in root.iter():
        if elem.tag.endswith('uTrib'):
            uTrib_capturado.append(elem.text)

        elif elem.tag.endswith('cEAN'):
            cEAN_capturado.append(elem.text)
    
    if uTrib_capturado != uTrib_esperado:
        messagebox.showerror('Erro uTrib', f'Erro na tributação:\n- Esperado: {uTrib_esperado}\n- Capturado: {uTrib_capturado}')
        aux = True

    if cEAN_capturado != cEAN_esperado:
        messagebox.showerror('Erro cEAN', f'Erro no código cEAN:\n- Esperado: {cEAN_esperado}\n- Capturado: {cEAN_capturado}')
        aux = True

    return aux

def validar_nfce_neo(args=''):

    sleep(1)
    press('insert')
    xml = {
        1: {'utrib': ['UN'], 'cean': ['1000000000016']},
        #2: {'utrib': ['UN'], 'cean': ['1000000000016']},
        3: {'utrib': ['UN'], 'cean': ['SEM GTIN']},
        4: {'utrib': ['CX'], 'cean': ['1000000000023']},
        5: {'utrib': ['CX'], 'cean': ['1000000000023']},
        6: {'utrib': ['UN', 'CX', 'UN'], 'cean': ['1000000000016', '1000000000023', 'SEM GTIN']},
        7: {'utrib': ['CX'], 'cean': ['1000000000023']},
        8: {'utrib': ['CX'], 'cean': ['1000000000023']},
    }
    click(1309, 260) # maximiza
    sleep(0.7)
    click(58, 180) # Primeira venda
    sleep(0.7)

    for venda in xml.values():
        click(930, 1002) # Scroll
        sleep(0.5)
        click(851, 926) # Abre XML
        sleep(1)
        clicaCentro()
        hotkey('ctrl', 'a') # Seleciona o conteudo do XML
        hotkey('ctrl', 'c') # Copia o conteudo do XML
        if verifica_xml(venda): return True
        sleep(0.8)
        click(1341, 260) # fechar
        sleep(0.8)
        clicaCentro()
        press('down')
        sleep(0.8)
        copy('')

    clicaCentro()
    press('esc')
    return False

def copiar_tudo(coords):
    rightClick(coords[0], coords[1])
    sleep(0.75)
    press('t')

def situacao_notas(tipo):
    validacao = { 
        'confirmado': ['Confirmado', 'Documento Regular', ''],
        'cancelado': ['Cancelado', 'Documento Cancelado', ''],
        'pendente': ['Pendente de Autorização', 'Documento Regular', 'Portal Inativo ou Inoperante']
    }

    copiar_tudo([503, 988])
    if valida_grid('empty', validacao[tipo], 0,3,3,3,3,3,3,3,3,3):
        messagebox.showerror('Erro NFC-e', 'Esperado: ' + str(validacao[tipo]))
        return True
    return False
    
def produtos_nota(situacao, nota):
    fechado = {
        1: ['1', '#produto1', '1000000000016', '2,59', '3,00', '10', '30,00', '0,00', '0,00', '0,00', '0,00', '30,00', 'Fechado', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        2: ['1', '#produto3', '100', '50,00', '60,00', '10', '600,00', '0,00', '0,00', '0,00', '0,00', '600,00', 'Fechado', '12,00', '600,00', '72,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        3: ['1', '#produto2', '1000000000023', '15,37', '20,00', '15', '300,00', '0,00', '-0,85', '0,00', '0,00', '299,15', 'Fechado', '12,00', '299,15', '35,90', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        4: ['1', '#produto2', '1000000000023', '15,37', '20,00', '2', '40,00', '0,00', '0,00', '0,00', '0,00', '40,00', 'Fechado', '12,00', '40,00', '4,80', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        5: ['1', '#produto1', '1000000000016', '2,59', '3,00', '1', '3,00', '0,00', '0,00', '0,00', '0,00', '3,00', 'Fechado', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '2', '#produto2', '1000000000023', '15,37', '20,00', '1', '20,00', '0,00', '0,00', '0,00', '0,00', '20,00', 'Fechado', '12,00', '20,00', '2,40', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '3', '#produto3', '100', '50,00', '60,00', '1', '60,00', '0,00', '0,00', '0,00', '0,00', '60,00', 'Fechado', '12,00', '60,00', '7,20', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        6: ['1', '#produto2', '1000000000023', '15,37', '20,00', '25', '500,00', '0,00', '0,00', '0,00', '0,00', '500,00', 'Fechado', '12,00', '500,00', '60,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        7: ['1', '#produto2', '1000000000023', '15,37', '20,00', '12', '240,00', '0,00', '-15,00', '0,00', '0,00', '225,00', 'Fechado', '12,00', '225,00', '27,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
    }

    cancelado = {
        1: ['1', '#produto1', '1000000000016', '2,59', '3,00', '10', '30,00', '0,00', '0,00', '0,00', '0,00', '30,00', 'Cancelado', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        2: ['1', '#produto3', '100', '50,00', '60,00', '10', '600,00', '0,00', '0,00', '0,00', '0,00', '600,00', 'Cancelado', '12,00', '600,00', '72,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        3: ['1', '#produto2', '1000000000023', '15,37', '20,00', '15', '300,00', '0,00', '-0,85', '0,00', '0,00', '299,15', 'Cancelado', '12,00', '299,15', '35,90', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        4: ['1', '#produto2', '1000000000023', '15,37', '20,00', '2', '40,00', '0,00', '0,00', '0,00', '0,00', '40,00', 'Cancelado', '12,00', '40,00', '4,80', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        5: ['1', '#produto1', '1000000000016', '2,59', '3,00', '1', '3,00', '0,00', '0,00', '0,00', '0,00', '3,00', 'Cancelado', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '2', '#produto2', '1000000000023', '15,37', '20,00', '1', '20,00', '0,00', '0,00', '0,00', '0,00', '20,00', 'Cancelado', '12,00', '20,00', '2,40', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '3', '#produto3', '100', '50,00', '60,00', '1', '60,00', '0,00', '0,00', '0,00', '0,00', '60,00', 'Cancelado', '12,00', '60,00', '7,20', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        6: ['1', '#produto2', '1000000000023', '15,37', '20,00', '25', '500,00', '0,00', '0,00', '0,00', '0,00', '500,00', 'Cancelado', '12,00', '500,00', '60,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
        7: ['1', '#produto2', '1000000000023', '15,37', '20,00', '12', '240,00', '0,00', '-15,00', '0,00', '0,00', '225,00', 'Cancelado', '12,00', '225,00', '27,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', ''],
    }

    aux = {}
    aux = fechado if situacao else cancelado


    copiar_tudo([1467, 990])
    if valida_grid('empty', aux[nota]):
        messagebox.showerror('Erro NFC-e', 'Esperado: ' + str(aux[nota]))
        return True
    clicaCentro()
    return False
    
def verifica_notas_confirmadas(args=''):

    sleep(0.7)
    press('insert') # Sai do filtro
    sleep(0.5)
    click(58, 183)
    sleep(0.3)

    # Valida antes de cancelar
    # Nota 1
    sleep(0.5)
    if situacao_notas('confirmado') or produtos_nota(1, 1): 
        return True
    
    # Nota 2
    sleep(0.5)
    press('down')
    if situacao_notas('confirmado') or produtos_nota(1, 2): return True
    
    # Nota 3
    sleep(0.5)
    press('down')
    if situacao_notas('confirmado') or produtos_nota(1, 3): return True
    
    # Nota 4
    sleep(0.5)
    press('down')
    if situacao_notas('confirmado') or produtos_nota(1, 4): return True
    
    # Nota 5
    sleep(0.5)
    press('down')
    if situacao_notas('confirmado') or produtos_nota(1, 5): return True
    
    # Nota 6
    sleep(0.5)
    press('down')
    if situacao_notas('confirmado') or produtos_nota(1, 6): return True
    
    # Nota 7
    sleep(0.5)
    press('down')
    if situacao_notas('pendente') or produtos_nota(1, 7): return True

    press('esc')
    return False

def verifica_notas_canceladas(args=''):
    sleep(0.5)
    press('insert') # Sai do filtro
    sleep(0.5)
    click(58, 183)
    sleep(0.3)

    # Valida antes de cancelar
    # Nota 1
    sleep(0.5)
    if situacao_notas('cancelado') or produtos_nota(0, 1): 
        return True
    
    # Nota 2
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 2): return True
    
    # Nota 3
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 3): return True
    
    # Nota 4
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 4): return True
    
    # Nota 5
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 5): return True
    
    # Nota 6
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 6): return True
    
    # Nota 7
    sleep(0.5)
    press('down')
    if situacao_notas('cancelado') or produtos_nota(0, 7): return True

    sleep(1)
    press('esc')
    
    return False

def fechar_caixa(args=''):
    sleep(0.5)
    maximizar_janela(0)
    sleep(0.5)

    press('f12') # Fechar Caixa
    sleep(1)

    press('enter') # Retirada do Caixa
    write('20')
    press('enter') 

    modulo = {
        'pasta': 'terminal',
        'imagem': 'fechamentodecaixa1',
        'inicio': '656x301',
        'fim': '1282x721'
    }
    sleep(1)
    if imagens_diferentes(modulo): return True

    press('enter') # Confirma fechamento
    sleep(0.6)
    press('s')
    sleep(2)

    modulo = {
        'pasta': 'terminal',
        'imagem': 'fechamentodecaixa_relatorio',
        'inicio': '823x302',
        'fim': '1063x1004'
    }

    if imagens_diferentes(modulo, (9, 391, 120, 530)): return True
    sleep(0.8)
    press('esc')
    sleep(0.5)
    maximizar_janela(1)

    return False

def cancelar_nfce(estoqueFinal):

    press('insert') # Sai do filtro
    sleep(0.8)

    click(57, 183)
    sleep(0.5)

    # Primeira Nota
    #press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(3)


    # Segunda Nota
    press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(3)

    # Terceira Nota
    press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(3)

    # Quarta Nota
    press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(3)

    # Quinta Nota ( Financeiro possui baixa)
    press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(1)

    modulo = {
        'pasta': 'terminal',
        'imagem': 'financeiropossuibaixa',
        'inicio': '562x423',
        'fim': '1358x614'
    }
    sleep(3)
    if imagens_diferentes(modulo): return True
    press('esc')
    sleep(0.5)

    hotkey('ctrl', 'shift', 'r') # Aba complementar
    sleep(2)

    click(851, 614) # Cartoes
    sleep(2)

    # Estorna cartao 1
    hotkey('ctrl', 'e')
    press('s') # Confirma
    sleep(1)
    press('down')
    sleep(0.5)

    # Estorna cartao 2
    hotkey('ctrl', 'e')
    press('s') # Confirma
    sleep(1)
    press('esc')
    sleep(2)
    press('esc')
    sleep(1.5)

    press('f4') # Cancelar
    sleep(0.3)

    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(3.5)

    # Sexta Nota
    press('down')
    sleep(0.3)
    press('f4') # Cancelar
    sleep(0.3)
    
    press('s') # Confirma
    sleep(0.3)
    press('f5') # Motivo
    sleep(1)

    # Sétima Nota ( Deve estar confirmada )
    press('down')
    sleep(2.5)
    press('f4') # Cancelar
    sleep(1)
    
    press('s') # Confirma
    sleep(0.8)
    press('f5') # Motivo
    sleep(0.8)

    modulo = {
        'pasta': 'terminal',
        'imagem': 'pendenteautorizacao',
        'inicio': '837x489',
        'fim': '1121x537'
    }
    sleep(2.5)
    if imagens_diferentes(modulo): return True
    press('enter') # Ok

    press('down')

    modulo = {
        'pasta': 'terminal',
        'imagem': 'legendas1',
        'inicio': '11x175',
        'fim': '27x317'
    }
    sleep(1)
    if imagens_diferentes(modulo): 
        messagebox.showerror('Erro - Legendas NFC-e', 'As legendas devem estar na ordem:\n\nCancelado\nCancelado\nCancelado\nCancelado\nCancelado\nCancelado\nConfirmado')
        return True

    ajustar_nfce()
    sleep(0.7)

    click(65, 309)

    press('f4') # Cancelar
    sleep(0.8)

    press('s') # Confirma
    sleep(0.7)
    press('f5') # Motivo
    sleep(3)

    modulo = {
        'pasta': 'terminal',
        'imagem': 'financeiropossuibaixa',
        'inicio': '562x423',
        'fim': '1358x614'
    }
    sleep(2)
    if imagens_diferentes(modulo): return True
    press('esc')
    sleep(0.5)

    hotkey('ctrl', 'shift', 'r') # Aba complementar
    sleep(1.5)

    click(851, 614) # Cartoes
    sleep(1.5)

    # Estorna cartao 1
    hotkey('ctrl', 'e')
    press('s') # Confirma
    press('down')
    sleep(0.8)
    press('esc')
    sleep(1)
    press('esc')
    sleep(0.8)

    press('f4') # Cancelar
    sleep(0.5)

    press('s') # Confirma
    sleep(0.5)
    press('f5') # Motivo
    sleep(1.8)

    # Verifica as legendas
    modulo = {
        'pasta': 'terminal',
        'imagem': 'legendas2',
        'inicio': '11x175',
        'fim': '27x317'
    }
    
    sleep(0.5)
    if imagens_diferentes(modulo): return True

    press('esc')
    sleep(0.8)
    return False

def ajustar_nfce(args=''):
    # Ajustar NFC-e
    click(491, 87) # Ajustar
    sleep(0.5)
    click(29, 311) # Nota aberta
    sleep(0.5)
    click(655, 84) # Executar
    sleep(0.5)

    click(491, 87) # Ajustar
    sleep(4)
    return False
    # TODO VALIDAR AJUSTAR NFCE THIS IS A TEST