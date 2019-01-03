# -*- coding: utf-8 -*-
# TELEFONE 99993-0162 / 3325-1413 / 3325-3003 / Antonio de Lima
# robisagro@outlook.com

import wx
import wx.ribbon
from datetime import datetime
from dateutil.parser import parse
import datedelta
from _telas.desingner.tcrctm import TCRCTM
from _telas.sys.ssdate import SSDATE
from _regras.clcm.rcrctm import RCRCTM, RCRITM


class CRCTM(TCRCTM):
    ctr_acao = 0  # 0-Inicial, 1-Consultar, 2-Incluir, 3-Alterar, 4-Excluir
    item_acao = 0
    litens = []
    situacao = {'Ativo': 1, 'Análise': 2, 'Bloqueado': 3, 'Saneamento': 4, 'Encerrado': 5, 'Cancelado': 9}

    def __init__(self, *args, **kwargs):
        super(CRCTM, self).__init__(*args, **kwargs)
        self.fc_ctr_ativa_botoes()
        self.tc_ctr_contrato.Enable(True)

    ### Ações do contrato (RibbonBar) ###

    def ac_ctr_consultar(self, event):
        try:
            self.ctr_acao = 1
            self.sb_contrato.SetStatusText('', 0)
            consulta = RCRCTM(self.ctr_acao, self.tc_ctr_contrato.Value)
            if consulta.ac_consultar():
                self.sb_contrato.SetStatusText('', 0)
                self.tc_ctr_contrato.Value = str(consulta.contrato)
                self.tc_ctr_operacao.Value = str(consulta.operacao)
                self.tc_ctr_unidade.Value = str(consulta.unidade)
                self.tc_ctr_pessoa.Value = str(consulta.pessoa)
                self.tc_ctr_nome_pessoa.Value = ''
                self.tc_ctr_vigencia.Value = str(consulta.vigencia)
                self.cb_ctr_vigencia.Selection = consulta.tp_vigencia - 1
                self.cb_ctr_situacao.Value = loc_sitacao(self.situacao, consulta.situacao)
                self.tc_ctr_dt_emissao.Value = consulta.dt_emissao.strftime('%d/%m/%Y')
                self.tc_ctr_dt_inicio.Value = consulta.dt_inicio.strftime('%d/%m/%Y')
                self.tc_ctr_dt_termino.Value = consulta.dt_termino.strftime('%d/%m/%Y')
                self.tc_ctr_valor.Value = f'{consulta.montante:.2f}'
                self.litens = consulta.litens
                self.fc_atualiza_grade()
            else:
                self.sb_contrato.SetStatusText('Contrato não localizado!', 0)
            self.fc_ctr_ativa_botoes()
            self.fc_item_ativa_botoes()
        except:
            pass

    def ac_ctr_adicionar(self, event):
        self.ctr_acao = 2
        self.fc_ctr_limpa_campos()
        self.fc_ctr_ativa_botoes()
        self.fc_ctr_ativar_campos(True)
        self.fc_item_limpa_campos()
        self.fc_item_ativa_botoes()

    def ac_ctr_editar(self, event):
        self.ctr_acao = 3
        self.sb_contrato.SetStatusText('', 0)
        self.fc_ctr_ativa_botoes()
        pass

    def ac_ctr_excluir(self, event):
        self.ctr_acao = 4
        self.sb_contrato.SetStatusText('', 0)
        pass

    def ac_ctr_confirmar(self, event):
        try:
            self.sb_contrato.SetStatusText('', 0)
            mensagem = ''
            confirma = RCRCTM(self.ctr_acao,
                              contrato='',
                              operacao=self.tc_ctr_operacao.Value,
                              unidade=int(self.tc_ctr_unidade.Value),
                              pessoa=int(self.tc_ctr_pessoa.Value),
                              vigencia=self.tc_ctr_vigencia.Value,
                              tp_vigencia=self.cb_ctr_vigencia.Selection + 1,
                              situacao=self.situacao[self.cb_ctr_situacao.Value],
                              dt_emissao=parse(self.tc_ctr_dt_emissao.Value),
                              dt_inicio=parse(self.tc_ctr_dt_inicio.Value),
                              dt_termino=parse(self.tc_ctr_dt_termino.Value))
            confirma.litens = self.litens
            contrato = str(confirma.ac_gravar())
            self.ctr_acao = 0
            self.fc_ctr_ativa_botoes()
            self.fc_ctr_limpa_campos()
            self.litens.clear()
            self.fc_item_limpa_campos()
            self.fc_item_ativa_botoes()
            self.fc_ctr_ativar_campos(False)
            self.fc_atualiza_grade()
            mensagem = f'Contrato {contrato} salvo com sucesso!'
        except:
            mensagem = 'Erro na criação do contrato. Verifique as informações.'
        finally:
            self.sb_contrato.SetStatusText(mensagem, 0)

    def ac_ctr_cancelar(self, event):
        self.ctr_acao = 0
        self.sb_contrato.SetStatusText('', 0)
        self.fc_ctr_ativa_botoes()
        self.fc_ctr_ativar_campos(False)
        self.fc_item_ativar_campos(False)

    def ac_ctr_gerar_doc(self, event):
        pass

    def ac_ctr_imprimir(self, event):
        pass

    ### Ações internas do contrato ###

    def fc_ctr_limpa_campos(self):
        self.sb_contrato.SetStatusText('', 0)
        self.tc_ctr_contrato.Value = ''
        self.tc_ctr_operacao.Value = ''
        self.tc_ctr_unidade.Value = ''
        self.tc_ctr_pessoa.Value = ''
        self.tc_ctr_nome_pessoa.Value = ''
        self.tc_ctr_vigencia.Value = ''
        self.cb_ctr_vigencia.Selection = 1
        self.cb_ctr_situacao.Selection = 0
        # self.tc_ctr_dt_emissao.Value = ''
        self.tc_ctr_dt_inicio.Value = ''
        self.tc_ctr_dt_termino.Value = ''
        self.tc_ctr_valor.Value = ''

    def fc_ctr_ativar_campos(self, condicao: object = bool) -> object:
        self.tc_ctr_contrato.Enable(not condicao)
        self.tc_ctr_operacao.Enable(condicao)
        # self.bt_ctr_loc_operacao.Enable(condicao)
        self.tc_ctr_unidade.Enable(condicao)
        # self.bt_ctr_unidade.Enable(condicao)
        self.tc_ctr_pessoa.Enable(condicao)
        # self.tc_ctr_nome_pessoa.Enable(True)
        # self.bt_ctr_loc_pessoa.Enable(condicao)
        self.tc_ctr_vigencia.Enable(condicao)
        self.cb_ctr_vigencia.Enable(condicao)
        self.cb_ctr_situacao.Enable(condicao)
        self.tc_ctr_dt_emissao.Value = datetime.today().strftime('%d/%m/%Y')
        self.tc_ctr_dt_inicio.Enable(condicao)
        self.bt_ctr_dt_inicio.Enable(condicao)
        self.tc_ctr_dt_termino.Enable(condicao)
        self.bt_ctr_dt_termino.Enable(condicao)

    def fc_ctr_ativa_botoes(self):
        if self.ctr_acao == 0:
            self.rbb_contrato.EnableButton(wx.ID_FIND, True)
            self.rbb_contrato.EnableButton(wx.ID_NEW, True)
            self.rbb_contrato.EnableButton(wx.ID_EDIT, False)
            self.rbb_contrato.EnableButton(wx.ID_DELETE, False)
            self.rbb_registro.EnableButton(wx.ID_SAVE, False)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, False)
            self.rbb_documento.EnableButton(wx.ID_EXECUTE, False)
            self.rbb_documento.EnableButton(wx.ID_PRINT, False)
            self.tc_ctr_contrato.Enable(True)
        if self.ctr_acao == 1:
            self.rbb_contrato.EnableButton(wx.ID_FIND, True)
            self.rbb_contrato.EnableButton(wx.ID_NEW, True)
            self.rbb_contrato.EnableButton(wx.ID_EDIT, True)
            self.rbb_contrato.EnableButton(wx.ID_DELETE, True)
            self.rbb_registro.EnableButton(wx.ID_SAVE, False)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, False)
            self.rbb_documento.EnableButton(wx.ID_EXECUTE, False)
            self.rbb_documento.EnableButton(wx.ID_PRINT, False)
            self.tc_ctr_contrato.Enable(True)
        if (self.ctr_acao == 2) or (self.ctr_acao == 3):
            self.rbb_contrato.EnableButton(wx.ID_FIND, False)
            self.rbb_contrato.EnableButton(wx.ID_NEW, False)
            self.rbb_contrato.EnableButton(wx.ID_EDIT, False)
            self.rbb_contrato.EnableButton(wx.ID_DELETE, False)
            self.rbb_registro.EnableButton(wx.ID_SAVE, True)
            self.rbb_registro.EnableButton(wx.ID_CANCEL, True)
            self.rbb_documento.EnableButton(wx.ID_EXECUTE, False)
            self.rbb_documento.EnableButton(wx.ID_PRINT, False)
            self.tc_ctr_contrato.Enable(True)

    def fc_ctr_soma_itens(self):
        total = 0.00
        for item in self.litens:
            total += item.val_total
        return total

    ### Ações do item (lay_grid_botoes) ###

    def ac_item_consultar(self, event):
        self.item_acao = 1
        codigo = int(self.gd_ctr_itens.GetCellValue(self.gd_ctr_itens.GetGridCursorRow(), 0))
        item = None
        for i in self.litens:
            if i.codigo == codigo:
                item = i
                break
        # Página 'Dados Básicos'
        self.tc_item_codigo.Value = str(item.codigo)
        self.cb_item_tipo.Selection = item.tp_item
        self.tc_item_coditem.Value = str(item.item)
        self.tc_item_nome.Value = ''
        self.tc_item_descricao.Value = str(item.descricao)
        self.tc_item_quantidade.Value = f'{item.qtde:.3f}'
        self.tc_item_val_unitario.Value = f'{item.val_unit:.2f}'
        self.tc_item_val_total.Value = f'{item.val_total:.2f}'
        self.tc_item_imobilizado.Value = str(item.imobilizado)
        self.tc_item_imob_nome.Value = ''
        # Página 'Financeiro'
        self.tc_item_form_pgto.Value = str(item.form_pgto)
        self.tc_item_cond_pgto.Value = str(item.cond_pgto)
        self.cb_item_tipo_cpgto.Selection = int(item.tp_cond_pgto)
        self.tc_item_conta_bancaria.Value = str(item.conta_banc)
        self.tc_item_cartao.Value = str(item.cartao)
        self.fc_item_ativa_botoes()

    def ac_item_adicionar(self, event):
        self.item_acao = 2
        self.fc_item_ativa_botoes()
        self.fc_item_ativar_campos(True)

    def ac_item_editar(self, event):
        self.item_acao = 3
        self.fc_item_ativa_botoes()
        self.fc_item_ativar_campos(True)

    def ac_item_excluir(self, event):
        pass

    def ac_item_confirmar(self, event):
        if self.item_acao == 2:
            sequencia = 0
            if len(self.litens) > 0:
                itens = []
                for item in self.litens:
                    itens.append(item.codigo)
                sequencia = max(itens)
            item = RCRITM(codigo=sequencia + 1,
                          tp_item=self.cb_item_tipo.GetSelection(),
                          item=int(self.tc_item_coditem.Value),
                          situacao=1,
                          descricao=self.tc_item_descricao.Value,
                          qtde=float(self.tc_item_quantidade.Value),
                          val_unit=float(self.tc_item_val_unitario.Value),
                          val_total=float(self.tc_item_val_total.Value),
                          moeda=self.tc_item_moeda.Value,
                          imobilizado=int(self.tc_item_imobilizado.Value),
                          form_pgto=self.tc_item_form_pgto.Value,
                          cond_pgto=self.tc_item_cond_pgto.Value,
                          tp_cond_pgto=int(self.cb_item_tipo_cpgto.GetSelection()),
                          conta_banc=int(self.tc_item_conta_bancaria.Value),
                          cartao=int(self.tc_item_cartao.Value),
                          acao=self.item_acao)
            self.litens.append(item)
        elif self.item_acao == 3:
            for item in self.litens:
                if item.codigo == int(self.tc_item_codigo.Value):
                    item.tp_servico = self.cb_item_tipo.GetSelection()
                    item.item = int(self.tc_item_coditem.Value)
                    item.descricao = str(self.tc_item_descricao.Value)
                    item.qtde = float(self.tc_item_quantidade.Value)
                    item.val_unit = float(self.tc_item_val_unitario.Value)
                    item.val_total = float(self.tc_item_val_total.Value)
                    item.imobilizado = int(self.tc_item_imobilizado.Value)
                    item.form_pgto = str(self.tc_item_form_pgto.Value)
                    item.cond_pgto = str(self.tc_item_cond_pgto.Value)
                    item.tp_cond_pgto = self.cb_item_tipo_cpgto.GetSelection()
                    item.conta_banc = int(self.tc_item_conta_bancaria.Value)
                    item.cartao = int(self.tc_item_cartao.Value)
                    break
        self.tc_ctr_valor.Value = f'{self.fc_ctr_soma_itens():.2f}'
        self.fc_atualiza_grade()
        self.fc_item_limpa_campos()
        self.fc_item_ativar_campos(False)
        self.item_acao = 0
        self.fc_item_ativa_botoes()

    def ac_item_cancelar(self, event):
        self.item_acao = 0
        self.fc_item_ativa_botoes()
        self.fc_item_limpa_campos()
        self.fc_item_ativar_campos(False)

    ### Ações internas dos itens

    def off_focus_qtde(self, event):
        try:
            if self.tc_item_val_unitario == '':
                self.tc_item_val_unitario = '0.00'
            if self.tc_item_quantidade == '':
                self.tc_item_quantidade = '0.000'
            val_unit = float(self.tc_item_val_unitario.Value)
            qtde = float(self.tc_item_quantidade.Value)
            if (qtde != 0) and (val_unit != 0):
                val_total = val_unit * qtde
                self.tc_item_val_total.Value = f'{val_total:.2f}'
        except:
            pass
        event.Skip()

    def on_focus_qtde(self, event):
        event.Skip()

    def off_focus_vunit(self, event):
        if self.tc_item_val_unitario == '':
            self.tc_item_val_unitario = '0.00'
        if self.tc_item_quantidade == '':
            self.tc_item_quantidade = '0.000'
        val_unit = float(self.tc_item_val_unitario.Value)
        qtde = float(self.tc_item_quantidade.Value)
        if (qtde != 0) and (val_unit != 0):
            val_total = val_unit * qtde
            self.tc_item_val_total.Value = f'{val_total:.2f}'
        event.Skip()

    def on_focus_vunit(self, event):
        event.Skip()

    def off_focus_vtotal(self, event):
        val_total = float(self.tc_item_val_total.Value)
        qtde = float(self.tc_item_quantidade.Value)
        if (qtde != 0) and (val_total != 0):
            val_unit = val_total / qtde
            self.tc_item_val_unitario.Value = f'{val_unit:.2f}'
        event.Skip()

    def on_focus_vtotal(self, event):
        event.Skip()

    def fc_item_limpa_campos(self):
        # Página 'Dados Básicos'
        self.cb_item_tipo.Selection = 0
        self.tc_item_coditem.Value = ''
        self.tc_item_nome.Value = ''
        self.tc_item_descricao.Value = ''
        self.tc_item_quantidade.Value = '0.000'
        self.tc_item_val_unitario.Value = '0.00'
        self.tc_item_val_total.Value = '0.00'
        self.tc_item_imobilizado.Value = ''
        self.tc_item_imob_nome.Value = ''
        # Página 'Financeiro'
        self.tc_item_form_pgto.Value = ''
        self.tc_item_cond_pgto.Value = ''
        self.cb_item_tipo_cpgto.Selection = 0
        self.tc_item_conta_bancaria.Value = ''
        self.tc_item_cartao.Value = ''

    def fc_item_ativar_campos(self, condicao: object = bool) -> object:
        # Página 'Dados Básicos'
        self.cb_item_tipo.Enable(condicao)
        self.tc_item_coditem.Enable(condicao)
        # self.bt_item_loc_codigo.Enable(condicao)
        self.tc_item_descricao.Enable(condicao)
        self.tc_item_quantidade.Enable(condicao)
        self.tc_item_val_unitario.Enable(condicao)
        self.tc_item_val_total.Enable(condicao)
        self.tc_item_moeda.Enable(condicao)
        self.tc_item_imobilizado.Enable(condicao)
        # self.bt_item_loc_imob.Enable(condicao)
        # Página 'Financeiro'
        self.tc_item_form_pgto.Enable(condicao)
        # self.bt_item_loc_form_pgto.Enable(condicao)
        self.tc_item_cond_pgto.Enable(condicao)
        # self.bt_item_loc_cond_pgto.Enable(condicao)
        self.cb_item_tipo_cpgto.Enable(condicao)
        self.tc_item_conta_bancaria.Enable(condicao)
        # self.bt_item_loc_conta_banc.Enable(condicao)
        self.tc_item_cartao.Enable(condicao)
        # self.bt_item_loc_cartao.Enable(condicao)

    def fc_item_ativa_botoes(self):
        if self.item_acao == 0:
            if self.gd_ctr_itens.GetNumberRows() > 0:
                self.bt_item_consultar.Enable(True)
            else:
                self.bt_item_consultar.Enable(False)
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

    def fc_atualiza_grade(self):
        for i in range(self.gd_ctr_itens.GetNumberRows()):
            self.gd_ctr_itens.DeleteRows()
        if len(self.litens) > 0:
            linha = 0
            for item in self.litens:
                self.gd_ctr_itens.AppendRows(1)
                self.gd_ctr_itens.SetCellValue(linha, 0, str(item.codigo))
                self.gd_ctr_itens.SetCellValue(linha, 1, str(item.item))
                self.gd_ctr_itens.SetCellValue(linha, 3, str(item.descricao))
                self.gd_ctr_itens.SetCellValue(linha, 4, f'{item.qtde:.3f}')
                self.gd_ctr_itens.SetCellValue(linha, 5, f'{item.val_unit:.2f}')
                self.gd_ctr_itens.SetCellValue(linha, 6, f'{item.val_total:.2f}')
                linha += 1

    ### Ações de botoes de localização e consultas ###

    def ac_loc_operacao(self, event):
        pass

    def ac_loc_pessoa(self, event):
        pass

    def ac_dt_inicio(self, event):
        self.tc_ctr_dt_inicio.Value = self.fc_dialog_data()

    def ac_dt_termino(self, event):
        self.tc_ctr_dt_termino.Value = self.fc_dialog_data()

    def ac_ctr_tp_vigencia(self, event):
        if self.tc_ctr_dt_inicio.Value == '':
            self.tc_ctr_dt_inicio.Value = datetime.today().strftime('%d/%m/%Y')
        data = parse(self.tc_ctr_dt_inicio.Value)
        if self.cb_ctr_vigencia.Selection == 0:
            data = data + datedelta.datedelta(days=int(self.tc_ctr_vigencia.Value))
        if self.cb_ctr_vigencia.Selection == 1:
            data = data + datedelta.datedelta(months=int(self.tc_ctr_vigencia.Value))
        if self.cb_ctr_vigencia.Selection == 2:
            data = data + datedelta.datedelta(years=int(self.tc_ctr_vigencia.Value))
        self.tc_ctr_dt_termino.Value = data.strftime('%d/%m/%Y')

    def off_focus_vigencia(self, event):
        if self.tc_ctr_dt_inicio.Value == '':
            self.tc_ctr_dt_inicio.Value = datetime.today().strftime('%d/%m/%Y')
        data = parse(self.tc_ctr_dt_inicio.Value)
        if self.cb_ctr_vigencia.Selection == 0:
            data = data + datedelta.datedelta(days=int(self.tc_ctr_vigencia.Value))
        if self.cb_ctr_vigencia.Selection == 1:
            data = data + datedelta.datedelta(months=int(self.tc_ctr_vigencia.Value))
        if self.cb_ctr_vigencia.Selection == 2:
            data = data + datedelta.datedelta(years=int(self.tc_ctr_vigencia.Value))
        self.tc_ctr_dt_termino.Value = data.strftime('%d/%m/%Y')
        event.Skip()

    def on_focus_vigencia(self, event):
        event.Skip()
        pass

    def ac_loc_item(self, event):
        pass

    def ac_loc_imobilizado(self, event):
        pass

    def ac_loc_form_pgto(self, event):
        pass

    def ac_loc_cond_pgto(self, event):
        pass

    def ac_loc_conta_bancaria(self, event):
        pass

    def ac_loc_cartao(self, event):
        pass

    # Métodos próprios

    def fc_dialog_data(self):
        data = ''
        consulta = SSDATE(self)
        if consulta.ShowModal() == wx.ID_OK:
            data = str(consulta.date)
        consulta.Destroy()
        return data

    def fc_datatostr(self):
        pass


def loc_sitacao(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i
