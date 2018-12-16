# -*- coding: utf-8 -*-

import _dados.ssgcon as conexao
import _regras.ssglob as ssglob


class DAFCON:

    def __init__(self, empresa='', codigo='', descricao=''):
        self.empresa = empresa
        self.conta = codigo
        self.nome = descricao

    def fc_buscar(self):
        try:
            sql = ''
            if self.conta != '':
                sql = 'arpc_codigo=' + str(self.conta)
            if self.nome != '':
                if sql != '':
                    sql = sql + ' AND '
                sql = sql + "arpc_nome LIKE '%" + self.nome + "%'"
            sql = 'SELECT arpc_codigo, arpc_nome FROM accl_arpc WHERE ' + sql
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            dados = conexao.conn.cursor.fetchall()
            return [True, dados]
        except:
            return [False, 0]
        finally:
            conexao.conn.off_cursor()
