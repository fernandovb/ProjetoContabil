# -*- coding: utf-8 -*-

"""Retorna informações sobre operações comerciais
    Através da operação a ser realizada, será retornado o código do documento a ser gerado.

"""

import _dados.sys.ssgcon as conexao
import _regras.sys.ssglob as ssglob


class DELOPR:

    def __init__(self, operacao):
        self.empresa = ssglob.SSGLOB.empresa
        self.operacao = operacao

    def fc_busca(self):
        """Busca o documento a ser gerado, com base na operação informada

        :return: código do documento
        """
        try:
            sql = f"SELECT eropr_documento " \
                f"FROM sebd_eropr " \
                f"WHERE eropr_empresa={self.empresa} " \
                f"AND eropr_codigo='{str(self.operacao).upper()}'"
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            return int(conexao.conn.cursor.fetchone()[0])
        except:
            return 0
        finally:
            conexao.conn.off_cursor()
