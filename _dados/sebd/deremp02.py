# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DEREMP02:

    def __init__(self, codigo=0):
        self.codigo = codigo
        self.mensagem = ''

    def ac_consultar(self):
        existe = False
        try:
            # Pega o nome da empresa
            conexao.conn.on_cursor()
            sql = f"SELECT emp_nome_formal FROM sebd_eremp WHERE emp_codigo = " + str(self.codigo)
            conexao.conn.cursor.execute(sql)
            emp_cursor = conexao.conn.cursor.fetchone()
            if len(emp_cursor) > 0:
                self.nome_formal = str(emp_cursor[0])
                # Pega o movimento corrente
                sql = f"SELECT cfe_periodo, cfe_exercicio FROM sebd_epcfe WHERE cfe_empresa = " + str(self.codigo)
                conexao.conn.cursor.execute(sql)
                emp_cursor = conexao.conn.cursor.fetchone()
                if len(emp_cursor) > 0:
                    self.periodo = int(emp_cursor[0])
                    self.exercicio = int(emp_cursor[1])
                    existe = True
        except:
            self.mensagem = 'Erro ao consultar dados'
        finally:
            conexao.conn.off_cursor()
            return existe
