# -*- coding: utf-8 -*-

from _dados.accl.dafcon import DAFCON


class RAFCON:

    def __init__(self, empresa='', codigo='', descricao=''):
        self.empresa = empresa
        self.codigo = codigo
        self.descricao = descricao

    def fc_buscar(self):
        busca = DAFCON(self.empresa, self.codigo, self.descricao)
        resultado = busca.fc_buscar()
        if resultado[0]:
            return resultado[1]
        else:
            return None
