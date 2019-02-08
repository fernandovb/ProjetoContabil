# -*- coding: utf-8 -*-

from _dados.prm.dpfpes import DPFPES
import _regras.sys.ssglob as ssglob


class RPFPES:

    def __init__(self, codigo='', nome_formal='', nome_alternativo='', federal=''):
        self.empresa = str(ssglob.SSGLOB.empresa)
        self.codigo = str(codigo)
        self.nome_formal = nome_formal
        self.nome_alternativo = nome_alternativo
        self.federal = federal

    def fc_buscar(self):
        busca = DPFPES(empresa=self.empresa,
                       codigo=self.codigo,
                       nome_formal=self.nome_formal,
                       nome_alternativo=self.nome_alternativo,
                       federal=self.federal)
        resultado = busca.fc_buscar()
        if resultado[0]:
            return resultado[1]
        else:
            return None
