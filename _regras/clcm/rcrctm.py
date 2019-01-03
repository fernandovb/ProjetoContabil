# -*- coding: utf-8 -*-

import _regras.sys.ssglob as ssglob
from datetime import datetime
from dateutil.parser import parse
from _dados.clcm.dcrctm import DCRCTM, DCRITM


class RCRCTM:

    def __init__(self,
                 acao,
                 contrato='',
                 operacao='',
                 unidade=0,
                 pessoa=0,
                 vigencia=0,
                 tp_vigencia=0,
                 situacao=0,
                 dt_emissao=datetime,
                 dt_inicio=datetime,
                 dt_termino=datetime):
        self.acao = int(acao)
        self.empresa = ssglob.SSGLOB.empresa
        self.contrato = str(contrato)
        self.litens = []
        if acao == 2:
            self.operacao = str(operacao)
            self.unidade = int(unidade)
            self.pessoa = int(pessoa)
            self.vigencia = int(vigencia)
            self.tp_vigencia = int(tp_vigencia)
            self.situacao = int(situacao)
            self.dt_emissao = dt_emissao.strftime('%Y-%m-%d')
            self.dt_inicio = dt_inicio.strftime('%Y-%m-%d')
            self.dt_termino = dt_termino.strftime('%Y-%m-%d')
            self.montante = self.fc_total_contrato()

    def ac_consultar(self):
        try:
            consulta = DCRCTM(acao=self.acao, empresa=self.empresa, contrato=self.contrato)
            if consulta.ac_consultar():
                self.empresa = int(consulta.empresa)
                self.contrato = str(consulta.contrato)
                self.operacao = str(consulta.operacao)
                self.unidade = int(consulta.unidade)
                self.pessoa = int(consulta.pessoa)
                self.vigencia = int(consulta.vigencia)
                self.tp_vigencia = int(consulta.tp_vigencia)
                self.situacao = int(consulta.situacao)
                self.dt_emissao = parse(consulta.dt_emissao)
                self.dt_inicio = parse(consulta.dt_inicio)
                self.dt_termino = parse(consulta.dt_termino)
                self.montante = float(consulta.montante)
                for item in consulta.litens:
                    i = RCRITM(item.codigo,
                               item.tp_item,
                               item.item,
                               item.situacao,
                               item.descricao,
                               item.qtde,
                               item.val_unit,
                               item.val_total,
                               item.moeda,
                               item.imobilizado,
                               item.form_pgto,
                               item.cond_pgto,
                               item.tp_cond_pgto,
                               item.conta_banc,
                               item.cartao,
                               item.acao)
                    self.litens.append(i)
            else:
                raise Exception()
            return True
        except:
            return False

    def ac_gravar(self):
        gravar = DCRCTM(self.acao,
                        self.empresa,
                        self.contrato,
                        self.operacao,
                        self.unidade,
                        self.pessoa,
                        self.vigencia,
                        self.tp_vigencia,
                        self.situacao,
                        self.dt_emissao,
                        self.dt_inicio,
                        self.dt_termino,
                        self.montante)
        for item in self.litens:
            it_ctr = DCRITM(empresa=self.empresa,
                            contrato=self.contrato,
                            codigo=item.codigo,
                            situacao=item.situacao,
                            tp_item=item.tp_servico,
                            item=item.item,
                            descricao=item.descricao,
                            qtde=item.qtde,
                            val_unit=item.val_unit,
                            val_total=item.val_total,
                            moeda=item.moeda,
                            imobilizado=item.imobilizado,
                            form_pgto=item.form_pgto,
                            cond_pgto=item.cond_pgto,
                            tp_cond_pgto=item.tp_cond_pgto,
                            conta_banc=item.conta_banc,
                            cartao=item.cartao,
                            acao=item.acao)
            gravar.litens.append(it_ctr)
        gravar.ac_gravar()
        return gravar.contrato

    def fc_total_contrato(self):
        total = 0.00
        if len(self.litens) > 0:
            for item in self.litens:
                total += item.val_total
        return total


class RCRITM:

    def __init__(self,
                 codigo=0,
                 tp_item=0,
                 item=0,
                 situacao=0,
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
        self.codigo = int(codigo)
        self.acao = int(acao)
        self.tp_item = int(tp_item)
        self.item = int(item)
        self.situacao = int(situacao)
        self.descricao = str(descricao)
        self.qtde = float(qtde)
        self.val_unit = float(val_unit)
        self.val_total = float(val_total)
        self.moeda = str(moeda)
        self.imobilizado = int(imobilizado)
        self.form_pgto = str(form_pgto)
        self.cond_pgto = str(cond_pgto)
        self.tp_cond_pgto = int(tp_cond_pgto)
        self.conta_banc = int(conta_banc)
        self.cartao = int(cartao)
