# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DCRCTM:

    def __init__(self,
                 acao,
                 empresa,
                 contrato='',
                 operacao='',
                 unidade=0,
                 pessoa=0,
                 vigencia=0,
                 tp_vigencia=0,
                 situacao=0,
                 dt_emissao='',
                 dt_inicio='',
                 dt_termino='',
                 montante=0.00):
        self.acao = acao
        self.empresa = empresa
        self.contrato = contrato
        if acao == 2:
            self.situacao = situacao
            self.unidade = unidade
            self.operacao = operacao
            self.pessoa = pessoa
            self.vigencia = vigencia
            self.tp_vigencia = tp_vigencia
            self.dt_emissao = dt_emissao
            self.dt_inicio = dt_inicio
            self.dt_termino = dt_termino
            self.montante = montante
        self.litens = []

    def ac_gravar(self):
        try:
            self.contrato = conexao.conn.fc_gera_cod_doc(self.empresa, 45)
            conexao.conn.on_cursor()
            sql = "INSERT INTO clcm_crctm (" \
                  "crctm_empresa, " \
                  "crctm_codigo, " \
                  "crctm_situacao, " \
                  "crctm_operacao, " \
                  "crctm_unidade, " \
                  "crctm_pessoa, " \
                  "crctm_vigencia, " \
                  "crctm_tp_vigencia, " \
                  "crctm_dt_emissao, " \
                  "crctm_dt_inicio, " \
                  "crctm_dt_termino, " \
                  "crctm_montante) " \
                  "VALUES ("
            sql = sql + str(self.empresa) + ", "
            sql = sql + "'" + str(self.contrato) + "', "
            sql = sql + str(self.situacao) + ", "
            sql = sql + "'" + str(self.operacao) + "', "
            sql = sql + str(self.unidade) + ", "
            sql = sql + str(self.pessoa) + ", "
            sql = sql + str(self.vigencia) + ", "
            sql = sql + str(self.tp_vigencia) + ", "
            sql = sql + "'" + str(self.dt_emissao) + "', "
            sql = sql + "'" + str(self.dt_inicio) + "', "
            sql = sql + "'" + str(self.dt_termino) + "', "
            sql = sql + str(self.montante) + ")"
            conexao.conn.cursor.execute(sql)
            for item in self.litens:
                if not item.ac_gravar(self.contrato):
                    raise Exception()
            conexao.conn.commit()
            conexao.conn.off_cursor()
            return self.contrato
        except:
            return 0

    def ac_consultar(self):
        try:
            sql = "SELECT " \
                  "crctm_empresa, " \
                  "crctm_codigo, " \
                  "crctm_situacao, " \
                  "crctm_operacao, " \
                  "crctm_unidade, " \
                  "crctm_pessoa, " \
                  "crctm_vigencia, " \
                  "crctm_tp_vigencia, " \
                  "crctm_dt_emissao, " \
                  "crctm_dt_inicio, " \
                  "crctm_dt_termino, " \
                  "crctm_montante " \
                  "FROM clcm_crctm WHERE "
            sql = sql + "crctm_empresa = " + str(self.empresa) + " AND "
            sql = sql + "crctm_codigo = '" + str(self.contrato) + "'"
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            consulta = conexao.conn.cursor.fetchone()
            if len(consulta) > 0:
                self.empresa = consulta[0]
                self.contrato = consulta[1]
                self.situacao = consulta[2]
                self.operacao = consulta[3]
                self.unidade = consulta[4]
                self.pessoa = consulta[5]
                self.vigencia = consulta[6]
                self.tp_vigencia = consulta[7]
                self.dt_emissao = str(consulta[8])
                self.dt_inicio = str(consulta[9])
                self.dt_termino = str(consulta[10])
                self.montante = consulta[11]
            self.fc_consultar_itens()
            return True
        except:
            return False
        finally:
            conexao.conn.off_cursor()

    def fc_consultar_itens(self):
        sql = "SELECT " \
              "critm_empresa, " \
              "critm_contrato, " \
              "critm_codigo, " \
              "critm_situacao, " \
              "critm_tp_item, " \
              "critm_item, " \
              "critm_descricao, " \
              "critm_quantidade, " \
              "critm_val_unit, " \
              "critm_montante, " \
              "critm_moeda, " \
              "critm_imobilizado, " \
              "critm_form_pgto, " \
              "critm_cond_pgto, " \
              "critm_tp_pgto, " \
              "critm_conta_banc, " \
              "critm_cartao " \
              "FROM clcm_critm WHERE "
        sql = sql + "critm_empresa = " + str(self.empresa) + " AND "
        sql = sql + "critm_contrato = '" + str(self.contrato) + "'"
        conexao.conn.cursor.execute(sql)
        consulta = conexao.conn.cursor.fetchall()
        if len(consulta) > 0:
            for item in consulta:
                item_ad = DCRITM(empresa=item[0],
                                 contrato=item[1],
                                 codigo=item[2],
                                 situacao=item[3],
                                 tp_item=item[4],
                                 item=item[5],
                                 descricao=item[6],
                                 qtde=item[7],
                                 val_unit=item[8],
                                 val_total=item[9],
                                 moeda=item[10],
                                 imobilizado=item[11],
                                 form_pgto=item[12],
                                 cond_pgto=item[13],
                                 tp_cond_pgto=item[14],
                                 conta_banc=item[15],
                                 cartao=item[16])
                self.litens.append(item_ad)


class DCRITM:

    def __init__(self,
                 empresa,
                 contrato,
                 codigo=0,
                 situacao=0,
                 tp_item=0,
                 item=0,
                 descricao='',
                 qtde=0.00,
                 val_unit=0.00,
                 val_total=0.00,
                 moeda='',
                 imobilizado=0,
                 form_pgto='',
                 cond_pgto='',
                 tp_cond_pgto=0,
                 conta_banc=0,
                 cartao=0,
                 acao=0):
        self.acao = acao
        self.empresa = empresa
        self.contrato = contrato
        self.codigo = codigo
        self.situacao = situacao
        self.tp_item = tp_item
        self.item = item
        self.descricao = descricao
        self.qtde = qtde
        self.val_unit = val_unit
        self.val_total = val_total
        self.moeda = moeda
        self.imobilizado = imobilizado
        self.form_pgto = form_pgto
        self.cond_pgto = cond_pgto
        self.tp_cond_pgto = tp_cond_pgto
        self.conta_banc = conta_banc
        self.cartao = cartao

    def ac_gravar(self, contrato=''):
        try:
            self.contrato = contrato
            sql = "INSERT INTO clcm_critm (" \
                  "critm_empresa, " \
                  "critm_contrato, " \
                  "critm_codigo, " \
                  "critm_situacao, " \
                  "critm_tp_item, " \
                  "critm_item, " \
                  "critm_descricao, " \
                  "critm_quantidade, " \
                  "critm_val_unit, " \
                  "critm_montante, " \
                  "critm_moeda, " \
                  "critm_imobilizado, " \
                  "critm_form_pgto, " \
                  "critm_cond_pgto, " \
                  "critm_tp_pgto, " \
                  "critm_conta_banc, " \
                  "critm_cartao) VALUES ("
            sql = sql + str(self.empresa) + ", "
            sql = sql + "'" + str(self.contrato) + "', "
            sql = sql + str(self.codigo) + ", "
            sql = sql + str(self.situacao) + ", "
            sql = sql + str(self.tp_item) + ", "
            sql = sql + str(self.item) + ", "
            sql = sql + "'" + str(self.descricao) + "', "
            sql = sql + str(self.qtde) + ", "
            sql = sql + str(self.val_unit) + ", "
            sql = sql + str(self.val_total) + ", "
            sql = sql + "'" + str(self.moeda) + "', "
            sql = sql + str(self.imobilizado) + ", "
            sql = sql + "'" + str(self.form_pgto) + "', "
            sql = sql + "'" + str(self.cond_pgto) + "', "
            sql = sql + str(self.tp_cond_pgto) + ", "
            sql = sql + str(self.conta_banc) + ", "
            sql = sql + str(self.cartao) + ")"
            conexao.conn.cursor.execute(sql)
            return True
        except:
            return False
