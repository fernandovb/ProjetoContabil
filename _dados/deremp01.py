# -*- coding: utf-8 -*-

import _dados.ssgcon as conexao


class DEREMP01:
    global conn

    def __init__(self,
                 codigo,
                 situacao=0,
                 tipo='',
                 nome_formal='',
                 nome_alternativo='',
                 logradouro='',
                 numero='',
                 bairro='',
                 municipio='',
                 estado=''):
        self.acao = 0
        self.codigo = int(codigo)
        self.situacao = str(situacao)
        self.tipo = str(tipo)
        self.nome_formal = str(nome_formal)
        self.nome_alternativo = str(nome_alternativo)
        self.logradouro = str(logradouro)
        self.numero = str(numero)
        self.bairro = str(bairro)
        self.municipio = str(municipio)
        self.estado = str(estado)
        self.tot_capital = 0.00
        self.tot_quotas = 0.00
        self.val_quotas = 0.00
        self.lsocios = []

    def ac_consultar(self):
        try:
            conexao.conn.on_cursor()
            sql = f"SELECT " \
                      f"emp_codigo, " \
                      f"emp_situacao, " \
                      f"emp_tipo, " \
                      f"emp_nome_formal, " \
                      f"emp_nome_alternativo, " \
                      f"emp_logradouro, " \
                      f"emp_numero, " \
                      f"emp_bairro, " \
                      f"emp_municipio, " \
                      f"emp_estado " \
                      f"FROM sebd_eremp WHERE emp_codigo = " + \
                  str(self.codigo)
            conexao.conn.cursor.execute(sql)
            emp_cursor = conexao.conn.cursor.fetchone()
            self.acao = 0
            self.codigo = int(emp_cursor[0])
            self.situacao = int(emp_cursor[1])
            self.tipo = str(emp_cursor[2])
            self.nome_formal = str(emp_cursor[3])
            self.nome_alternativo = str(emp_cursor[4])
            self.logradouro = str(emp_cursor[5])
            self.numero = str(emp_cursor[6])
            self.bairro = str(emp_cursor[7])
            self.municipio = str(emp_cursor[8])
            self.estado = str(emp_cursor[9])
            sql = f"SELECT * FROM sebd_ersoc WHERE esc_empresa = " + str(self.codigo)
            conexao.conn.cursor.execute(sql)
            soc_cursor = conexao.conn.cursor.fetchall()
            if len(soc_cursor) > 0:
                for i in soc_cursor:
                    socio = DERSOC01(empresa=i[0],
                                     codigo=i[1],
                                     situacao=i[2],
                                     nome=i[3],
                                     federal=i[4],
                                     capital=float(i[5]),
                                     quotas=float(i[6]),
                                     val_quotas=float(i[7]))
                    self.lsocios.append(socio)
                    self.tot_capital += socio.capital
                    self.tot_quotas += socio.quotas
            self.val_quotas = self.tot_capital / self.tot_quotas
        except:
            pass
        finally:
            conexao.conn.off_cursor()

    def ac_gravar(self, acao):
        self.acao = acao
        try:
            if self.acao == 1:
                sql = "INSERT INTO sebd_eremp (" \
                      "emp_situacao, " \
                      "emp_tipo, " \
                      "emp_nome_formal, " \
                      "emp_nome_alternativo, " \
                      "emp_logradouro, " \
                      "emp_numero, " \
                      "emp_bairro, " \
                      "emp_municipio, " \
                      "emp_estado) " \
                      "VALUES ("
                sql = sql + "'" + str(self.situacao) + "', "
                sql = sql + "'" + str(self.tipo) + "', "
                sql = sql + "'" + str(self.nome_formal) + "', "
                sql = sql + "'" + str(self.nome_alternativo) + "', "
                sql = sql + "'" + str(self.logradouro) + "', "
                sql = sql + "'" + str(self.numero) + "', "
                sql = sql + "'" + str(self.bairro) + "', "
                sql = sql + "'" + str(self.municipio) + "', "
                sql = sql + "'" + str(self.estado) + "') "
            elif self.acao == 2:
                sql = 'UPDATE sebd_eremp SET '
                sql = sql + 'emp_tipo = ' + "'" + str(self.tipo) + "', "
                sql = sql + 'emp_situacao = ' + "'" + str(self.situacao) + "', "
                sql = sql + 'emp_nome_formal = ' + "'" + str(self.nome_formal) + "', "
                sql = sql + 'emp_nome_alternativo = ' + "'" + str(self.nome_alternativo) + "', "
                sql = sql + 'emp_logradouro = ' + "'" + str(self.logradouro) + "', "
                sql = sql + 'emp_numero = ' + "'" + str(self.numero) + "', "
                sql = sql + 'emp_bairro = ' + "'" + str(self.bairro) + "', "
                sql = sql + 'emp_municipio = ' + "'" + str(self.municipio) + "', "
                sql = sql + 'emp_estado = ' + "'" + str(self.estado) + "' "
                sql = sql + 'WHERE ' + str(self.codigo)
            conexao.conn.on_cursor()
            conexao.conn.cursor.execute(sql)
            if self.acao == 1:
                self.codigo = conexao.conn.retorna_id()
            if len(self.lsocios) > 0:
                for socio in self.lsocios:
                    socio.ac_gravar()
            conexao.conn.commit()
        except:
            pass
        finally:
            conexao.conn.off_cursor()


class DERSOC01:
    global conn

    def __init__(self,
                 empresa,
                 codigo=0,
                 situacao=1,
                 nome='',
                 federal='',
                 capital=0.00,
                 quotas=0.00,
                 val_quotas=0.00,
                 acao=0):
        self.empresa = int(empresa)
        self.codigo = int(codigo)
        self.situacao = int(situacao)
        self.nome = str(nome)
        self.federal = str(federal)
        self.capital = float(capital)
        self.quotas = float(quotas)
        self.val_quotas = float(val_quotas)
        self.acao = acao

    def ac_gravar(self):
        try:
            if self.acao == 1:
                sql = "INSERT INTO sebd_ersoc (" \
                      "esc_empresa, " \
                      "esc_codigo, " \
                      "esc_situacao, " \
                      "esc_nome, " \
                      "esc_federal, " \
                      "esc_capital, " \
                      "esc_quotas, " \
                      "esc_val_quot) " \
                      "VALUES ("
                sql = sql + "'" + str(self.empresa) + "', "
                sql = sql + "'" + str(self.codigo) + "', "
                sql = sql + "'" + str(self.situacao) + "', "
                sql = sql + "'" + str(self.nome) + "', "
                sql = sql + "'" + str(self.federal) + "', "
                sql = sql + "'" + str(self.capital) + "', "
                sql = sql + "'" + str(self.quotas) + "', "
                sql = sql + "'" + str(self.val_quotas) + "') "
            elif self.acao == 2:
                sql = 'UPDATE sebd_ersoc SET '
                sql = sql + 'esc_situacao = ' + "'" + str(self.situacao) + "', "
                sql = sql + 'esc_nome = ' + "'" + str(self.nome) + "', "
                sql = sql + 'esc_federal = ' + "'" + str(self.federal) + "', "
                sql = sql + 'esc_capital = ' + "'" + str(self.capital) + "', "
                sql = sql + 'esc_quotas = ' + "'" + str(self.quotas) + "', "
                sql = sql + 'esc_val_quot = ' + "'" + str(self.val_quotas) + "' "
                sql = sql + 'WHERE esc_empresa = ' + str(self.empresa) + " AND "
                sql = sql + 'esc_codigo = ' + str(self.codigo)
            conexao.conn.cursor.execute(sql)
        except:
            pass
        finally:
            pass
