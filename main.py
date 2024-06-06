from cadastro_produtos import *
from cadastro_pessoas import *
from funcoes_gerais_neo import *
from vendas import *
from dados import *
from pyperclip import copy
from tkinter import messagebox

def sair(arg=''):
    press('esc')
    sleep(0.2)

etapas = [
    ('Parâmetros Gerais', 'sm010', [''], parametros_gerais),  # 1 Parametros Gerais
    ('Parâmetros Contabilização', 'sm004', [''], parametros_contabilizacao),  # 2 Parametros de Contabilização
    ('Cad. Operadora Cartão', 'sf029',[operadoraCartao1], cadastro_operadora_cartao), # 3 Operadora Cartão
    ('Cad. Transações', 'sf033', [''], cadastro_transacao), # 4
    ('', '', [transacao1], incluir_transacao), # 5
    ('', '', [transacao2], incluir_transacao), # 6
    ('', '', [transacao3], incluir_transacao), # 7
    ('', '', [''], sair), # 8
    ('', '', [validacaoTransacoes], valida_transacoes), # 9
    ('', '', [''], sair), # 10
    ('Cad. Finalizadora - Dinheiro', 'sp154', [finalizadora1], cadastro_finalizadora), # 11
    ('Cad. Finalizadora - A prazo', 'sp154', [finalizadora2], cadastro_finalizadora), # 12
    ('Cad. Finalizadora - Crédito 1x', 'sp154', [finalizadora3], cadastro_finalizadora), # 13
    ('Cad. Finalizadora - Débito', 'sp154', [finalizadora4], cadastro_finalizadora), # 14
    ('Cad. Finalizadora - Crédito 2x', 'sp154', [finalizadora5], cadastro_finalizadora), # 15
    ('Cad. Classificação Cliente', 'sp040', [classificacao1], cadastro_classificacao_cliente), # 16
    ('Cad. Cliente 5', 'sp038', [cliente5], cadastro_cliente_5), # 17
    ('Cadastro Produto Padrão', 'sp001', [produtoPadrao], cadastro_produto_padrao), # 18
    ('Cad. Produto 1', 'sp001', [produto1], cadastro_produto), # 19
    ('Cad. Produto 2', 'sp001', [produto2], cadastro_produto), # 20
    ('Cad. Produto 3', 'sp001', [produto3], cadastro_produto), # 21
    ('Cad. Unidade Tributável', 'sp001', [unidadeTributavel], cadastro_unidade_tributavel), # 22
    ('Ajuste de Estoque Produto 1', 'sp001', [produto1], ajustar_estoque), # 23
    ('Ajuste de Estoque Produto 2', 'sp001', [produto2], ajustar_estoque), # 24
    ('Ajuste de Estoque Produto 3', 'sp001', [produto3], ajustar_estoque), # 25
    ('Cad. Forma Pagamento - A vista', 'sv020', [formaPagamento1], cadastro_forma_pagamento), # 26
    ('Cad. Forma Pagamento - A prazo', 'sv020', [formaPagamento2], cadastro_forma_pagamento), # 27
    ('Cria Terminal NFC-e', '', [''], cria_terminal), # 28
    ('Configura Terminal NFC-e', '', [sincronizacao], configurar_terminal), # 29
    ('Entrar na NFC-e', '', [usuario], entrar_no_terminal), # 30
    ('DAV 1 - A Prazo', '', [dav1], dav), # 31
    ('DAV 2 - A Vista', '', [dav2], dav), # 32
    ('DAV Rápido 1', 'sv060', [davRapido1], dav_rapido), # 33
    ('DAV Rápido 2', 'sv060', [davRapido2], dav_rapido), # 34
    ('Importar DAV para NFC-e', '', [dav2], importar_para_nfce), # 35
    ('Importar DAV Rápido NFC-e', '', [davRapido2, 1], importar_para_nfce), # 36
    ('Venda Avulsa PDV 1', '', [vendaAvulsa1], venda_nfce_1), #37
    ('Venda Avulsa PDV 2', '', [vendaAvulsa2], venda_nfce_2), #38
    ('Venda Avulsa PDV 3', '', [vendaAvulsa3], venda_nfce_3), #39
    ('Conferência de XML', 'sp205', [''], validar_nfce_neo), # 40
    ('Fechar Caixa NFC-e', '', [''], fechar_caixa), # 41
    ('Verificar Notas - Confirmadas/Contingência', 'sp205', [''], verifica_notas_confirmadas), # 42
    ('Cancelar NFC-e\'s', 'sp205', [estoqueFinal], cancelar_nfce), # 43
    ('Verificar Notas - Canceladas', 'sp205', [''], verifica_notas_canceladas), # 44
    ('Verificar Estoque Final', 'sp001', [estoqueFinal], valida_estoque_final), # 45
]

def smokeNFCE(start_index, insere_mensagem, step):
    step(start_index - 0.2)
    for cont, (nomeTela, tela, dados, cadastro, *params) in enumerate(etapas, start=1):
        if start_index <= cont:
            copy('')
            cancelaExecucao = False
            if nomeTela != '': insere_mensagem('➤ ' + nomeTela)
                
            if tela != '': entra_na_tela(tela)

            if cadastro: cancelaExecucao = cadastro(*dados, *params)

            if cancelaExecucao or forcaCancelaExecucao['status']: # Se TRUE cancela a execucao
                insere_mensagem('✘ ' + nomeTela, 2)
                insere_mensagem(f'\nExecução interrompida.\nErro em: {tela.upper()} - {nomeTela}')
                return
            else:
                if nomeTela != '': insere_mensagem('✔ ' + nomeTela, 2)

            step(cont)

    insere_mensagem('✔ Teste Finalizado!')