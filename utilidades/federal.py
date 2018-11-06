# encoding: utf-8
# module federal
# from (built-in)
# version 0.01
# Author: Fernando Vicente Batista
# Contact: fernandovicente.batista@gmail.com
"""
Análise de informações de cadastros federais brasileiros
"""

import re

__version__: str = 'Versão 0.01 - em desenvolvimento'

__all__ = [
    'limpa_cadastro',
    'formata_cadastro',
    'validar',
    'digito',
]


# Variables with simple values
n = {'CPF': 11, 'CNPJ': 14}


# Classes
class MyError(Exception):
    pass


class TamanhoError(MyError):
    pass


class DocVazioError(MyError):
    pass


# functions
def limpa_cadastro(doc: object, tipo: object = 'CPF') -> object:
    """Elimina caracteres especiais do cadastro federal deixando somente os números
    Além de eliminar os caracteres especiais verifica o comprimento do número do cadastro.
    Caso seja superior ao tamanho de 11 caracteres para CPF, ou 14 para CNPJ, retornaraá um erro.

    :param doc: informa o número do cadastro federal
    :param tipo: informa o tipo do cadastro federal, por padrão carrega CPF.
    :return: string com sequência de números sem caracteres especiais
    """
    docl = ''.join(re.findall('\d', doc)).zfill(n[tipo])
    if len(docl) > n[tipo]:
        raise TamanhoError(f'{tipo} deve conter no máximo {n[tipo]} números.')
    else:
        return docl


def formata_cadastro(doc, tipo='CPF'):
    """Formata número para padrão de exibição com caracteres especiais ('.', '/', '-')
    A função limpará o número informado, caso tenha algum caractere especial, e retornará
    no formato 000.000.000-00 para CPF e 00.000.000/0001-00 para CNPJ.

    :param doc: informa o número do cadastro federal
    :param tipo: informa o tipo do cadastro federal, por padrão carrega CPF.
    :return: string com sequência de número com formatação padrão
    """
    docl = limpa_cadastro(doc, tipo)
    docf = ''
    if tipo == 'CPF':
        for i in range(0, 9, 3):
            docf = docf + docl[i:i + 3]
            if i < 6:
                docf = docf + '.'
            else:
                docf = docf + '-' + docl[i + 3:]
        return docf
    elif tipo == 'CNPJ':
        docf = docl[0:2] + '.'
        for i in range(2, 9, 3):
            if i < 7:
                docf = docf + docl[i:i + 3] + '.'
            else:
                docf = docf + '/' + docl[i:i + 4] + '-' + docl[i + 4:]
                break
        return docf


def validar(doc: object, tipo: object = 'CPF') -> object:
    """Verifica se o cadastro federal é válido
    Testa se o dígito verificador do documento é válido

    :param doc: número do cadastro federal
    :param tipo: informa se é CPF ou CNPJ. O padrão é CPF
    :return: True, para documento válido, e False, para documento incorreto
    """
    docl = ''
    val = 0
    for i in range(0, len(doc)):
        if doc[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            docl = docl + doc[i]
    if len(docl) > n[tipo]:
        raise TamanhoError(f'{tipo} deve conter no máximo {n[tipo]} números.')
    if len(docl) <= 2:
        raise DocVazioError('Documento não possui digitos para análise')
    if tipo == 'CPF':
        docl = docl.zfill(n[tipo])
        for i in range(0, 9):
            val = val + (int(docl[i]) * (10 - i))
        dig = str((val * 10) % 11)
        val = 0
        for i in range(0, 10):
            val = val + (int(docl[i]) * (11 - i))
        dig = dig + str((val * 10) % 11)
        if dig == docl[-2:]:
            return True
        else:
            return False
    elif tipo == 'CNPJ':
        docl = docl.zfill(n[tipo])
        c = 5
        for i in range(0, 12):
            if c < 2:
                c = 9
            val = val + (int(docl[i]) * c)
            c = c - 1
        if (val % 11) < 2:
            dig = '0'
        else:
            dig = str(11 - (val % 11))
        val = 0
        c = 6
        for i in range(0, 13):
            if c < 2:
                c = 9
            val = val + (int(docl[i]) * c)
            c = c - 1
        if (val % 11) < 2:
            dig = dig + '0'
        else:
            dig = dig + str(11 - (val % 11))
        if dig == docl[-2:]:
            return True
        else:
            return False


def digito(doc, tipo='CPF', digv=True):
    """Calcula o digito correto do cadastro
    Ao ser informado o número do cadastro, sem o dígito, será calculado o digito correto

    :param doc: número do cadastro federal, sem o digito;
    :param tipo: informa se é CPF ou CNPJ;
    :param digv: informa se o digito verificador foi informado, mesmo que inválido. Se não houver digito,
    somente os demais números do CNPJ, informe True;
    :return: digito verificador com dois digitos.
    """
    docl = ''
    val = 0
    for i in range(0, len(doc)):
        if doc[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            docl = docl + doc[i]
    if len(docl) > n[tipo]:
        raise TamanhoError(f'{tipo} deve conter no máximo {n[tipo]} números.')
    if len(docl) <= 2:
        raise DocVazioError('Documento não possui digitos para análise')
    if tipo == 'CPF':
        if digv:
            docl = docl[:-2].zfill(9)
        else:
            docl = docl.zfill(9)
        for i in range(0, 9):
            val = val + (int(docl[i]) * (10 - i))
        dig = str((val * 10) % 11)
        docl = docl + dig
        val = 0
        for i in range(0, 10):
            val = val + (int(docl[i]) * (11 - i))
        dig = dig + str((val * 10) % 11)
        return str(dig)
    # Verifica o CNPJ
    elif tipo == 'CNPJ':
        if digv:
            docl = docl[:-2].zfill(12)
        else:
            docl = docl.zfill(12)
        c = 5
        for i in range(0, 12):
            if c < 2:
                c = 9
            val = val + (int(docl[i]) * c)
            c = c - 1
        if (val % 11) < 2:
            dig = '0'
        else:
            dig = str(11 - (val % 11))
        docl = docl + dig
        val = 0
        c = 6
        for i in range(0, 13):
            if c < 2:
                c = 9
            val = val + (int(docl[i]) * c)
            c = c - 1
        if (val % 11) < 2:
            dig = dig + '0'
        else:
            dig = dig + str(11 - (val % 11))
        return (str(dig))
    else:
        return 'Tamanho do documento incorreto. Favor verificar'
