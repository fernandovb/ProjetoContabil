# -*- coding: utf-8 -*-

from _dados.sebd.deremp02 import DEREMP02


class REREMP02:

    def __init__(self, codigo=0):
        self.codigo = int(codigo)
        self.mensagem = ''

    def fc_consultar(self):
        consulta = DEREMP02(self.codigo)
        consulta.ac_consultar()
        self.nome_formal = consulta.nome_formal
        self.periodo = consulta.periodo
        self.exercicio = consulta.exercicio
        self.mensagem = consulta.mensagem
