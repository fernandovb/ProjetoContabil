# -*- coding: utf-8 -*-

from _dados.accl.dafcon import DAFCON


class RAFCON:

    def __init__(self, empresa='', codigo='', descricao='', ordem=''):
        self.empresa = empresa
        self.codigo = codigo
        self.descricao = descricao
        self.ordem = ordem

    def fc_buscar(self):
        busca = DAFCON(self.empresa, self.codigo, self.descricao, self.ordem)
        resultado = busca.fc_buscar()
        if resultado[0]:
            return resultado[1]
        else:
            return None
