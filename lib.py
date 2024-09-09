from pyautogui import click, press, hotkey, write, doubleClick, rightClick, size, moveTo, size
import keyboard
from pygetwindow import getWindowsWithTitle
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

def calcular_xy(coordenada):
    screen_width, screen_height = size()
    x,y = map(int, coordenada.split("x"))
    x = (screen_width / 2) + (x - 960)
    y = (screen_height / 2) + (y - 540)
    return x, y

def clicaCentro():
    screen_width, screen_height = size()
    center_x = screen_width / 2
    center_y = screen_height / 2
    click(center_x, center_y)

def clicaEsquerdo(x, y):
    x, y = calcular_xy('x'.join([str(x),str(y)]))
    click(x, y)

def clicaDireito(x, y):
    x, y = calcular_xy('x'.join([str(x),str(y)]))
    sleep(0.7)
    rightClick(x, y)

def clicaEsquerdoDuplo(x, y):
    x, y = calcular_xy('x'.join([str(x),str(y)]))
    doubleClick(x, y)

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
    numeros_aleatorios = [randint(1, 7) for _ in range(9)]
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