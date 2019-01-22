# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DIFPRP:

    def __init__(self):
        pass

    def fc_busca_codigo(self, empresa, codigo):
        try:
            sql = f'SELECT ' \
                f'irprp_descricao, ' \
                f'irprp_medidor_1, ' \
                f'irprp_medidor_2 ' \
                f'FROM fvb_db.accl_irprp WHERE irprp_empresa = {empresa} AND irprp_codigo = {codigo}'
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            busca = conexao.conn.cursor.fetchone()
            self.empresa = empresa
            self.codigo = codigo
            self.descricao = busca[0]
            self.medidor_1 = busca[1]
            self.medidor_2 = busca[2]
            return True
        except:
            return False
        finally:
            conexao.conn.off_cursor()
