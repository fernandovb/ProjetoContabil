# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao

class DARSLC:

    def __init__(self,
                 acao,
                 empresa,
                 num_documento,
                 dt_criacao,
                 dt_movimento,
                 periodo,
                 exercicio,
                 usuario):
        self.acao = acao
        self.empresa = empresa
        self.num_documento = num_documento
        self.dt_criacao = dt_criacao
        self.dt_movimento = dt_movimento
        self.periodo = periodo
        self.exercicio = exercicio
        self.usuario = usuario
        self.partidas = []

    def ac_gravar(self):
        try:
            self.num_documento = conexao.conn.fc_gera_cod_doc(self.empresa, 10)
            conexao.conn.on_cursor()
            sql = "INSERT INTO accl_arslc (" \
                  "arslc_empresa, " \
                  "arslc_num_documento, " \
                  "arslc_dt_criacao, " \
                  "arslc_dt_movimento, " \
                  "arslc_periodo, " \
                  "arslc_exercicio, " \
                  "arslc_usuario) " \
                  "VALUES ("
            sql = sql + str(self.empresa) + ", "
            sql = sql + "'" + str(self.num_documento) + "', "
            sql = sql + "'" + str(self.dt_criacao) + "', "
            sql = sql + "'" + str(self.dt_movimento) + "', "
            sql = sql + str(self.periodo) + ", "
            sql = sql + str(self.exercicio) + ", "
            sql = sql + "'" + str(self.usuario) + "')"
            conexao.conn.cursor.execute(sql)
            for partida in self.partidas:
                if not partida.ac_gravar(self.num_documento):
                    raise Exception()
            conexao.conn.commit()
            return self.num_documento
        except:
            return 0
        finally:
            conexao.conn.off_cursor()

class DARSLD:

    def __init__(self,
                 empresa,
                 num_documento,
                 registro,
                 situacao,
                 tipo_registro,
                 unidade,
                 chave_registro,
                 conta_contabil,
                 centro_lucro,
                 descricao,
                 doc_referencia,
                 doc_compensacao,
                 montante,
                 moeda):
        self.empresa = empresa
        self.num_documento = num_documento
        self.registro = registro
        self.situacao = situacao
        self.tipo_registro = tipo_registro
        self.unidade = unidade
        self.chave_registro = chave_registro
        self.conta_contabil = conta_contabil
        self.centro_lucro = centro_lucro
        self.descricao = descricao
        self.doc_referencia = doc_referencia
        self.doc_compensacao = doc_compensacao
        self.montante = montante
        self.moeda = moeda

    def ac_gravar(self, num_documento=''):
        try:
            self.num_documento = num_documento
            sql = "INSERT INTO accl_arsld (" \
                  "arsld_empresa, " \
                  "arsld_num_documento, " \
                  "arsld_registro, " \
                  "arsld_situacao, " \
                  "arsld_tipo_registro, " \
                  "arsld_unidade, " \
                  "arsld_chave_registro, " \
                  "arsld_conta_contabil, " \
                  "arsld_centro_lucro, " \
                  "arsld_descricao, " \
                  "arsld_doc_referencia, " \
                  "arsld_doc_compensacao, " \
                  "arsld_montante_doc, " \
                  "arsld_moeda) " \
                  "VALUES ("
            sql = sql + str(self.empresa) + ", "
            sql = sql + "'" + str(self.num_documento) + "', "
            sql = sql + str(self.registro) + ", "
            sql = sql + str(self.situacao) + ", "
            sql = sql + "'" + str(self.tipo_registro) + "', "
            sql = sql + str(self.unidade) + ", "
            sql = sql + "'" + str(self.chave_registro) + "', "
            sql = sql + str(self.conta_contabil) + ", "
            sql = sql + str(self.centro_lucro) + ", "
            sql = sql + "'" + str(self.descricao) + "', "
            sql = sql + "'" + str(self.doc_referencia) + "', "
            sql = sql + "'" + str(self.doc_compensacao) + "', "
            sql = sql + str(self.montante) + ", "
            sql = sql + "'" + str(self.moeda) + "')"
            conexao.conn.cursor.execute(sql)
            return True
        except:
            return False
