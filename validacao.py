from captura import *
from time import sleep
from pyautogui import click, press, hotkey, write, doubleClick, rightClick, size
from pyperclip import copy, paste
import keyboard
from datetime import datetime
import xml.etree.ElementTree as ET
from os.path import exists
from os import mkdir, makedirs

def nao_existe_registro(texto):
    hotkey('shift', 'backspace')  # Limpa o campo
    copy('')  # Limpa área de transferência

    press('f12')  # Busca geral
    keyboard.write(texto)

    sleep(1)

    hotkey('ctrl', 'c')
    check = paste()

    return check == ''  

def valida_grid(registro, validacao, *data):

    sleep(0.3)
    if registro != '':
        press('f12')
        sleep(0.5)
        keyboard.write(registro) # Procura pelo registro
        sleep(0.6)

    if registro != 'empty':
        largura, altura = size()
        coordenadas_centro = (largura // 2, altura // 2)
        coords =  coordenadas_centro
        rightClick(coords[0], coords[1]) # Clica no centro
        sleep(0.75)
        press('t') # Copia tudo
        sleep(0.4)

    content = paste()
    sleep(0.4)

    try:
        content = content.split('\r') # Divide entre labels e valores
        content.pop(0) # Retira os labels

        aux = []
        for _ in content:
            aux += _.split('\t')

        if data != -1:
            for indx in data: aux.pop(indx)

    except IndexError:
        adicionar_log(f'ERRO - Validacao: {(validacao)}')
        adicionar_log(f'ERRO - Esperado : {str(validacao)}')
        #messagebox.showerror("Erro!", "Esperado - '" + str(validacao) + "'")
        return True
    
    print(f'validacao = {(validacao)}')
    print(f'capturado = {(aux)}')
    adicionar_log(f'Validacao = {(validacao)}')
    adicionar_log(f'Capturado = {(aux)}')

    chk = aux == validacao

    #if not chk: # Diferentes
        #messagebox.showerror("Erro!", "Esperado - '" + str(validacao) + "'")
    
    return not chk
        
def imagens_diferentes(modulo, coordenada_a_ignorar=(0, 0, 0, 0)):
    check = captura_imagem(modulo['inicio'], modulo['fim'], modulo['pasta'], modulo['imagem'], coordenada_a_ignorar)

    if modulo['pasta'] == 'campos':
        return not check  # Iguais
    else:
        if check:  # Iguais
            return False
    # São diferentes
    adicionar_log(f'ERRO - Imagem {modulo['pasta']}\\{modulo['imagem']} não confere!')
    return True

def adicionar_log(texto):
    data_hora_atual = datetime.now().strftime("%d/%m/%Y - %H:%M")

    log_formatado = f"[{data_hora_atual}] \n{texto}\n\n"
    
    if not exists('./Logs'):
        makedirs('./Logs')

    if not exists('./Logs/log.txt'):
        open('./Logs/log.txt', 'w').close()
    
    with open('./Logs/log.txt', 'a') as arquivo_log:
        arquivo_log.write(log_formatado)

def valida_visualizacao_xml(tag, valorTag): # <uTrib> {UN e CX } <cEAN> {SEM GTIN e EAN de cada produto}
    # Obter o XML da área de transferência
    xml_string = paste()

    # Verificar se o XML não está vazio
    if xml_string.strip() == "":
        print("Nenhum XML encontrado na área de transferência.")
        return True

    # Analisar o XML
    xml_string = xml_string[2:]
    xml_string = xml_string.replace('-', '')
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Erro ao analisar o XML:", e)
        return True

    # Definir o namespace
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    # Encontrar o valor dentro da tag <uTrib>
    tag = root.find(f'.//nfe:det/nfe:prod/nfe:{tag}', ns)

    if tag is not None: # Encontrou
        if tag.text != valorTag: return True
    return False
