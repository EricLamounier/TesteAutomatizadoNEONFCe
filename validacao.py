from captura import *
from time import sleep
from pyautogui import click, press, hotkey, write, doubleClick, rightClick, size
from pyperclip import copy, paste
import keyboard
from datetime import datetime
import xml.etree.ElementTree as ET
from os import mkdir, path
from tkinter import messagebox
from shutil import copy as copyImage
import dados
from lib import *

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
        hotkey('ctrl', 'c')
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
        adicionar_log(f'ERRO - Esperado : {str(validacao)}\n')
        return True
    
    print(f'validacao = {(validacao)}')
    print(f'capturado = {(aux)}\n')
    adicionar_log(f'Validacao = {(validacao)}')
    adicionar_log(f'Capturado = {(aux)}\n')

    chk = aux == validacao
    
    return not chk
        
def substitui_imagem(modulo): #TODO MUDAR DE PREVIAS PARA O NOME DA MAQUINA | TESTAR
    newImage = f'{modulo['imagem']}.png'
    try:
        mkdir(f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}') if not path.exists(f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}') else True
        print(f'./{modulo['pasta']}/{newImage}')
        copyImage(f'./captura.png', f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}/{modulo['imagem']}.png')

    except Exception as err:
        print(f'Erro ao copiar a nova imagem: {err}')
        messagebox.showerror('Erro ao copiar a nova imagem', err)

def captura_imagem_naoexistente(inicio, fim):
    top, left = calcular_xy(inicio)
    bottom, right = calcular_xy(fim)

    width = right - left
    height = bottom - top
    captura = screenshot(region=(top, left, height, width))
    
    # Verifica se a captura foi bem-sucedida
    if captura is None:
        print("Erro ao capturar a imagem.")
        return False
    
    captura.save('captura.png')
    cap = cv2.imread('./captura.png')

def imagens_diferentes(modulo, coordenada_a_ignorar=(0, 0, 0, 0)): #TODO MUDAR DE PREVIAS PARA O NOME DA MAQUINA | TESTAR

    # Se nao existir a pasta, cria a pasta e salva a imagem
    if not path.exists(f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}'):
        mkdir(f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}')
    
    if not path.exists(f'./Imagens/{dados.banco['nome_maquina']}/{modulo['pasta']}/{modulo['imagem']}.png'):
        captura_imagem_naoexistente(modulo['inicio'], modulo['fim'])
        substitui_imagem(modulo)
        return False
    
    check = captura_imagem(modulo['inicio'], modulo['fim'], modulo['pasta'], modulo['imagem'], coordenada_a_ignorar)

    # Se existir a pasta mas nao a imagem salva a imagem
    if modulo['pasta'] == 'campos': # TODO REMOVER QUANDO MUDAR AS VALIDACOES PARA TEXTO
        return not check  # Iguais
    else:
        if check:  # Iguais
            return False
    
    # São diferentes
    adicionar_log(f'ERRO - Imagem {modulo['pasta']}\\{modulo['imagem']} não confere!')
    res = messagebox.askyesno('As imagens não conferem', 'Deseja salvar a nova imagem e continuar a execução do teste?')
    
    sleep(0.5)
    
    if res:
        substitui_imagem(modulo)
        clicaCentro() # clica no centro da tela
        return False
    
    return True

def adicionar_log(texto):
    data_hora_atual = datetime.now().strftime("%d/%m/%Y - %H:%M")

    log_formatado = f"[{data_hora_atual}] \n{texto}\n\n"
    
    mkdir('Logs/') if not path.exists('Logs/') else True
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

def verifica_estoque_alterado(venda):
    maximizar_janela(1)
    sleep(4)
    entra_na_tela('sp001') # Tela Produtos
    sleep(0.3)
    press('insert') # Sai do filtro
    sleep(0.5)

    for prod in venda['produtos']:
        hotkey('shift', 'backspace')
        if valida_grid(prod['produto'], prod['validacao'], 18): 
            messagebox.showerror('Erro - Estoque Porduto - ' + prod['produto'], 'Esperado: ' + str(prod['validacao']))
            return True

    press('esc')

    return False