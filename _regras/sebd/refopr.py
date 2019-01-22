# -*- coding: utf-8 -*-

from _dados.sebd.defopr import DEFOPR
import _regras.sys.ssglob as ssglob


class REFOPR:

    def __init__(self, codigo='', descricao=''):
        self.empresa = str(ssglob.SSGLOB.empresa)
        self.codigo = codigo
        self.descricao = descricao

    def fc_buscar(self):
        busca = DEFOPR(empresa=self.empresa, codigo=self.codigo, descricao=self.descricao)
        resultado = busca.fc_buscar()
        if resultado[0]:
            return resultado[1]
        else:
            return None
