# -*- coding: utf-8 -*-

import _regras.ssglob as ssglob
from datetime import datetime
from _dados.accl.darslc import DARSLC, DARSLD


class RARSLC:

    def __init__(self, acao, num_documento=''):
        agora = datetime.today()
        self.acao = acao  # 0-Consultar, 1-Inlcuir, 2-Alterar
        self.empresa = ssglob.SSGLOB.empresa
        self.num_documento = num_documento
        self.dt_criacao = agora.strftime('%Y-%m-%d')
        self.dt_movimento = agora.strftime('%Y-%m-%d')
        self.periodo = ssglob.SSGLOB.periodo
        self.exercicio = ssglob.SSGLOB.exercicio
        self.usuario = ssglob.SSGLOB.matricula
        self.partidas = []

    def ac_gravar(self):
        grava = DARSLC(self.acao,
                       self.empresa,
                       self.num_documento,
                       self.dt_criacao,
                       self.dt_movimento,
                       self.periodo,
                       self.exercicio,
                       self.usuario)
        for partida in self.partidas:
            p = DARSLD(self.empresa,
                       self.num_documento,
                       partida.registro,
                       partida.situacao,
                       partida.tipo_registro,
                       partida.unidade,
                       partida.chave_registro,
                       partida.conta_contabil,
                       partida.centro_lucro,
                       partida.descricao,
                       partida.doc_referencia,
                       partida.doc_compensacao,
                       partida.montante,
                       partida.moeda)
            grava.partidas.append(p)
        self.num_documento = grava.ac_gravar()


class RARSLD:

    def __init__(self,
                 registro,
                 situacao=0,
                 tipo_registro='',
                 unidade=0,
                 chave_registro='D',
                 conta_contabil=0,
                 centro_lucro=0,
                 descricao='',
                 doc_referencia='',
                 doc_compensacao='',
                 montante=0.00,
                 moeda='BRL'):
        self.registro = int(registro)
        self.situacao = situacao
        self.tipo_registro = tipo_registro
        self.unidade = int(unidade)
        self.chave_registro = str(chave_registro).upper()
        self.conta_contabil = conta_contabil
        self.centro_lucro = centro_lucro
        self.descricao = str(descricao).upper()
        self.doc_referencia = str(doc_referencia)
        self.doc_compensacao = str(doc_compensacao)
        if (self.chave_registro == 'C') and (float(montante) > 0):
            self.montante = float(montante * -1)
        else:
            self.montante = float(montante)
        self.moeda = moeda.upper()
