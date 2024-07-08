forcaCancelaExecucao = { 'status': False}

banco = { 'ip_maquina': '127.0.0.1' }

erros = { 'cont': 0, 'janela': [] }

# Finalizadora Dinheiro
finalizadora1 = {
    'cod': '1',
    'finalizadora': 'Dinheiro',
    'tipo': 'dinheiro',
    'utilizacao': 'ambos',
    'geraCR': -1,
    'geraTEF': -1,
    'informaCliente': 'nao',
    'teclaAtalho': 'f3',
    'transacao': -1,
    'desconto': '0',
    'habPromocao': 'nao',
    'meioPagamento': 'dinheiro',  
    'validacao': ['Dinheiro', '1', 'Dinheiro', 'N', 'N', 'N', 'N', 'F3', 'Dinheiro', 'N', 'N', '1']
}

finalizadora2 = {
    'cod': '2',
    'finalizadora': 'A prazo',
    'tipo': 'outros',
    'utilizacao': 'ambos',
    'geraCR': 'sim',
    'geraTEF': -1,
    'informaCliente': -1,
    'teclaAtalho': 'f4',
    'transacao': -1,
    'desconto': '0',
    'habPromocao': 'nao',
    'meioPagamento': 'cartao da',  # Credito Loja / Crédito em Loja
    'validacao': ['A prazo', '2', 'Outros', 'S', 'N', 'S', 'N', 'F4', 'Cartão da Loja (Private Label)', 'N', 'N', '1']
}

finalizadora3 = {
    'cod': '3',
    'finalizadora': 'Cartão Crédito',
    'tipo': 'cartao',
    'utilizacao': 'ambos',
    'geraCR': -1,
    'geraTEF': 'nao',
    'informaCliente': 'nao',
    'teclaAtalho': 'f5',
    'transacao': '1',
    'desconto': '0',
    'habPromocao': 'nao',
    'meioPagamento': 'cartao de cre',  
    'validacao': ['Cartão Crédito', '3', 'Cartão', 'N', 'N', 'N', 'N', 'F5', 'Cartão de Crédito', 'N', 'N', '1']
}

finalizadora4 = {
    'cod': '4',
    'finalizadora': 'Cartão Débito',
    'tipo': 'cartao',
    'utilizacao': 'ambos',
    'geraCR': -1,
    'geraTEF': 'nao',
    'informaCliente': 'nao',
    'teclaAtalho': 'f6',
    'transacao': '2',
    'desconto': '0',
    'habPromocao': 'nao',
    'meioPagamento': 'cartao de de',  
    'validacao': ['Cartão Débito', '4', 'Cartão', 'N', 'N', 'N', 'N', 'F6', 'Cartão de Débito', 'N', 'N', '1']
}

finalizadora5 = {
    'cod': '5',
    'finalizadora': 'Crédito 2x',
    'tipo': 'cartao',
    'utilizacao': 'ambos',
    'geraCR': -1,
    'geraTEF': 'nao',
    'informaCliente': 'nao',
    'teclaAtalho': 'f7',
    'transacao': '3',
    'desconto': '0',
    'habPromocao': 'nao',
    'meioPagamento': 'cartao de cre',  
    'validacao': ['Crédito 2x', '5', 'Cartão', 'N', 'N', 'N', 'N', 'F7', 'Cartão de Crédito', 'N', 'N', '1']
}

operadoraCartao1 = {
    'operadora': '#empresa1',
    'validacao': ['#empresa1', 'Cartão a Receber', 'S', '']
}

transacao1 = {
    'transacao': 'crédito a vista',
    'taxa': '1',
    'tipo': 'credito',
    'qtdParcelas': -1
}

transacao2 = {
    'transacao': 'débito',
    'taxa': '0.5',
    'tipo': 'debito',
    'qtdParcelas': -1
}

transacao3 = {
    'transacao': 'crédito 2x',
    'taxa': '1.2',
    'tipo': 'parcelado',
    'qtdParcelas': '2'
}

validacaoTransacoes = {'validacao': ['Crédito 2x', 'Elo', 'Cartão a Receber', '0', '1,20', '0,00', 'Parcelado', 'S', 'S', 'Crédito a Vista', 'Elo', 'Cartão a Receber', '0', '1,00', '0,00', 'Crédito', 'S', 'S', 'Débito', 'Elo', 'Cartão a Receber', '0', '0,50', '0,00', 'Débito', 'S', 'S', ''], }

validacaoTerminal = {
    1: ['\nInformação', '\n---------------------------', '\nTerminal NFC-e configurado com sucesso.', '\n---------------------------', '\nOK   ', '\n---------------------------', '\n'],
    2: ['\nInformação', '\n---------------------------', '\nO sistema precisa ser reiniciado.', '\n---------------------------', '\nOK   ', '\n---------------------------', '\n'],
}
# Cliente Classificação
classificacao1 = {
    'classificacao': 'Bloqueia Limite',
    'mensagem': 'bloqueia limite',
    'bloqueiaVendaAPrazo': 'nao',
    'bloqueiaAtraso': 'nao',
    'bloqueiaLimiteCredito': 'bloqueia',
    'validacao': ['Bloqueia Limite', '2', 'Não', 'Bloqueia', 'Não', 'Bloqueia', 'Não', 'Bloqueia', 'Não', 'Bloqueia', 'Não', 'Bloqueia', 'Não', 'Bloqueia', 'Avisa', 'Avisa', 'Não', 'Bloqueia', 'Não', 'Bloqueia', '0', '0', 'Bloqueia Limite', 'S', '']
}

cliente5 = {
    'nome': '#pessoa5',
    'tipoPessoa': 'juridica',
    'doc': '48.149.882/0001-88',
    'nomeUsual': 'Usual Cliente 5',
    'cep': '38800000',
    'logradouro': '1',
    'numero': 's/n',
    'bairro': '1',
    'municipio': '3162104',
    'telefone': '3892345947',
    'classificacao': '2',
    'validacao': ['\n', 'CEP', 'Cód. Município', 'Município', 'UF', 'Caixa Postal', 'Foto', 'Nascimento', '#pessoa5', 'Usual Cliente 5', '7', '48.149.882/0001-88', 'Não Contribuinte', '', 'S', '', '', '', '', '', '', '0', 'Avenida Rui Barbosa', 'S/n', 'Centro', '', '38800-000', '3162104', 'São Gotardo', 'MG', '', '', '', '']
}

produtoPadrao = {
    'nome': 'padrao',
    'marca': '1',
    'unidade': '1',
    'grupo': '1',
    'subgrupo': '1',
    'venda': '1',
}

produto1 = {
    'cod': '1',
    'barras': '1000000000016',
    'nome': '#produto1',
    'controlaEstoque': 'normal',
    'venda': '3',
    'quantidadeEstoque': '301',
    'ultimoCusto': '2.59',
    'cfop': '5102',
    'cst': '103',
    'aliquotaICMS': '21',
    'nfce': '21',
    'validacao': ['#produto1', '1', '1000000000016', '0,00', '3,00', '0,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '103', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '0,000', '0,00', 'UN', '0', 'T', 'T', '1001.19.00', '', '0,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '0,00', '0,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
    'validacaoAjusteEstoque':  ['#produto1', '1', '1000000000016', '2,59', '3,00', '301,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '103', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '301,000', '2,59', 'UN', '0', 'T', 'T', '1001.19.00', '', '0,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '15,83', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
}

produto2 = {
    'cod': '2',
    'barras': '1000000000023',
    'nome': '#produto2',
    'controlaEstoque': 'normal',
    'venda': '20',
    'quantidadeEstoque': '132',
    'ultimoCusto': '15,37',
    'cfop': '5102',
    'cst': '900',
    'aliquotaICMS': '2',
    'nfce': '2',
    'validacao': ['#produto2', '2', '1000000000023', '0,00', '20,00', '0,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '0,000', '0,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '0,00', '0,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
    'validacaoAjusteEstoque': ['#produto2', '2', '1000000000023', '15,37', '20,00', '132,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '132,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', '']
}

produto3 = {
    'cod': '3',
    'barras': '100',
    'nome': '#produto3',
    'controlaEstoque': 'grade',
    'venda': '60',
    'ultimoCusto': '50',
    'quantidadeEstoque': '100',
    'cfop': '5102',
    'cst': '900',
    'aliquotaICMS': '2',
    'nfce': '2',
    'validacao': ['#produto3', '3', '100', '0,00', '60,00', '0,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '0,000', '0,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '0,00', '0,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
    'validacaoAjusteEstoque':  ['#produto3', '3', '100', '50,00', '60,00', '100,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '100,000', '50,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '20,00', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
}

produto3Var1 = {
    'quantidade': '50',
    'barras': 'a1b1',
}

produto3Var2 = {
    'quantidade': '50',
    'barras': 'a2b2',
}

formaPagamento1 = { # A vista
    'cod': '1',
    'forma': 'a vista',
    'tipo': 'a vista',
    'qntParcela': '-1',
    'entrada': '-1',
    'diasEntrada': '-1',
    'tipoVencimento': '-1',
    'tipoJuros': '-1',
    'juros': '-1',
    'utiliza': '0',
    'ajusteCentavos': '0',
    'desconto': '0',
    'meioPagamento': 'dinheiro',
    'finalizadora': '1',
    'validacao': ['A Vista', '1', 'A Vista', '0', '1', 'S', '0', 'S', 'Ambos', 'Dinheiro', '', 'Dinheiro']
}

# Forma de Pagamento
formaPagamento2 = { # A prazo
    'cod': '1',
    'forma': 'a prazo',
    'tipo': 'crediario',
    'qntParcela': '2',
    'entrada': 'nao',
    'diasEntrada': '-1',
    'tipoVencimento': 'mensal',
    'tipoJuros': '-1',
    'juros': '0',
    'utiliza': '0',
    'ajusteCentavos': '0',
    'desconto': '0',
    'meioPagamento': 'cartao da', # credito em loja / crédito loja
    'finalizadora': '2',
    'validacao': ['A Prazo', '2', 'Crediário', '0', '2', 'N', '0', 'S', 'Ambos', 'Cartão da Loja (Private Label)', '', 'A prazo']
}

sincronizacao = {
    'rapida': ['  ✔\tCONFIGURACOES', '\n  ✔\tEMPRESA', '\n  ✔\tACESSO', '\n  ✔\tINTERFACE', '\n  ✔\tALIQUOTAPROGRAMADAECF', '\n  ✔\tALIQUOTAS', '\n  ✔\tBAIRRO', '\n  ✔\tUNIDADEMEDIDA', '\n  ✔\tCLIENTECLASSIFICACAO', '\n  ✔\tFINALIZADORA', '\n  ✔\tFORMAPAGAMENTO', '\n  ✔\tHISTORICO', '\n  ✔\tTIPOLOTE', '\n  ✔\tGRUPO', '\n  ✔\tSETOR', '\n  ✔\tSUBGRUPO', '\n  ✔\tGRUPOSERVICO', '\n  ✔\tSUBGRUPOSERVICO', '\n  ✔\tLOGRADOURO', '\n  ✔\tPROFISSAO', '\n  ✔\tMARCA', '\n  ✔\tTIPOCONTATO', '\n  ✔\tTERMINAL', '\n  ✔\tDISTRITO', '\n  ✔\tCARENCIA', '\n  ✔\tDOCUMENTO', '\n  ✔\tFORMACOBRANCA', '\n  ✔\tPLANOCONTAS', '\n  ✔\tPARAMETROS', '\n  ✔\tPESSOA', '\n  ✔\tPESSOABIOMETRIA', '\n  ✔\tCLASSIFICACAOCONTRIBUINTEIPI', '\n  ✔\tEMPRESAPESSOA', '\n  ✔\tPESSOAENDERECO', '\n  ✔\tPESSOAFISICA', '\n  ✔\tPRIVILEGIO', '\n  ✔\tPRIVILEGIOACESSO', '\n  ✔\tPRIVILEGIOINTERFACE', '\n  ✔\tPRODUTO', '\n  ✔\tEMBALAGEM', '\n  ✔\tPRODUTOEMBALAGEM', '\n  ✔\tVARIACAOCOR', '\n  ✔\tVARIACAOTAMANHO', '\n  ✔\tVARIACAOITEMPRODUTO', '\n  ✔\tPRODUTOGRUPO', '\n  ✔\tSERVICO', '\n  ✔\tTOTALIZADORNAOFISCAL', '\n  ✔\tTOTALIZADORNAOFISCALTERMINAL', '\n  ✔\tUSUARIO', '\n  ✔\tFUNCIONARIO', '\n  ✔\tOBSERVACAOITEMVENDA', '\n  ✔\tCLIENTE', '\n  ✔\tCLIENTEDESCONTOPDV', '\n  ✔\tCLIENTEPESSOAFISICA', '\n  ✔\tUSUARIOEMPRESA', '\n  ✔\tPARAMETROECF', '\n  ✔\tCADASTROPADRAO', '\n  ✔\tFILTROPADRAO', '\n  ✔\tCLIENTEPLANOCONTAS', '\n  ✔\tCHEQUECADASTRO', '\n  ✔\tCONTACORRENTE', '\n  ✔\tCARTAOBANDEIRA', '\n  ✔\tCARTAOADQUIRENTE', '\n  ✔\tCARTAOADBANDEIRA', '\n  ✔\tCARTAOADBANDEIRAITEM', '\n  ✔\tPROMOCAOSCANTECH', '\n  ✔\tPROMOCAO', '\n  ✔\tPROMOCAOITEM', '\n  ✔\tPROMOCAOITEMFORMAPAGAMENTO', '\n  ✔\tPROMOCAOITEMGRUPO', '\n  ✔\tPROMOCAOITEMMARCA', '\n  ✔\tPROMOCAOITEMSUBGRUPO', '\n  ✔\tPROMOCAOITEMPRODUTO', '\n  ✔\tPROMOCAOITEMBONUS', '\n  ✔\tPROMOCAOITEMDESCONTOCLIENTE', '\n  ✔\tCONSOLIDACAO', '\n  ✔\tCONSOLIDACAOEMPRESA', '\n  ✔\tPESSOACONTATO', '\n  ✔\tFINALIZADORATRANSACAO', '\n  ✔\tCFOPCONTACONTABIL', '\n  ✔\tCONTADOR', '\n  ✔\tPRODUTOTRIBUTACAONFCE', '\n  ✔\tPARAMETROSREALTEC', '\n  ✔\tPARAMETROSREALTECTERMINAL', '\n  ✔\tPRODUTOLOTE', '\n  ✔\tCERTIFICADO', '\n  ✔\tPRODUTOFOTO', '\n  ✔\tPRODUTOUNIDADETRIBUTAVEL', '\n  ✔\tEMPRESAPESSOAEMAIL', '\n  ✔\tCAMPOCUSTOMIZADO', '\n  ✔\tPRODUTOBARRASALTERNATIVO', '\n  ✔\tCOMBUSTIVELMONOFASICO', '\n  ✔\tPAGAMENTOINSTANTANEO', '\n  ✔\tPAGAMENTOINSTANTANEOCHAVE', '\n  ✔\tCONTACORRENTEUSUARIO', '\n  ✔\tCONTABANCARIA', '\n  ✔\tPLATAFORMA', '\n  ✔\tPLATAFORMAPARAMETROS', '\n  ✔\tCAIXAECF', '\n  ✔\tVENDARAPIDA', '\n  ✔\tVENDARAPIDAFINALIZADORA', '\n  ✔\tITEMVENDARAPIDA', '\n  ✔\tVENDARAPIDANFCE', '\n  ✔\tITEMVENDASERVICO', '\n  ✔\tVARIACAOITEMVENDARAPIDA', '\n  ✔\tMOVIMENTOCAIXAECF', '\n  ✔\tVENDARAPIDAFINALIZADORATEF', '\n  ✔\tVENDARAPIDAMOVCAIXAECF', '\n  ✔\tTOTALIZADORGERAL', '\n  ✔\tVENDARAPIDACLIENTE', '\n  ✔\tCONTASRECEBER', '\n  ✔\tVENDARAPIDACR', '\n  ✔\tLANCAMENTO', '\n  ✔\tLANCAMENTOPARTIDA', '\n  ✔\tCRLANC', '\n  ✔\tCONTADORCNF', '\n  ✔\tVENDARAPIDACONTADORCNF', '\n  ✔\tAUTORIZARVENDA', '\n  ✔\tVENDARAPIDAAUTORIZAVENDA', '\n  ✔\tCONTASRECEBERCARTAOADBANDEIRA', '\n  ✔\tNOTAFISCALVENDACONSUMIDOR', '\n  ✔\tNOTAFISCALVENDACONSUMIDORITEM', '\n  ✔\tVENDARAPIDANFSERIED', '\n  ✔\tPRODUTONAOCADASTRADOECF', '\n  ✔\tCARTAOPARCELAMENTO', '\n  ✔\tCARTAOPARCELAMENTOCR', '\n  ✔\tCRRECEBIMENTO', '\n  ✔\tCARTAOPARCRCRECEBIMENTO', '\n  ✔\tREPOSITORIOXML', '\n  ✔\tPRODUTOLOTEITEMVENDARAPIDA', '\n  ✔\tITEMVENDARAPIDAOBS', '\n  ✔\tPROMOCAOITEMVENDARAPIDA', '\n  ✔\tVENDARAPIDACANCELAMENTO', '\n  ✔\tVENDARAPIDAITEMCANCELAMENTO', '\n  ✔\tCLIENTECREDITO', '\n  ✔\tVENDARAPIDAFINCLIENTECREDITO', '\n  ✔\tCONFERENCIACAIXA', '\n  ✔\tCONFERENCIACAIXALANCAMENTO', '\n  ✔\tPIX', '\n  ✔\tPIXCR', '\n  ✔\tPIXLANCAMENTO', '\nSincronização Concluída.', '\n'],
}

usuario = {
    'usuario': '#usuario1',
    'login': 'u1',
    'senha': '1'
}

dav1 = {
    'cfop': '5102',
    'cliente': '1',
    'funcionario': '1',
    'pagamento': '2',
    'produtos': 
    [
        {'cod': '1', 
         'produto': '#produto1',
         'barras': '1000000000016', 
         'quantidade': '10', 
         'desconto': '0',
         'validacao':['#produto1', '1', '1000000000016', '2,59', '3,00', '291,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '103', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '291,000', '2,59', 'UN', '0', 'T', 'T', '1001.19.00', '', '0,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '15,83', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', '']
         }
    ],
    'validacaoVenda': ['', '1', 'P', '10,00', '1', '1000000000016', '', '#produto1', '5.102', '3,00', '0,00', '0,00', '30,00', '', '#pessoaresponsável', '1001.19.00', '-- Outros', '5.102', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', 'Unidade'],
    'validacaoFinanceiro': ['1/1', '07/03/2024', '', '15,00', '0,00', '15,00', '1/2', '07/04/2024', '', '15,00', '0,00', '15,00'],
    'validacaoDav': ['#pessoa1', '1', '1', '30,00', 'Confirmado', 'S', 'S', 'Pedido Venda', '', 'Não', '', '', '00:00', '', '', '', '', '', 'MG', 'São Gotardo', '', '#pessoaresponsável', 'Venda', '', 'A Prazo', '5.102', 'Sem Ocorrência de Transporte', '0,00', '30,00', '0,00', '0,00', '0,00', '0,00', '30,00', '0,00', '0,00', '0,00', '0,00', '', '', ''],
    'comprovante': {
        'cnpj': '04.248.801/0001-21',
        'cliente': 'Cliente: 1 - #pessoa1',
        'cpf': '341.010.576-05',
        'endereco': 'Avenida Rui Barbosa, S/n',
        'total': '30',
        'parcela1': '15',
        'parcela2': '15',
        'vencimento1': '', # Data atual + 1 mes
        'vencimento2': '', # Data atual + 2 meses
        'liquido': '30',
        'data': '', # Data atual
        'operador': '#usuário1'
    },
    'nota': {
        'cnpj': '04.248.801/0001-21',
        'cpf': '341.010.576-05',
        'data': '',
        'rodape': 'Cliente: 1 - #pessoa1 CPF: 341.010.576-05',
        'operador': '#usuário1'
    }
}

dav2 = {
    'cfop': '5102',
    'cliente': '2',
    'funcionario': '1',
    'pagamento': '1',
    'produtos': 
    [
        {'cod': '2', 
         'produto': '#produto2',
         'barras': '1000000000023', 
         'quantidade': '15', 
         'desconto': '0.85',
         'validacao':['#produto2', '2', '1000000000023', '15,37', '20,00', '117,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '117,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', '']
         }
    ],
    'validacaoVenda': ['', '1', 'P', '15,00', '2', '1000000000023', '', '#produto2', '5.102', '20,00', '0,00', '0,85', '299,15', '', '#pessoaresponsável', '1001.19.00', '-- Outros', '5.102', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', 'Unidade'],
    'validacaoDav': ['#pessoa2', '1', '1', '30,00', 'Confirmado', 'S', 'S', 'Pedido Venda', '', 'Não', '', '', '00:00', '', '', '', '', '', 'MG', 'São Gotardo', '', '#pessoaresponsável', 'Venda', '', 'A Vista', '5.102', 'Sem Ocorrência de Transporte', '0,00', '299,15', '0,00', '0,00', '0,00', '0,00', '299,15', '0,00', '0,00', '0,00', '0,00', '', '', ''],
    'nota': {
        'cnpj': '04.248.801/0001-21',
        'cpf': '04.140.757/0001-31',
        'data': '',
        'rodape': 'Cliente: 2 - #pessoa2 CNPJ: 04.140.757/0001-31',
        'operador': '#usuário1'
    }
}

davRapido1 = {
    'cliente': '1',
    'funcionario': '1',
    'pagamento': '2',
    'abertura': 1,
    'produtos': 
    [
        {'cod': '3', 
         'produto': '#produto3',
         'barras': '100', 
         'quantidade': '10', 
         'validacao':  ['#produto3', '3', '100', '50,00', '60,00', '90,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '90,000', '50,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '20,00', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
         'variacao1': '0',
         'variacao2': '10'
        },
    ],
    'comprovante': {
        'cnpj': '04.248.801/0001-21',
        'cliente': 'Cliente: 1 - #pessoa1',
        'cpf': '341.010.576-05',
        'endereco': 'Avenida Rui Barbosa, S/n',
        'total': '600',
        'parcela1': '300',
        'parcela2': '300',
        'vencimento1': '', # Data atual + 1 mes
        'vencimento2': '', # Data atual + 2 meses
        'liquido': '600',
        'data': '', # Data atual
        'operador': '#usuário1'
    },
    'nota': {
        'cnpj': '04.248.801/0001-21',
        'cpf': '341.010.576-05',
        'data': '',
        'rodape': 'Cliente: 1 - #pessoa1 CPF: 341.010.576-05',
        'operador': '#usuário1'
    },
    'tela1': 'davrapido1_tela1',
    'tela2': 'davrapido1_tela2',
    'tela3': 'davrapido1_financeiro',
    'dav': 'davrapido1'
}

davRapido2 = {
    'cliente': '4',
    'funcionario': '1',
    'pagamento': '1',
    'abertura': 0,
    'produtos': 
    [
        {'cod': '2', 
         'produto': '#produto2',
         'barras': '1000000000023', 
         'quantidade': '2', 
         'validacao':   ['#produto2', '2', '1000000000023', '15,37', '20,00', '117,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '117,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', ''],
        },
    ],
    'comprovante': { # TODO TIRAR O PRINT DE NOVO POIS ESTA ERRADO O CLIENTE
        'cnpj': '04.248.801/0001-21',
        'cliente': 'Cliente: 4 - #pessoa5',
        'cpf': '341.010.576-05',
        'endereco': 'Avenida Rui Barbosa, S/n',
        'total': '600',
        'parcela1': '300',
        'parcela2': '300',
        'vencimento1': '', # Data atual + 1 mes
        'vencimento2': '', # Data atual + 2 meses
        'liquido': '600',
        'data': '', # Data atual
        'operador': '#usuário1'
    },
    'nota': { # TODO TIRAR PRINT DE NOVO POIS ESTA ERRADO O CLIENTE
        'cnpj': '04.248.801/0001-21',
        'cpf': '48.149.882/0001-88',
        'data': '',
        'rodape': 'Cliente: 4 - #pessoa5 CNPJ: 48.149.882/0001-88',
        'operador': '#usuário1'
    },
    'tela1': 'davrapido2_tela1',
    'tela2': 'davrapido2_tela2',
    'dav': 'davrapido2'
}

vendaAvulsa1 = {
    'cod': '1',
    'produtos': [
        {
            'barras': '1000000000016',
            'produto': '#produto1',
            'quantidade': '1',
            'variacao': -1,
            'travaSistema': False,
            'validacao': ['#produto1', '1', '1000000000016', '2,59', '3,00', '290,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '103', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '290,000', '2,59', 'UN', '0', 'T', 'T', '1001.19.00', '', '0,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '15,83', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],

        },
        {
            'barras': '1000000000023',
            'produto': '#produto2',
            'quantidade': '1',
            'variacao': -1,
            'travaSistema': False,
            'validacao': ['#produto2', '2', '1000000000023', '15,37', '20,00', '114,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '114,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', ''],


        },
        {
            'barras': '100',
            'produto': '#produto3',
            'quantidade': '1',
            'variacao': '1',
            'travaSistema': False,
            'validacao': ['#produto3', '3', '100', '50,00', '60,00', '89,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '89,000', '50,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '20,00', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', '']

        }
    ],
    'cliente': -1,
    'finalizadora': '5', # Credito 2x
    'desconto': '0',
    'autorizaVenda': False,
}

vendaAvulsa2 = {
    'cod': '2',
    'produtos': [
        {
            'barras': '1000000000023',
            'produto': '#produto2',
            'quantidade': '25',
            'variacao': -1,
            'travaSistema': False,
            'validacao': ['#produto2', '2', '1000000000023', '15,37', '20,00', '89,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '89,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', '']

        },
    ],
    'cliente': '4',
    'finalizadora': '2', # A prazo
    'desconto': '0',
    'autorizaVenda': True,
    'comprovante': {
        'cnpj': '04.248.801/0001-21',
        'cliente': 'Cliente: 4 - #pessoa5',
        'cpf': '48.149.882/0001-88',
        'endereco': 'Avenida Rui Barbosa, S/n',
        'total': '500',
        'parcela1': '250',
        'parcela2': '250',
        'vencimento1': '', # Data atual + 1 mes
        'vencimento2': '', # Data atual + 2 meses
        'liquido': '500',
        'data': '', # Data atual
        'operador': '#usuário1'
    },
    'nota': {
        'cnpj': '',
        'cpf': '48.149.882/0001-88',
        'data': '',
        'rodape': 'Cliente: 4 - #pessoa5 CNPJ: 48.149.882/0001-88',
        'operador': '#usuário1'
    },
}

vendaAvulsa3 = {
    'cod': '3',
    'produtos': [
        {
            'barras': '1000000000023',
            'produto': '#produto2',
            'quantidade': '120',
            'variacao': -1,
            'quantidadeCorreta': '12',
            'travaSistema': True,
            'validacao': ['#produto2', '2', '1000000000023', '15,37', '20,00', '77,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '77,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', ''],

        },
    ],
    'cliente': -1,
    'finalizadora': '4', # Débito
    'desconto': '150',
    'descontoCorreto': '15',
    'autorizaVenda': True,
}

unidadeTributavel = {
    'produto': '#produto2',
    'unidade': 'caixa',
    'simbolo': 'cx',
    'barras': '012345678912',
    'quantidade': '5',
    'validacao': ['#produto2', '2', '1000000000023', '0,00', '20,00', '0,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '0,000', '0,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '0,00', '0,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', '']
}

valicadaoCancelarNfce = {
    1: ['\nInformação', '\n---------------------------', '\nNFC-e deve estar confirmada para ser cancelada.', '\n---------------------------', '\nOK   ', '\n---------------------------', '\n'],
}

estoqueFinal = {
    'produtos': [
        {
            'produto': '#produto1',
            'validacao': ['#produto1', '1', '1000000000016', '2,59', '3,00', '291,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '103', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '291,000', '2,59', 'UN', '0', 'T', 'T', '1001.19.00', '', '0,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '15,83', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
        },
        {
            'produto': '#produto2',
            'validacao': ['#produto2', '2', '1000000000023', '15,37', '20,00', '117,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '117,000', '15,37', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '30,12', '-100,00', '012345678912', 'CX', '5,00', '0,00', '0,00', '0,00', '', '0,00', ''],
        },
        {
            'produto': '#produto3',
            'validacao': ['#produto3', '3', '100', '50,00', '60,00', '100,000', '0,00', '0,00', 'S', '0,00', 'Unidade', '900', 'Teste Marca', 'Teste Grupo', 'Teste Subgrupo', '', '00 - Mercadoria para Revenda', '00', '0', '0', '0,000', '0,000', '0,000', '100,000', '50,00', 'UN', '12', 'T', 'T', '1001.19.00', '', '12,00', '', '0', '', '', 'Nenhum', '', '', 'N', '', '0,000', '0,00', '0,00', '0,00', '5.102', '0,000', '0,000', '0,00', '0,00', '20,00', '-100,00', '', '', '', '0,00', '0,00', '0,00', '', '0,00', ''],
        }
    ]
}
