from pyautogui import click, press, hotkey, write, doubleClick, rightClick, size, moveTo
import keyboard
from pygetwindow import getWindowsWithTitle
from validacao import *
from time import sleep
from random import randint
from pyperclip import copy, paste, waitForPaste
from tkinter import messagebox
from subprocess import run
from datetime import datetime
from dateutil.relativedelta import relativedelta
from threading import Thread
from os.path import join, exists
from os import remove
import dados

def obter_data(qtdMes_a_mais=0):
    data_atual = datetime.now()
    nova_data = data_atual + relativedelta(months=+qtdMes_a_mais)
    nova_data_formatada = nova_data.strftime("%d/%m/%Y")
    return nova_data_formatada

def clicaCentro():
    click(960, 528)

def abre_exe_pdv(arg=''):
    title = r"C:\Realtec\Neo\Exe\NeoPDV.exe"
    def executar_processo():
        try:
            run(title)
        except Exception as e:
            messagebox.showerror('NEOPDV/NFC-e não encontrado!', f'Erro ao executar {title}: {e}')

    thread = Thread(target=executar_processo)

    thread.start()

def maximizar_janela(title=1):
    try:
        title = 'Neo - #empresa1' if title else 'Neo NFC-e'

        window = getWindowsWithTitle(title)[0]
        sleep(0.5)
        window.activate()
        window.maximize()
        sleep(0.5)
    except IndexError:
        messagebox.showerror('Janela não encontrada!', 'Certifique-se de estar com o NEO e o NEOPDV/NFC-e abertos.')
        
def minimizar_janela(opt, title=''):
    if opt == 0:
        opt = 'Neo NFC-e'
    elif opt == 1:
        opt = 'Neo - #empresa1'
    else: opt == title

    try:
        window = getWindowsWithTitle(opt)[0]
        sleep(0.5)
        window.activate()
        window.minimize()
        sleep(0.5)
    except IndexError:
        messagebox.showerror('Janela não encontrada!', 'Certifique-se de estar com o NEO e o NEOPDV/NFC-e abertos.')

def copia_e_cola(texto):
    copy(texto)
    sleep(1)
    hotkey('ctrl', 'c')
    sleep(0.5)
    return not paste() == ''

def numero_aletorio():
    numeros_aleatorios = [randint(0, 7) for _ in range(9)]
    sequencia = ''.join(map(str, numeros_aleatorios))
    return  sequencia

def entra_na_tela(tela):

    sleep(0.5)
    hotkey('ctrl', 'f')  # Busca
    keyboard.write(tela)
    press('enter')
    sleep(1)

def excluir_arquivo_acbr():
    # Concatenando o caminho do diretório com o nome do arquivo
    caminho_arquivo = join(r'C:\Realtec\Neo\Exe', 'ACBrNFeServicos.ini')

    # Verificando se o arquivo existe
    if exists(caminho_arquivo):
        try:
            # Excluindo o arquivo
            remove(caminho_arquivo)
            print(f'O arquivo {caminho_arquivo} foi excluído com sucesso.')
        except Exception as e:
            print(f'Ocorreu um erro ao excluir o arquivo: {e}')
    else:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')

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