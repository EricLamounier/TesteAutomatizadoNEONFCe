import pyperclip
import xml.etree.ElementTree as ET
"""
def teste():
    # Obter o XML da área de transferência
    xml_string = pyperclip.paste()

    # Verificar se o XML não está vazio
    if xml_string.strip() == "":
        print("Nenhum XML encontrado na área de transferência.")
        return

    # Analisar o XML
    xml_string = xml_string[2:]
    xml_string = xml_string.replace('-', '')
    print(xml_string)
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Erro ao analisar o XML:", e)
        return

    # Definir o namespace
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    # Encontrar o valor dentro da tag <uTrib>
    uTrib = root.find('.//nfe:det/nfe:prod/nfe:uTrib', ns)

    # Verificar se o elemento foi encontrado e imprimir o valor
    if uTrib is not None:
        valor_uTrib = uTrib.text
        print("Valor dentro da tag <uTrib>:", valor_uTrib)
    else:
        print("Tag <uTrib> não encontrada.")
"""
def contar_tags_uTrib(xml_string):
    # Analisar o XML
    root = ET.fromstring(xml_string)

    # Definir o namespace
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    # Encontrar todas as ocorrências da tag <uTrib>
    tags_uTrib = root.findall('.//nfe:det/nfe:prod/nfe:uTrib', ns)

    # Contar quantas vezes a tag <uTrib> aparece
    total_tags_uTrib = len(tags_uTrib)

    return total_tags_uTrib

# Exemplo de uso
xml_string = pyperclip.paste()  # Obter XML da área de transferência
total = contar_tags_uTrib(xml_string)
print("Total de tags <uTrib>:", total)