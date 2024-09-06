from os.path import join, dirname, exists
from shutil import copytree
from os import mkdir, walk, remove
from tkinter import Tk, Text, Listbox, messagebox, DISABLED, NORMAL, END, SINGLE
from pyautogui import click, size, hotkey
from threading import Thread
from keyboard import add_hotkey
from tkinter import ttk
from math import floor
import socket
import dados

from funcoes_gerais_neo import *
from cadastro_produtos import *
from cadastro_pessoas import *
from main import smokeNFCE, etapas
from config import *

WINDOW_TITLE = "Teste Automatizado NEONFC-e (BETA)"
ICON_PATH = join(dirname(__file__), 'assets', 'logo.ico')

def inicia_opcao(opcoes_menu, opt, ip_maquina):
    
    dados.forcaCancelaExecucao['status'] = False
    
    selected_texto = opcoes_menu.get()
    selected_valor = opt.get(selected_texto)

    dados.banco['ip_maquina'] = ip_maquina.get()  # Pega o ip da maquina

    if dados.banco['ip_maquina'] == '10.1.10.-' or dados.banco['ip_maquina'] == '': dados.banco['ip_maquina'] = '127.0.0.1'

    # Verifica se existe a pasta do usuario em questão
    if not exists(r"./Imagens/"):
        mkdir(r"./Imagens/")
        
    dirImagens = r"./Imagens/" + dados.banco['nome_maquina']
    if not exists(dirImagens):
        mkdir(r"./Imagens/" + dados.banco['nome_maquina'])
        if exists(r"./Imagens/Previas"):
            copytree(r"./Imagens/Previas", dirImagens)

    largura, altura = size()
    coordenadas_centro = (largura // 2, altura // 2)

    limpa()

    click(coordenadas_centro[0], coordenadas_centro[1])

    Thread(target=lambda: smokeNFCE(selected_valor, insere_mensagem, step)).start()

def limpa():
    global current_line
    barra_lateral.config(state=NORMAL)
    barra_lateral.delete('1.0', END)
    barra_lateral.config(state=DISABLED)
    current_line = 1

def apagaImagens():
    root_dir = f'./Imagens/{dados.banco['nome_maquina']}'
    # Percorre todas as subpastas e arquivos a partir do diretório raiz
    res = messagebox.askyesno('Apagar Imagens', f'Tem certeza que deseja apagar todas as prévias de:\n{root_dir} ?')
    if not res: return

    print(f"Apagando imagens de {root_dir}")
    for subdir, _, files in walk(root_dir):
        for file in files:
            # Verifica se o arquivo tem extensão .png
            if file.lower().endswith('.png'):
                file_path = path.join(subdir, file)
                try:
                    remove(file_path)
                except Exception as e:
                    print(f'Erro ao apagar {file_path}: {e}')
    print("- Finalizado.\n")
    messagebox.showinfo("Sucesso", "Imagens apagadas com sucesso!")

def obter_endereco_ip():
    try:
        # Obtém o nome do host
        host_name = socket.gethostname()
        # Obtém o endereço IP associado ao nome do host
        endereco_ip = socket.gethostbyname(host_name)
        return endereco_ip
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")
        return None

def obter_nome_maquina():
    nome_maquina = socket.gethostname()
    dados.banco['nome_maquina'] = nome_maquina
    return nome_maquina

def insere_regras(msg):
    message.config(state=NORMAL)

    for msg in mensagem_inicial:
        message.insert(END, f'{msg}\n')

    message.config(state=DISABLED)

def insere_mensagem(msg, check=1):
    global current_line
    barra_lateral.config(state=NORMAL)
    barra_lateral.see(END)
    
    if msg[0] == '➤':
        # Insira a mensagem e colora de #EFB237 (amarelo)
        barra_lateral.insert(END, f'{msg}')
        barra_lateral.config(state=DISABLED)
        change_color(msg)
        tela.update()
        return
    
    # Limpa a linha anterior
    start_index = barra_lateral.index(f"{current_line}.0")
    end_index = barra_lateral.index(f"{current_line}.end")
    barra_lateral.delete(start_index, end_index)

    # Insere a mensagem e colora de verde se for ✔, de vermelho se for ✘
    barra_lateral.insert(END, f'{msg}\n')
    barra_lateral.config(state=DISABLED)
    change_color(msg)
    tela.update()
    current_line+=1

def change_color(msg):
    global current_line
    chk = msg[0]

    # Obtém o índice de início da linha atual
    start_index = barra_lateral.index(f"{current_line}.0")

    # Obtém o índice de fim da linha atual (calcula o início da próxima linha)
    end_index = barra_lateral.index(f"{current_line}.end")

    # Configura uma tag única para a linha atual com uma cor específica
    tag_name = f"line_{current_line}_tag"
    barra_lateral.tag_configure(tag_name, foreground="green" if chk == '✔' else "red" if chk == '✘' else "#c98e16")

    # Aplica a tag à linha atual
    barra_lateral.tag_add(tag_name, start_index, end_index)

def forcarFechar():
    teste = run(['taskkill', '/IM', 'python.exe', '/F'], capture_output=True, text=True)
    messagebox.showinfo('Processo não encontrado!', teste.stderr)
    
def atalhoPararExecucao():
    add_hotkey('alt', pararExecucao)
    add_hotkey('delete', forcarFechar)

def pararExecucao():
    hotkey('ctrl', 'shift', 'esc')
    dados.forcaCancelaExecucao['status'] = True
    messagebox.showinfo("Parando Teste", "Aguarde a finalização dessa etapa ou bloqueie seu computador para parar imediatamente...")
    
def forcarFechar():
    teste = run(['taskkill', '/IM', 'python.exe', '/F'], capture_output=True, text=True)
    messagebox.showinfo('Processo não encontrado!', teste.stderr)
    
def inativar_produtos():
    messagebox.showinfo("Teste", "Teste Teste Teste Teste Teste Teste Teste...")

def step(val):
    num = len(etapas) # %
    porcent = round((val*100)/num, 2)
    progressbar['value'] = porcent
    porcentagem['text'] = str(porcent) + '%'

if __name__ == "__main__":
    tela = Tk()
    tela.title(WINDOW_TITLE)
    tela.iconbitmap(ICON_PATH)
    tela.resizable(width=False, height=False)
    current_line = 1 # Linha inicial da barra lateral
    
    # Seta o atalho para parar o teste
    atalhoPararExecucao()

    # Box centralizado para "Banco"
    box_credenciais = ttk.LabelFrame(tela, text="Credenciais", padding=10)
    box_credenciais.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    labelIP_Maquina = ttk.Label(box_credenciais, text='IP Da Máquina')
    labelIP_Maquina.grid(column=0, row=0,sticky="nsew")

    ipMaquina = ttk.Entry(box_credenciais, text="ip_maquina", width=20)
    ipMaquina.grid(column=0, row=1)
    ipMaquina.insert(0, obter_endereco_ip())

    nome_Maquina = ttk.Label(box_credenciais, text='Máquina')
    nome_Maquina.grid(column=1, row=0,sticky="nsew", padx=10)

    nomeMaquina = ttk.Entry(box_credenciais, text="nome_maquina", width=20)
    nomeMaquina.grid(column=1, row=1, padx=10)
    nomeMaquina.insert(0, obter_nome_maquina())
    nomeMaquina['state']=DISABLED

    # Barra Lateral
    barra_lateral = Text(tela, state=DISABLED, width=36, height=10)
    barra_lateral.grid(row=0, column=2, rowspan=5, sticky="nsew", padx=(0,10), pady=10)

    lateralBox = ttk.Frame(tela)
    lateralBox.grid(column=2, pady=(5,0))

    #limpar = ttk.Button(lateralBox, text="Limpar", command=limpa)
    #limpar.grid(column=0, row=0)

    apagarImagens = ttk.Button(lateralBox, text="Apagar Imagens", command=apagaImagens)
    apagarImagens.grid(column=0, row=0)

    inativarBttn = ttk.Button(lateralBox, text="Forçar Fechar (DEL)", command=forcarFechar)
    inativarBttn.grid(column=1, row=0)

    parar = ttk.Button(lateralBox, text="Parar (ALT)", command=pararExecucao)
    parar.grid(column=2, row=0)

    box_neo = ttk.LabelFrame(tela, text="Início", padding=10)
    box_neo.grid(column=0, row=1, padx=10, pady=10, rowspan=2, sticky="nsew")

    # Box "NEO"
    labelIniciarNEO = ttk.Label(box_neo, text='Iniciar')
    labelIniciarNEO.grid(column=0, row=0)

    menuOpcoes = ttk.Combobox(box_neo, values=list(opcoesNEO.keys()), width=60)
    menuOpcoes.grid(column=1, row=0, padx=10, pady=10)
    menuOpcoes.state(['readonly'])
    menuOpcoes.set(list(opcoesNEO.keys())[0])

    boxBotoes = ttk.Frame(box_neo)
    boxBotoes.grid(column=0, row=1, columnspan=2, pady=10)

    IniciarBotao = ttk.Button(boxBotoes, text='Iniciar', command=lambda: inicia_opcao(menuOpcoes, opcoesNEO, ipMaquina))
    IniciarBotao.grid(column=0, row=0, padx=5)
    
    labelInfo = ttk.Label(tela, text="ATENÇÃO - Configurações a serem seguidas:")
    labelInfo.grid(column=0, row=3, sticky='w', padx=(10,0), pady=0)

    message = Listbox(tela, selectbackground="grey", selectmode=SINGLE, height=10, width=50)
    message.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    message.configure(font=("Segoe UI", 9))
    
    progressbar = ttk.Progressbar(tela, orient="horizontal", mode='determinate')
    progressbar.grid(column=0, row=5, columnspan=1, sticky="ew", padx=5, pady=10)
    
    porcentagem = ttk.Label(tela, text='0%', background=tela.cget("bg"))
    porcentagem.grid(column=0, row=5, columnspan=1)

    versao_label = ttk.Label(tela, text='Realtec © 2024', foreground='grey')
    versao_label.grid(column=0, row=7, columnspan=4)

    insere_regras(mensagem_inicial)

    tela.mainloop()