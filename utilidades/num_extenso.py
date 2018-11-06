# encoding: utf-8
# module num_extenso
# from (built-in)
# version 0.01
# Author: Fernando Vicente Batista
# Contact: fernandovicente.batista@gmail.com
"""
Escreve um número por extenso

Lê um número float e converte para string com o extenso deste número.
Opção para inclusão de moeda.
"""

# no import


__all__ = [
    'extenso',
]


# Variables with simple values
__uni = {'1': 'um', '2': 'dois', '3': 'três', '4': 'quatro', '5': 'cinco', '6': 'seis', '7': 'sete',
         '8': 'oito', '9': 'nove'}
__dez = {'2': 'vinte', '3': 'trinta', '4': 'quarenta', '5': 'cinquenta', '6': 'sessenta', '7': 'setenta',
         '8': 'oitenta', '9': 'noventa'}
__deze = {'10': 'dez', '11': 'onze', '12': 'doze', '13': 'treze', '14': 'quatorze', '15': 'quinze',
          '16': 'dezesseis', '17': 'dezessete', '18': 'dezoito', '19': 'dezenove'}
__cen = {'2': 'duzentos', '3': 'trezentos', '4': 'quatrocentos', '5': 'quinhentos', '6': 'seiscentos',
         '7': 'setecentos', '8': 'oitocentos', '9': 'novecentos'}
__moedas = {
    'real': 'reais',
    'dolar': 'dolares',
    'euro': 'euros',
    'peso': 'pesos',
    'rubro': 'rubros',
    'libra': 'libras',
}


# Classes


class MyError(Exception):
    pass


class ZeroNumError(MyError):
    pass


# functions


def extenso(num, moeda=''):
    """Retorna um número por extenso
    Lê o número e retorna string com o extenso do número.

    :param num: número a ser lido
    :param moeda: informa qual moeda deverá ser utilizada.
    :return: string com extenso
    """
    if (num == 0) or (num == ''):
        raise ZeroNumError('Número vazio')
    e = False
    ext = ''
    numi = str(int(num)).zfill(9)
    for i in range(len(numi) - 3, -1, -3):
        if int(numi[i: i + 3]) != 0:
            if ext != '':
                if e:
                    ext = ' e ' + ext
                else:
                    ext = ', ' + ext
                if i == 3:
                    ext = ' mil' + ext
                if i < 3:
                    if int(numi[i: i + 3]) > 1:
                        ext = ' milhões' + ext
                    else:
                        ext = ' milhão' + ext
            ext = __triple_ext(numi[i: i + 3]) + ext
            if int(numi[i: i + 3]) <= 100:
                e = True
            else:
                e = False
        else:
            e = True
    if moeda != '':
        if int(numi) > 1:
            ext = ext + ' ' + __moedas[moeda]
        else:
            ext = ext + moeda
    b = int((num % 1) * 100)
    if b > 0:
        if ext != '':
            ext = ext + ' e '
        ext = ext + __triple_ext(b)
        if moeda != '':
            if b > 1:
                ext = ext + ' centavos'
            else:
                ext = ext + ' centavo'
        else:
            if b > 1:
                ext = ext + ' décimos'
            else:
                ext = ext + ' décimo'
    return ext


def __triple_ext(val):
    text = ''
    val = str(val).zfill(3)
    if val[1] == '1':
        text = __deze[val[1:3]]
    elif val[2] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        text = __uni[val[2]]
    if val[1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        if text != '':
            text = ' e ' + text
        text = __dez[val[1]] + text
    if val[0] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        if text != '':
            text = ' e ' + text
        text = __cen[val[0]] + text
    elif val[0] == '1':
        if text != '':
            text = 'cento e ' + text
        else:
            text = 'cem'
    return text
