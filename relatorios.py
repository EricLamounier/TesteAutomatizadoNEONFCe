from lib import *
from validacao import *

def busca_no_relatorio(content):
    hotkey('ctrl', 'f')
    keyboard.write(content)
    press('enter')
    print(content)
    sleep(1)

def cola_nota(content):
    copy(content)
    clicaEsquerdoDuplo(1854, 81)
    sleep(0.5)
    clicaEsquerdo(1854, 168)

def comprovante_aprazo(relatorio):
    hotkey('ctrl', 'f')
    sleep(0.5)
    clicaEsquerdo(1824, 227)
    sleep(0.3)

    # TODO MUDAR PARA VERIFICAR A MENSAGEM
    modulo = {
        'pasta': 'campos',
        'imagem': relatorio['validacaoMensagem'], #asdasd
        'inicio': '884x460',
        'fim': '1035x579'
    }

    # CNPJ - Endereco e cidade nao busca
    hotkey('ctrl', 'f')
    busca_no_relatorio(relatorio['cnpj'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro CNPJ', 'Erro ao procurar o CNPJ - ' + relatorio['cnpj'])
        return True

    # Cliente
    hotkey('ctrl', 'f')
    busca_no_relatorio(relatorio['cliente'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro CLIENTE', 'Erro ao procurar o CLIENTE - ' + relatorio['cliente'])
        return True

    # CPF 
    hotkey('ctrl', 'f')
    busca_no_relatorio(relatorio['cpf'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro CPF/CNPJ', 'Erro ao procurar o CPF/CNPJ - ' + relatorio['cpf'])
        return True

    # Endereco
    hotkey('ctrl', 'f')
    busca_no_relatorio(relatorio['endereco'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro ENDERECO', 'Erro ao procurar o ENDERECO - ' + relatorio['endereco'])
        return True

    # Valor total
    hotkey('ctrl', 'f')
    busca_no_relatorio(relatorio['total'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro TOTAL', 'Erro ao procurar o TOTAL - ' + relatorio['total'])
        return True
    clicaEsquerdo(1824, 227)
    sleep(0.25)

    # Pula
    hotkey('ctrl', 'f')
    sleep(0.25)
    write('Descontos')
    sleep(0.25)

    # Valor Líquido
    clicaEsquerdo(1870, 322)
    busca_no_relatorio(relatorio['liquido'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro VALOR LÍQUIDO', 'Erro ao procurar o VALOR LÍQUIDO - ' + relatorio['liquido'])
        return True

    # Parcela 1
    busca_no_relatorio(relatorio['parcela1'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro PARCELA 1', 'Erro ao procurar o PARCELA 1 - ' + relatorio['parcela1'])
        return True

    # Vencimento 1
    relatorio['vencimento1'] = obter_data(1)
    busca_no_relatorio(relatorio['vencimento1'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro VENCIMENTO 1', 'Erro ao procurar o VENCIMENTO 1 - ' + relatorio['vencimento1'])
        return True

    # Parcela 2
    busca_no_relatorio(relatorio['parcela2'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro PARCELA 2', 'Erro ao procurar o PARCELA 2 - ' + relatorio['parcela2'])
        return True

    # Vencimento 2
    relatorio['vencimento2'] = obter_data(2)
    busca_no_relatorio(relatorio['vencimento2'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro VENCIMENTO 1', 'Erro ao procurar o VENCIMENTO 1 - ' + relatorio['vencimento2'])
        return True

    # Valor Líquido
    busca_no_relatorio(relatorio['liquido'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro VALOR LÍQUIDO', 'Erro ao procurar o VALOR LÍQUIDO - ' + relatorio['liquido'])
        return True

    # Data atual
    relatorio['data'] = obter_data()
    busca_no_relatorio(relatorio['data'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro DATA', 'Erro ao procurar o DATA - ' + relatorio['data'])
        return True

    # Operador
    busca_no_relatorio(relatorio['operador'])
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro OPERADOR', 'Erro ao procurar o OPERADOR - ' + relatorio['operador'])
        return True

def notas(nota):
    # TODO MUDAR PARA VERIFICAR A MENSAGEM
    modulo = {
        'pasta': 'campos',
        'imagem': 'textonaoencontradopdv',
        'inicio': '884x460',
        'fim': '1035x579'
    }

    # CPF 
    hotkey('ctrl', 'f')
    write(nota['cpf'])
    sleep(0.5)
    clicaEsquerdo(1868, 218)
    sleep(0.8)
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro CPF', 'Erro ao procurar o CPF - ' + nota['cpf'])
        return True

    # Data
    nota['data'] = obter_data(0)
    hotkey('ctrl', 'f')
    sleep(0.3)
    hotkey('ctrl', 'f')
    write(nota['data'])
    sleep(0.5)
    clicaEsquerdo(1868, 218)
    sleep(0.8)
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro DATA', 'Erro ao procurar a DATA - ' + nota['data'])
        return True

    # Rodape
    hotkey('ctrl', 'f')
    sleep(0.3)
    hotkey('ctrl', 'f')
    write(nota['rodape'])
    sleep(0.5)
    clicaEsquerdo(1868, 218)
    sleep(0.8)
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro ' + nota['rodape'], 'Erro ao procurar - ' + nota['rodape'])
        return True

    # Operador
    hotkey('ctrl', 'f')
    sleep(0.3)
    hotkey('ctrl', 'f')
    keyboard.write(nota['operador'])
    sleep(0.5)
    clicaEsquerdo(1868, 218)
    sleep(0.8)
    if not imagens_diferentes(modulo): 
        messagebox.showerror('Erro OPERADOR', 'Erro ao procurar o OPERADOR - ' + nota['OPERADOR'])
        return True

    press('esc')
    return False