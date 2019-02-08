# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DPFPES:

    def __init__(self, empresa='', codigo='', nome_formal='', nome_alternativo='', federal=''):
        self.empresa = empresa
        self.codigo = codigo
        self.nome_formal = nome_formal
        self.nome_alternativo = nome_alternativo
        self.federal = federal

    def fc_buscar(self):
        sql = ''
        try:
            if self.codigo != '':
                sql = f"eropr_codigo = {str(self.codigo)} "
            if self.nome_formal != '':
                if sql != '':
                    sql = sql + 'AND '
                sql = sql + f"prpes_nome_formal LIKE '%{self.nome_formal}%' "
            if self.nome_alternativo != '':
                if sql != '':
                    sql = sql + 'AND '
                sql = sql + f"prpes_nome_alternativo LIKE '%{self.nome_alternativo}%' "
            if self.federal != '':
                if sql != '':
                    sql = sql + 'AND '
                sql = sql + f"prpes_federal = '{self.federal}' "
            sql = f"SELECT " \
                      f"prpes_codigo, " \
                      f"prpes_nome_formal, " \
                      f"prpes_nome_alternativo, " \
                      f"prpes_federal " \
                      f"FROM prm_prpes " \
                      f"WHERE prpes_empresa = {self.empresa} AND " + sql
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            dados = conexao.conn.cursor.fetchall()
            return [True, dados]
        except:
            return [False, sql]
        finally:
            conexao.conn.off_cursor()
