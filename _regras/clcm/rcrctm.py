# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.parser import parse
import win32com.client as win32
import os.path as path
import _regras.sys.ssglob as ssglob
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
        self.litens = []
        self.empresa = ssglob.SSGLOB.empresa
        self.contrato = str(contrato)
        if acao == 2:
            self.operacao = str(operacao).upper()
            self.unidade = int(unidade)
            self.pessoa = int(pessoa)
            self.vigencia = int(vigencia)
            self.tp_vigencia = int(tp_vigencia)
            self.situacao = int(situacao)
            self.dt_emissao = dt_emissao.strftime('%Y-%m-%d')
            self.dt_inicio = dt_inicio.strftime('%Y-%m-%d')
            self.dt_termino = dt_termino.strftime('%Y-%m-%d')

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
                               item.dia_vcto,
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
        gravar = DCRCTM(acao=self.acao,
                        empresa=self.empresa,
                        contrato=self.contrato,
                        operacao=self.operacao,
                        unidade=self.unidade,
                        pessoa=self.pessoa,
                        vigencia=self.vigencia,
                        tp_vigencia=self.tp_vigencia,
                        situacao=self.situacao,
                        dt_emissao=self.dt_emissao,
                        dt_inicio=self.dt_inicio,
                        dt_termino=self.dt_termino,
                        montante=self.fc_total_contrato())
        for item in self.litens:
            it_ctr = DCRITM(empresa=self.empresa,
                            contrato=self.contrato,
                            codigo=item.codigo,
                            situacao=item.situacao,
                            tp_item=item.tp_item,
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
                            dia_vcto=item.dia_vcto,
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
                 dia_vcto=0,
                 conta_banc=0,
                 cartao=0,
                 acao=0):
        self.codigo = int(codigo)
        self.acao = int(acao)
        self.tp_item = int(tp_item)
        self.item = int(item)
        self.situacao = int(situacao)
        self.descricao = str(descricao).upper()
        self.qtde = float(qtde)
        self.val_unit = float(val_unit)
        self.val_total = float(val_total)
        self.moeda = str(moeda).upper()
        self.imobilizado = int(imobilizado)
        self.form_pgto = str(form_pgto).upper()
        self.cond_pgto = str(cond_pgto).upper()
        self.tp_cond_pgto = int(tp_cond_pgto)
        self.dia_vcto = int(dia_vcto)
        self.conta_banc = int(conta_banc)
        self.cartao = int(cartao)


class RCRDOC:

    def __init__(self, modelo):
        self.modelo = modelo
        self.word = win32.gencache.EnsureDispatch('Word.Application')

    def fc_gerar_documento(self, nome_doc, **kwargs):
        try:
            self.nome_doc = nome_doc
            self.word.Documents.Open('C:\\ProjetoContabil\\modelos\\' + self.modelo)
            for key, value in kwargs.items():
                self.word.ActiveDocument.Bookmarks(key).Select()
                self.word.Selection.TypeText(value)
            self.word.ActiveDocument.SaveAs(path.expanduser("~\\Documents\\" + self.nome_doc))
            self.word.Documents.Close()
            return True
        except:
            return False
        finally:
            self.word.Application.Quit(-1)
