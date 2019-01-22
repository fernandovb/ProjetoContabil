# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DEFOPR:

    def __init__(self, empresa='', codigo='', descricao=''):
        self.empresa = empresa
        self.codigo = codigo
        self.descricao = descricao

    def fc_buscar(self):
        sql = ''
        try:
            if self.codigo != '':
                sql = f"eropr_codigo = '{str(self.codigo)}' "
            if self.descricao != '':
                if sql != '':
                    sql = sql + 'AND '
                sql = sql + f"eropr_nome LIKE '%{self.descricao}%' "
            sql = f'SELECT ' \
                      f'eropr_codigo, ' \
                      f'eropr_nome ' \
                      f'FROM sebd_eropr ' \
                      f"WHERE eropr_empresa = {self.empresa} AND " + sql
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            dados = conexao.conn.cursor.fetchall()
            return [True, dados]
        except:
            return [False, sql]
        finally:
            conexao.conn.off_cursor()
