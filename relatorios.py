from lib import *
from validacao import *
from dados import davRapido1
def busca_no_relatorio(doc, mensagem, busca=1):
    if busca: 
        hotkey('ctrl', 'f')
        keyboard.write(doc)
        press('enter')
    else:
        press('f2')
    return not valida_grid_NOVO('', 'clicaEsquerdo', mensagem)


def cola_nota(content):
    copy(content)
    clicaEsquerdoDuplo(1854, 81)
    sleep(0.5)
    clicaEsquerdo(1854, 168)

def comprovante_aprazo(comprovante):
    relatorio = comprovante['relatorio']
    validacao = comprovante['validacaoMensagem']

    hotkey('ctrl', 'f')
    sleep(0.5)
    clicaEsquerdo(1824, 227)
    sleep(0.3)
    
    # CNPJ - Endereco e cidade nao busca
    if busca_no_relatorio(relatorio['cnpj'], validacao): 
        messagebox.showerror('Erro CNPJ', 'Erro ao procurar o CNPJ - ' + relatorio['cnpj'])
        return True

    # Cliente
    if busca_no_relatorio(relatorio['cliente'], validacao): 
        messagebox.showerror('Erro CLIENTE', 'Erro ao procurar o CLIENTE - ' + relatorio['cliente'])
        return True

    # CPF
    if busca_no_relatorio(relatorio['cpf'], validacao): 
        messagebox.showerror('Erro CPF', 'Erro ao procurar o CPF - ' + relatorio['cpf'])
        return True

    # Endereco
    if busca_no_relatorio(relatorio['endereco'], validacao): 
        messagebox.showerror('Erro ENDERECO', 'Erro ao procurar o ENDERECO - ' + relatorio['endereco'])
        return True
    
    # Valor total
    if busca_no_relatorio(relatorio['total'], validacao): 
        messagebox.showerror('Erro total', 'Erro ao procurar o total - ' + relatorio['total'])
        return True
    
    # Valor Líquido
    if busca_no_relatorio(relatorio['liquido'], validacao, busca=0): 
        messagebox.showerror('Erro liquido', 'Erro ao procurar o liquido - ' + relatorio['liquido'])
        return True
    
    # Valor total
    if busca_no_relatorio(relatorio['liquido'], validacao, busca=0): 
        messagebox.showerror('Erro liquido', 'Erro ao procurar o liquido - ' + relatorio['liquido'])
        return True

    # Parcela 1
    if busca_no_relatorio(relatorio['parcela1'], validacao): 
        messagebox.showerror('Erro parcela1', 'Erro ao procurar o parcela1 - ' + relatorio['parcela1'])
        return True
    
    # Parcela 2
    if busca_no_relatorio(relatorio['parcela2'], validacao, busca=0): 
        messagebox.showerror('Erro parcela2', 'Erro ao procurar o parcela2 - ' + relatorio['parcela2'])
        return True
    # Vencimento 1
    relatorio['vencimento1'] = obter_data(1)
    if busca_no_relatorio(relatorio['vencimento1'], validacao): 
        messagebox.showerror('Erro vencimento1', 'Erro ao procurar o vencimento1 - ' + relatorio['vencimento1'])
        return True

    # Vencimento 2
    relatorio['vencimento2'] = obter_data(2)
    if busca_no_relatorio(relatorio['vencimento2'], validacao): 
        messagebox.showerror('Erro vencimento2', 'Erro ao procurar o vencimento2 - ' + relatorio['vencimento2'])
        return True

    # Data atual
    relatorio['data'] = obter_data()
    if busca_no_relatorio(relatorio['data'], validacao): 
        messagebox.showerror('Erro data', 'Erro ao procurar o data - ' + relatorio['data'])
        return True

    # Operador
    if busca_no_relatorio(relatorio['operador'], validacao): 
        messagebox.showerror('Erro operador', 'Erro ao procurar o operador - ' + relatorio['operador'])
        return True

def notas(comprovante):
    nota = comprovante['nota']
    validacao = comprovante['validacaoMensagem']
    sleep(0.3)

    # CPF
    sleep(0.5)
    if busca_no_relatorio(nota['cpf'], validacao): 
        messagebox.showerror('Erro cpf', 'Erro ao procurar o cpf - ' + nota['cpf'])
        return True

    # Data
    nota['data'] = obter_data(0)
    hotkey('ctrl', 'f')
    sleep(0.5)
    if busca_no_relatorio(nota['data'], validacao): 
        messagebox.showerror('Erro data', 'Erro ao procurar o data - ' + nota['data'])
        return True

    # Rodape
    hotkey('ctrl', 'f')
    sleep(0.5)
    if busca_no_relatorio(nota['rodape'], validacao): 
        messagebox.showerror('Erro rodape', 'Erro ao procurar o rodape - ' + nota['rodape'])
        return True

    # Operador
    hotkey('ctrl', 'f')
    sleep(0.5)
    if busca_no_relatorio(nota['operador'], validacao): 
        messagebox.showerror('Erro operador', 'Erro ao procurar o operador - ' + nota['operador'])
        return True

    press('esc')
    return False