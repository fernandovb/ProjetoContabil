# -*- coding: utf-8 -*-

import wx
import wx.ribbon
from datetime import datetime
from dateutil.parser import parse
import datedelta
from _telas.desingner.tirfat import TIRFAT
from _telas.sys.ssdate import SSDATE
from _telas.sebd.efopr import EFOPR
from _telas.prm.pfpes import PFPES
from _telas.accl.afcon import AFCON


class IRFAT(TIRFAT):
    ent_acao = 0  # 0-Inicial, 1-Consultar, 2-Incluir, 3-Alterar, 4-Excluir
    item_acao = 0
    litens = []
    situacao = {'Ativo': 1, 'Análise': 2, 'Bloqueado': 3, 'Saneamento': 4, 'Encerrado': 5, 'Cancelado': 9}
    tp_cond_pgto = {0: 'vincendo', 1: 'vencido'}

    def __init__(self, *args, **kwargs):
        super(IRFAT, self).__init__(*args, **kwargs)
        self.fc_ent_ativa_botoes()
        self.fc_ent_ativar_campos(False)
        self.fc_item_ativa_botoes()
        self.fc_item_ativar_campos(False)

    ### Ações do documento (RibbonBar) ###

    def ac_ent_consultar(self, event):
        pass

    def ac_ent_adicionar(self, event):
        self.ent_acao = 2
        self.fc_ent_limpa_campos()
        self.fc_ent_ativa_botoes()
        self.fc_ent_ativar_campos(True)
        self.fc_item_limpa_campos()
        self.fc_item_ativa_botoes()

    def ac_ent_editar(self, event):
        pass

    def ac_ent_excluir(self, event):
        pass

    def ac_ent_confirmar(self, event):
        pass

    def ac_ent_cancelar(self, event):
        self.ent_acao = 0
        self.item_acao = 0
        self.sb_entrada.SetStatusText('', 0)
        self.fc_ent_ativa_botoes()
        self.fc_ent_limpa_campos()
        self.fc_ent_ativar_campos(False)
        self.fc_item_ativa_botoes()
        self.fc_item_limpa_campos()
        self.fc_item_ativar_campos(False)

    def ac_ent_contabilidade(self, event):
        pass

    def ac_ent_dt_fatura(self, event):
        self.tc_ent_dt_fatura.Value = self.fc_dialog_data()

    def ac_ent_dt_lancamento(self, event):
        self.tc_ent_dt_lancamento.Value = self.fc_dialog_data()

    def ac_ent_dt_vencimento(self, event):
        self.tc_ent_vencimento.Value = self.fc_dialog_data()

    def ac_ent_busca_cpgto(self, event):
        pass

    def ac_ent_busca_fpgto(self, event):
        pass

    def ac_ent_busca_operacao(self, event):
        consulta = EFOPR(self)
        if consulta.ShowModal() == wx.ID_OK:
            self.tc_ent_operacao.Value = str(
                consulta.gd_resultado.GetCellValue(consulta.gd_resultado.GetGridCursorRow(), 0))
        consulta.Destroy()

    def ac_ent_busca_pessoa(self, event):
        consulta = PFPES(self)
        if consulta.ShowModal() == wx.ID_OK:
            self.tc_ent_pessoa.Value = str(
                consulta.gd_resultado.GetCellValue(consulta.gd_resultado.GetGridCursorRow(), 0))
            self.tc_ent_nome_pessoa.Value = str(
                consulta.gd_resultado.GetCellValue(consulta.gd_resultado.GetGridCursorRow(), 1))
        consulta.Destroy()

    ### Ações internas do documento ###

    def fc_ent_limpa_campos(self):
        self.tc_ent_documento.Value = ''
        self.tc_ent_dt_fatura.Value = ''
        self.tc_ent_dt_lancamento.Value = ''
        self.tc_ent_montante.Value = '0.00'
        self.tc_ent_moeda.Value = 'BRL'
        self.tc_ent_operacao.Value = ''
        self.cb_ent_tp_documento.Selection = 0
        self.tc_ent_referencia.Value = ''
        self.tc_ent_pessoa.Value = ''
        self.tc_ent_nome_pessoa.Value = ''
        self.tc_ent_vencimento.Value = ''
        self.tc_ent_form_pgto.Value = ''
        self.tc_ent_condicao.Value = ''

    def fc_ent_ativar_campos(self, condicao: object = bool) -> object:
        self.tc_ent_documento.Enable(not condicao)
        self.tc_ent_dt_fatura.Enable(condicao)
        self.bt_ent_dt_fatura.Enable(condicao)
        self.tc_ent_dt_lancamento.Enable(condicao)
        self.bt_ent_dt_lancamento.Enable(condicao)
        self.tc_ent_montante.Enable(condicao)
        self.tc_ent_moeda.Enable(condicao)
        self.tc_ent_operacao.Enable(condicao)
        self.bt_ent_operacao.Enable(condicao)
        self.cb_ent_tp_documento.Enable(condicao)
        self.tc_ent_referencia.Enable(condicao)
        self.tc_ent_pessoa.Enable(condicao)
        self.bt_ent_pessoa.Enable(condicao)
        self.tc_ent_form_pgto.Enable(condicao)
        self.bt_ent_form_pgto.Enable(condicao)
        self.tc_ent_condicao.Enable(condicao)
        self.bt_ent_condicao.Enable(condicao)
        self.tc_ent_vencimento.Enable(condicao)
        self.bt_ent_vencimento.Enable(condicao)

    def fc_ent_ativa_botoes(self):
        if self.ent_acao == 0:
            self.rbb_entrada.EnableButton(wx.ID_FIND, True)
            self.rbb_entrada.EnableButton(wx.ID_NEW, True)
            self.rbb_entrada.EnableButton(wx.ID_EDIT, False)
            self.rbb_entrada.EnableButton(wx.ID_DELETE, False)
            self.rbb_registro.EnableButton(wx.ID_SAVE, False)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, False)
            self.rbb_contabilidade.EnableButton(wx.ID_EXECUTE, False)
        if self.ent_acao == 1:
            self.rbb_entrada.EnableButton(wx.ID_FIND, True)
            self.rbb_entrada.EnableButton(wx.ID_NEW, True)
            self.rbb_entrada.EnableButton(wx.ID_EDIT, True)
            self.rbb_entrada.EnableButton(wx.ID_DELETE, False)
            self.rbb_registro.EnableButton(wx.ID_SAVE, False)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, False)
            self.rbb_contabilidade.EnableButton(wx.ID_EXECUTE, True)
        if (self.ent_acao == 2) or (self.ent_acao == 3):
            self.rbb_entrada.EnableButton(wx.ID_FIND, False)
            self.rbb_entrada.EnableButton(wx.ID_NEW, False)
            self.rbb_entrada.EnableButton(wx.ID_EDIT, False)
            self.rbb_entrada.EnableButton(wx.ID_DELETE, False)
            self.rbb_registro.EnableButton(wx.ID_SAVE, True)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, True)
            self.rbb_contabilidade.EnableButton(wx.ID_EXECUTE, False)

    def fc_ent_soma_itens(self):
        pass

    ### Ações do item (lay_grid_botoes) ###

    def ac_item_consultar(self, event):
        pass

    def ac_item_adicionar(self, event):
        self.item_acao = 2
        self.fc_item_ativa_botoes()
        self.fc_item_ativar_campos(True)

    def ac_item_editar(self, event):
        pass

    def ac_item_excluir(self, event):
        pass

    def ac_item_confirmar(self, event):
        pass

    def ac_item_cancelar(self, event):
        self.item_acao = 0
        self.fc_item_ativa_botoes()
        self.fc_item_limpa_campos()
        self.fc_item_ativar_campos(False)

    def ac_item_busca_item(self, event):
        pass

    def ac_item_busca_conta(self, event):
        consulta = AFCON(self)
        if consulta.ShowModal() == wx.ID_OK:
            self.tc_item_conta.Value = str(
                consulta.gd_resultado.GetCellValue(consulta.gd_resultado.GetGridCursorRow(), 0))
        consulta.Destroy()

    def ac_item_busca_ccusto(self, event):
        pass

    def ac_item_busca_clucro(self, event):
        pass

    ### Ações internas do item ###

    def fc_item_limpa_campos(self):
        self.tc_item_sequencia.Value = ''
        self.cb_item_tipo.Selection = 0
        self.tc_item_item.Value = ''
        self.tc_item_descricao.Value = ''
        self.tc_item_qtde.Value = '0.000'
        self.tc_item_val_unitario.Value = '0.00'
        self.tc_item_montante.Value = '0.00'
        self.tc_item_conta.Value = ''
        self.tc_item_centro_custo.Value = ''
        self.tc_item_centro_lucro.Value = ''

    def fc_item_ativa_botoes(self):
        if self.item_acao == 0:
            if self.gd_ent_itens.GetNumberRows() > 0:
                self.bt_item_consultar.Enable(True)
            else:
                self.bt_item_consultar.Enable(False)
            if self.ent_acao == 0:
                self.bt_item_adicionar.Enable(False)
            else:
                self.bt_item_adicionar.Enable(True)
            self.bt_item_editar.Enable(False)
            self.bt_item_excluir.Enable(False)
            self.bt_item_confirmar.Enable(False)
            self.bt_item_cancelar.Enable(False)
        if self.item_acao == 1:
            self.bt_item_consultar.Enable(True)
            self.bt_item_adicionar.Enable(True)
            self.bt_item_editar.Enable(True)
            self.bt_item_excluir.Enable(True)
            self.bt_item_confirmar.Enable(False)
            self.bt_item_cancelar.Enable(False)
        if (self.item_acao == 2) or (self.item_acao == 3):
            self.bt_item_consultar.Enable(False)
            self.bt_item_adicionar.Enable(False)
            self.bt_item_editar.Enable(False)
            self.bt_item_excluir.Enable(False)
            self.bt_item_confirmar.Enable(True)
            self.bt_item_cancelar.Enable(True)

    def fc_item_ativar_campos(self, condicao: object = bool) -> object:
        self.tc_item_sequencia.Enable(condicao)
        self.cb_item_tipo.Enable(condicao)
        self.tc_item_item.Enable(condicao)
        self.bt_item_item.Enable(condicao)
        self.tc_item_qtde.Enable(condicao)
        self.tc_item_val_unitario.Enable(condicao)
        self.tc_item_montante.Enable(condicao)
        self.tc_item_conta.Enable(condicao)
        self.bt_item_conta.Enable(condicao)
        self.tc_item_centro_custo.Enable(condicao)
        self.bt_item_centro_custo.Enable(condicao)
        self.tc_item_centro_lucro.Enable(condicao)
        self.bt_item_centro_lucro.Enable(condicao)

    ### Métodos próprios ###

    def fc_dialog_data(self):
        data = ''
        consulta = SSDATE(self)
        if consulta.ShowModal() == wx.ID_OK:
            data = str(consulta.date)
        consulta.Destroy()
        return data


def loc_sitacao(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i
