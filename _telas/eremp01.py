# -*- coding: utf-8 -*-

from _telas.desingner.tela_empresa import FrmEmpresa
from _regras.reremp01 import REREMP01, RERSOC01
import wx


class EREMP01(FrmEmpresa):

    acao = 0  # 0-Consultar, 1-Inlcuir, 2-Alterar
    situacao = {'Ativo': 1, 'Análise': 2, 'Bloqueado': 3, 'Saneamento': 4, 'Cancelado': 9}

    def __init__(self, *args, **kwargs):
        super(EREMP01, self).__init__(*args, **kwargs)
        self.tb_geral.EnableTool(wx.ID_FIND, True)
        self.tb_geral.EnableTool(wx.ID_ADD, True)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, False)
        self.tb_geral.EnableTool(wx.ID_ABORT, False)
        self.c_dados = {'emp_codigo': '',
                        'emp_situacao': '',
                        'emp_tipo': '',
                        'emp_nome_formal': '',
                        'emp_nome_alternativo': '',
                        'emp_logradouro': '',
                        'emp_numero': '',
                        'emp_bairro': '',
                        'emp_municipio': '',
                        'emp_estado': ''}
        self.lsocios = []
        self.gd_socios.SetColLabelValue(0, 'Empresa')
        self.gd_socios.SetColLabelValue(1, 'Codigo')
        self.gd_socios.SetColLabelValue(2, 'Situacao')
        self.gd_socios.SetColLabelValue(3, 'Nome do Sócio')
        self.gd_socios.SetColLabelValue(4, 'Cad.Federal')
        self.gd_socios.SetColLabelValue(5, 'Capital')
        self.gd_socios.SetColLabelValue(6, 'Quotas')
        self.gd_socios.SetColLabelValue(7, 'V.Quotas')

    def ac_sair(self, event):
        self.Close()

    def ac_buscar(self, event):
        self.acao = 0
        try:
            consulta = REREMP01(self.tc_codigo.Value)
            consulta.ac_consultar()
            self.cb_tipo.Value = consulta.tipo
            self.cb_situacao.Value = loc_sitacao(self.situacao, consulta.situacao)
            self.tc_nome_formal.Value = consulta.nome_formal
            self.tc_nome_alternativo.Value = consulta.nome_alternativo
            self.tc_logradouro.Value = consulta.logradouro
            self.tc_numero.Value = consulta.numero
            self.tc_bairro.Value = consulta.bairro
            self.tc_municipio.Value = consulta.municipio
            self.cb_estado.Value = consulta.estado
            self.lsocios = consulta.lsocios
            self.soc_atualiza_grade()
            # Ativa botões para a operação
            self.bt_soc_consultar.Enable(True)
            self.bt_soc_adicionar.Enable(True)
            self.bt_soc_editar.Enable(False)
            self.bt_soc_excluir.Enable(False)
            self.bt_soc_cancelar.Enable(False)
            # Exibe botões
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, True)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
            self.bt_soc_consultar.Enable(True)
        except:
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            wx.MessageBox(f'Erro ao carregar o registro {self.tc_codigo.Value}.',
                          caption='Erro', style=wx.OK | wx.ICON_ERROR)

    def ac_adicionar(self, event):
        self.acao = 1
        self.tb_geral.EnableTool(wx.ID_FIND, False)
        self.tb_geral.EnableTool(wx.ID_ADD, False)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, True)
        self.tb_geral.EnableTool(wx.ID_ABORT, True)
        self.bt_soc_consultar.Enable(False)
        self.bt_soc_adicionar.Enable(True)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_cancelar.Enable(False)
        self.limpa_campos()
        self.on_campos()

    def ac_editar(self, event):
        self.acao = 2
        self.tb_geral.EnableTool(wx.ID_FIND, False)
        self.tb_geral.EnableTool(wx.ID_ADD, False)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, True)
        self.tb_geral.EnableTool(wx.ID_ABORT, True)
        self.bt_soc_adicionar.Enable(True)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_cancelar.Enable(False)
        self.on_campos()

    def ac_confirmar(self, event):
        grava = REREMP01(self.tc_codigo.Value,
                         self.situacao[self.cb_situacao.Value],
                         self.cb_tipo.Value,
                         self.tc_nome_formal.Value,
                         self.tc_nome_alternativo.Value,
                         self.tc_logradouro.Value,
                         self.tc_numero.Value,
                         self.tc_bairro.Value,
                         self.tc_municipio.Value,
                         self.cb_estado.Value)
        grava.lsocios = self.lsocios
        grava.ac_gravar(self.acao)
        self.tb_geral.EnableTool(wx.ID_FIND, True)
        self.tb_geral.EnableTool(wx.ID_ADD, True)
        self.tb_geral.EnableTool(wx.ID_EDIT, True)
        self.tb_geral.EnableTool(wx.ID_APPLY, False)
        self.tb_geral.EnableTool(wx.ID_ABORT, False)
        self.off_campos()

    def ac_cancelar(self, event):
        if self.acao == 1:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
        elif self.acao == 2:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, True)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
        elif self.acao == 0:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
            self.limpa_campos()
        self.acao = 0
        self.off_campos()

    def on_campos(self):
        self.tc_codigo.Enable(False)
        self.cb_tipo.Enable(True)
        self.cb_situacao.Enable(True)
        self.tc_nome_formal.Enable(True)
        self.tc_nome_alternativo.Enable(True)
        self.tc_logradouro.Enable(True)
        self.tc_numero.Enable(True)
        self.tc_bairro.Enable(True)
        self.tc_municipio.Enable(True)
        self.cb_estado.Enable(True)

    def off_campos(self):
        self.tc_codigo.Enable(True)
        self.cb_tipo.Enable(False)
        self.cb_situacao.Enable(False)
        self.tc_nome_formal.Enable(False)
        self.tc_nome_alternativo.Enable(False)
        self.tc_logradouro.Enable(False)
        self.tc_numero.Enable(False)
        self.tc_bairro.Enable(False)
        self.tc_municipio.Enable(False)
        self.cb_estado.Enable(False)

    def limpa_campos(self):
        self.tc_codigo.Value = ''
        self.cb_tipo.Value = ''
        self.cb_situacao.Value = ''
        self.tc_nome_formal.Value = ''
        self.tc_nome_alternativo.Value = ''
        self.tc_logradouro.Value = ''
        self.tc_numero.Value = ''
        self.tc_bairro.Value = ''
        self.tc_municipio.Value = ''
        self.cb_estado.Value = ''

    def soc_consultar(self, event):
        socio = self.lsocios[self.gd_socios.GetGridCursorRow()]
        if socio is not None:
            self.tc_soc_empresa.Value = str(socio.empresa)
            self.tc_soc_codigo.Value = str(socio.codigo)
            self.cb_soc_situacao.Value = loc_sitacao(self.situacao, socio.situacao)
            self.tc_soc_nome.Value = str(socio.nome)
            self.tc_soc_federal.Value = str(socio.federal)
            self.tc_soc_capital.Value = str(socio.capital)
            self.tc_soc_quotas.Value = str(socio.quotas)
            self.tc_soc_vquota.Value = str(socio.val_quotas)
            self.bt_soc_consultar.Enable(False)
            self.bt_soc_adicionar.Enable(True)
            self.bt_soc_editar.Enable(True)
            self.bt_soc_excluir.Enable(True)
            self.bt_soc_confirmar.Enable(False)
            self.bt_soc_cancelar.Enable(True)
            self.m_notebook2.ChangeSelection(1)

    def soc_adicionar(self, event):
        self.bt_soc_consultar.Enable(False)
        self.bt_soc_adicionar.Enable(False)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_confirmar.Enable(True)
        self.bt_soc_cancelar.Enable(True)
        self.soc_on_campos()
        self.soc_limpa_campos()
        self.tc_soc_empresa.Value = self.tc_codigo.Value
        self.tc_soc_empresa.Enable(False)
        self.tc_soc_codigo.Value = str(self.gd_socios.GetNumberRows() + 1)
        self.tc_soc_codigo.Enable(False)
        self.cb_soc_situacao.Value = 'Ativo'
        self.m_notebook2.ChangeSelection(1)

    def soc_editar(self, event):
        self.bt_soc_consultar.Enable(False)
        self.bt_soc_adicionar.Enable(False)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_confirmar.Enable(True)
        self.bt_soc_cancelar.Enable(True)
        self.soc_on_campos()

    def soc_excluir(self, event):
        pass

    def soc_confirmar(self, event):
        pass

    def soc_cancelar(self, event):
        self.bt_soc_consultar.Enable(True)
        self.bt_soc_adicionar.Enable(True)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_confirmar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_cancelar.Enable(False)
        self.soc_off_campos()
        self.m_notebook2.ChangeSelection(0)

    def soc_carregar(self):
        pass

    def soc_atualiza_grade(self):
        for linha in range(self.gd_socios.GetNumberRows()):
            self.gd_socios.DeleteRows()
        if len(self.lsocios) > 0:
            linha = 0
            for socio in self.lsocios:
                self.gd_socios.AppendRows(1)
                self.gd_socios.SetCellValue(linha, 0, str(socio.empresa))
                self.gd_socios.SetCellValue(linha, 1, str(socio.codigo))
                self.gd_socios.SetCellValue(linha, 2, str(socio.situacao))
                self.gd_socios.SetCellValue(linha, 3, str(socio.nome))
                self.gd_socios.SetCellValue(linha, 4, str(socio.federal))
                self.gd_socios.SetCellValue(linha, 5, str(socio.capital))
                self.gd_socios.SetCellValue(linha, 6, str(socio.quotas))
                self.gd_socios.SetCellValue(linha, 7, str(socio.val_quotas))
                linha += 1
            self.soc_total_capital()

    def soc_limpa_campos(self):
        self.tc_soc_empresa.Value = ''
        self.tc_soc_codigo.Value = ''
        self.cb_soc_situacao.Value = ''
        self.tc_soc_nome.Value = ''
        self.tc_soc_federal.Value = ''
        self.tc_soc_capital.Value = ''
        self.tc_soc_quotas.Value = ''
        self.tc_soc_vquota.Value = ''

    def soc_on_campos(self):
        self.tc_soc_empresa.Enable(True)
        self.tc_soc_codigo.Enable(True)
        self.cb_soc_situacao.Enable(True)
        self.tc_soc_nome.Enable(True)
        self.tc_soc_federal.Enable(True)
        self.tc_soc_capital.Enable(True)
        self.tc_soc_quotas.Enable(True)
        self.tc_soc_vquota.Enable(True)

    def soc_off_campos(self):
        self.tc_soc_empresa.Enable(False)
        self.tc_soc_codigo.Enable(False)
        self.cb_soc_situacao.Enable(False)
        self.tc_soc_nome.Enable(False)
        self.tc_soc_federal.Enable(False)
        self.tc_soc_capital.Enable(False)
        self.tc_soc_quotas.Enable(False)
        self.tc_soc_vquota.Enable(False)

    def soc_total_capital(self):
        if len(self.lsocios) > 0:
            tot_capital = 0.00
            tot_quotas = 0.00
            for socio in self.lsocios:
                tot_capital = tot_capital + socio.capital
                tot_quotas = tot_quotas + socio.quotas
            self.tc_capital.Value = str(tot_capital)
            self.tc_quotas.Value = str(tot_capital)


def loc_sitacao(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i
