# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DPLPES:

    def __init__(self, codigo):
        self.codigo = codigo
        self.fc_localizar()

    def fc_localizar(self):
        sql = ''
        try:
            sql = """SELECT 
        `prm_prpes`.`prpes_codigo` AS `plpes_codigo`,
        `sebd_ernac`.`ernac_descricao` AS `plpes_nacionalidade`,
        `prm_prpes`.`prpes_est_civil` AS `plpes_est_civil`,
        `sebd_erocp`.`erocp_titulo` AS `plpes_atividade`,
        `prm_prpes`.`prpes_nome_formal` AS `plpes_nome_formal`,
        `prm_prpes`.`prpes_estadual` AS `plpes_estadual`,
        `prm_prpes`.`prpes_org_emissor` AS `plpes_org_emissor`,
        `prm_prpes`.`prpes_federal` AS `plpes_federal`
    FROM
        ((`prm_prpes`
        JOIN `sebd_ernac` ON ((`prm_prpes`.`prpes_nacionalidade` = `sebd_ernac`.`ernac_codigo`)))
        JOIN `sebd_erocp` ON ((`prm_prpes`.`prpes_atividade` = `sebd_erocp`.`erocp_codigo`)))"""
            sql = sql + " WHERE `prm_prpes`.`prpes_codigo` = " + str(self.codigo)
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            dados = conexao.conn.cursor.fetchone()
            self.nacionalidade = dados[1]
            self.est_civil = dados[2]
            self.atividade = dados[3]
            self.nome_formal = dados[4]
            self.estadual = dados[5]
            self.org_emissor = dados[6]
            self.federal = dados[7]
            return True
        except:
            return False
        finally:
            conexao.conn.off_cursor()
