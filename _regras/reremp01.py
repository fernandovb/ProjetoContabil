# -*- coding: utf-8 -*-

import _dados.deremp01 as deremp01


class REREMP01:

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
        self.situacao = int(situacao)
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
        consulta = deremp01.DEREMP01(self.codigo)
        consulta.ac_consultar()
        self.codigo = consulta.codigo
        self.situacao = consulta.situacao
        self.tipo = consulta.tipo
        self.nome_formal = consulta.nome_formal
        self.nome_alternativo = consulta.nome_alternativo
        self.logradouro = consulta.logradouro
        self.numero = consulta.numero
        self.bairro = consulta.bairro
        self.municipio = consulta.municipio
        self.estado = consulta.estado
        self.tot_capital = consulta.tot_capital
        self.tot_quotas = consulta.tot_quotas
        self.val_quotas = consulta.val_quotas
        if len(consulta.lsocios) > 0:
            for i in consulta.lsocios:
                socio = RERSOC01(empresa=i.empresa,
                                 codigo=i.codigo,
                                 situacao=i.situacao,
                                 nome=i.nome,
                                 federal=i.federal,
                                 capital=i.capital,
                                 quotas=i.quotas,
                                 val_quotas=i.val_quotas,
                                 acao=0)
                self.lsocios.append(socio)

    def ac_gravar(self, acao):
        self.acao = acao
        grava = deremp01.DEREMP01(self.codigo,
                                  self.situacao,
                                  self.tipo,
                                  self.nome_formal,
                                  self.nome_alternativo,
                                  self.logradouro,
                                  self.numero,
                                  self.bairro,
                                  self.municipio,
                                  self.estado)
        grava.lsocios = self.lsocios
        grava.ac_gravar(self.acao)


class RERSOC01:

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

    def ac_consultar(self):
        pass

    def ac_inserir(self):
        pass

    def ac_excluir(self):
        pass

    def ac_gravar(self):
        if self.acao != 0:
            grava = deremp01.DERSOC01(self.empresa,
                                      self.codigo,
                                      self.situacao,
                                      self.nome,
                                      self.federal,
                                      self.capital,
                                      self.quotas,
                                      self.val_quotas,
                                      self.acao)
            grava.ac_gravar()

    def ac_cancelar(self):
        pass
