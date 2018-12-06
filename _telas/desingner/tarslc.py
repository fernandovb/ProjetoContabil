# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class TARSLC
###########################################################################

class TARSLC(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Lançamento Contábil", pos=wx.DefaultPosition,
                          size=wx.Size(900, 648), style=wx.DEFAULT_FRAME_STYLE | wx.STATIC_BORDER)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.tb_geral = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.tb_geral.Realize()

        lay_body = wx.BoxSizer(wx.VERTICAL)

        lay_options = wx.BoxSizer(wx.VERTICAL)

        lay_body.Add(lay_options, 1, wx.EXPAND, 5)

        lay_slip = wx.BoxSizer(wx.VERTICAL)

        lay_cabecalho = wx.BoxSizer(wx.HORIZONTAL)

        lay_cabec_rotulo_01 = wx.BoxSizer(wx.VERTICAL)

        self.lb_empresa = wx.StaticText(self, wx.ID_ANY, u"Empresa:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_empresa.Wrap(-1)
        lay_cabec_rotulo_01.Add(self.lb_empresa, 0, wx.ALL, 5)

        self.lb_documento = wx.StaticText(self, wx.ID_ANY, u"Número lançamento:", wx.DefaultPosition, wx.Size(150, 26),
                                          wx.ALIGN_RIGHT)
        self.lb_documento.Wrap(-1)
        lay_cabec_rotulo_01.Add(self.lb_documento, 0, wx.ALL, 5)

        self.lb_dt_criacao = wx.StaticText(self, wx.ID_ANY, u"Criado em:", wx.DefaultPosition, wx.Size(150, 26),
                                           wx.ALIGN_RIGHT)
        self.lb_dt_criacao.Wrap(-1)
        lay_cabec_rotulo_01.Add(self.lb_dt_criacao, 0, wx.ALL, 5)

        self.lb_dt_movimento = wx.StaticText(self, wx.ID_ANY, u"Data do movimento:", wx.DefaultPosition,
                                             wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_dt_movimento.Wrap(-1)
        lay_cabec_rotulo_01.Add(self.lb_dt_movimento, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_rotulo_01, 0, wx.EXPAND, 5)

        lay_cabec_campos_01 = wx.BoxSizer(wx.VERTICAL)

        self.tc_empresa = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26), 0)
        lay_cabec_campos_01.Add(self.tc_empresa, 0, wx.ALL, 5)

        self.tc_num_documento = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 26), 0)
        lay_cabec_campos_01.Add(self.tc_num_documento, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_campos_01, 1, wx.EXPAND, 5)

        lay_cabec_rotulo_02 = wx.BoxSizer(wx.VERTICAL)

        self.lb_periodo = wx.StaticText(self, wx.ID_ANY, u"Período:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_periodo.Wrap(-1)
        lay_cabec_rotulo_02.Add(self.lb_periodo, 0, wx.ALL, 5)

        self.lb_exercicio = wx.StaticText(self, wx.ID_ANY, u"Exercício:", wx.DefaultPosition, wx.Size(150, 26),
                                          wx.ALIGN_RIGHT)
        self.lb_exercicio.Wrap(-1)
        lay_cabec_rotulo_02.Add(self.lb_exercicio, 0, wx.ALL, 5)

        self.lb_usuario = wx.StaticText(self, wx.ID_ANY, u"Criado por:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_usuario.Wrap(-1)
        lay_cabec_rotulo_02.Add(self.lb_usuario, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_rotulo_02, 0, wx.EXPAND, 5)

        lay_cabec_campos_02 = wx.BoxSizer(wx.VERTICAL)

        self.tc_periodo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26), 0)
        self.tc_periodo.Enable(False)

        lay_cabec_campos_02.Add(self.tc_periodo, 0, wx.ALL, 5)

        self.tc_exercicio = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 26), 0)
        lay_cabec_campos_02.Add(self.tc_exercicio, 0, wx.ALL, 5)

        self.tc_usuario = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 26), 0)
        lay_cabec_campos_02.Add(self.tc_usuario, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_campos_02, 1, wx.EXPAND, 5)

        lay_slip.Add(lay_cabecalho, 0, wx.EXPAND, 5)

        lay_detalhes = wx.BoxSizer(wx.VERTICAL)

        self.pn_partidas = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.pn_partidas.Enable(False)

        lay_partidas = wx.BoxSizer(wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self.pn_partidas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(5, 5)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        lay_partidas.Add(self.m_grid3, 0, wx.EXPAND, 5)

        self.pn_partidas.SetSizer(lay_partidas)
        self.pn_partidas.Layout()
        lay_partidas.Fit(self.pn_partidas)
        lay_detalhes.Add(self.pn_partidas, 1, wx.EXPAND | wx.ALL, 5)

        self.pn_detalhes = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.pn_detalhes.Enable(False)
        self.pn_detalhes.Hide()

        lay_detalhes1 = wx.BoxSizer(wx.HORIZONTAL)

        lay_detal_rotulos_01 = wx.BoxSizer(wx.VERTICAL)

        self.lb_empresa1 = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Empresa:", wx.DefaultPosition, wx.Size(150, 26),
                                         wx.ALIGN_RIGHT)
        self.lb_empresa1.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_empresa1, 0, wx.ALL, 5)

        self.lb_num_documento = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Número lançamento:", wx.DefaultPosition,
                                              wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_num_documento.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_num_documento, 0, wx.ALL, 5)

        self.lb_registro = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Registro:", wx.DefaultPosition,
                                         wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_registro.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_registro, 0, wx.ALL, 5)

        self.lb_situacao = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Situação:", wx.DefaultPosition,
                                         wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_situacao.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_situacao, 0, wx.ALL, 5)

        self.lb_tipo_registro = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Tipo de registro:", wx.DefaultPosition,
                                              wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_tipo_registro.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_tipo_registro, 0, wx.ALL, 5)

        self.lb_unidade = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Unidade:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_unidade.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_unidade, 0, wx.ALL, 5)

        self.lb_chave_registro = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Chave de registro:", wx.DefaultPosition,
                                               wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_chave_registro.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_chave_registro, 0, wx.ALL, 5)

        self.lb_conta_contabil = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Conta contábil:", wx.DefaultPosition,
                                               wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_conta_contabil.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_conta_contabil, 0, wx.ALL, 5)

        self.lb_centro_lucro = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Centro de lucro:", wx.DefaultPosition,
                                             wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_centro_lucro.Wrap(-1)
        lay_detal_rotulos_01.Add(self.lb_centro_lucro, 0, wx.ALL, 5)

        lay_detalhes1.Add(lay_detal_rotulos_01, 0, wx.EXPAND, 5)

        lay_detal_campos_01 = wx.BoxSizer(wx.VERTICAL)

        self.tc_empresa1 = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                       0)
        lay_detal_campos_01.Add(self.tc_empresa1, 0, wx.ALL, 5)

        self.tc_num_documento1 = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(150, 26), 0)
        lay_detal_campos_01.Add(self.tc_num_documento1, 0, wx.ALL, 5)

        self.tc_registro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(150, 26), 0)
        lay_detal_campos_01.Add(self.tc_registro, 0, wx.ALL, 5)

        self.tc_situacao = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(35, 26),
                                       0)
        lay_detal_campos_01.Add(self.tc_situacao, 0, wx.ALL, 5)

        self.tc_tipo_registro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, 26), 0)
        lay_detal_campos_01.Add(self.tc_tipo_registro, 0, wx.ALL, 5)

        self.tc_unidade = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                      0)
        lay_detal_campos_01.Add(self.tc_unidade, 0, wx.ALL, 5)

        self.tc_chave_registro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, u"40", wx.DefaultPosition, wx.Size(35, 26), 0)
        lay_detal_campos_01.Add(self.tc_chave_registro, 0, wx.ALL, 5)

        self.tc_conta_contabil = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(100, 26), 0)
        lay_detal_campos_01.Add(self.tc_conta_contabil, 0, wx.ALL, 5)

        self.tc_centro_lucro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(100, 26), 0)
        lay_detal_campos_01.Add(self.tc_centro_lucro, 0, wx.ALL, 5)

        lay_detalhes1.Add(lay_detal_campos_01, 1, wx.EXPAND, 5)

        lay_detal_rotulos_02 = wx.BoxSizer(wx.VERTICAL)

        self.lb_descricao = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Descrição:", wx.DefaultPosition,
                                          wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_descricao.Wrap(-1)
        lay_detal_rotulos_02.Add(self.lb_descricao, 0, wx.ALL, 5)

        self.lb_doc_referencia = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Doc. referência:", wx.DefaultPosition,
                                               wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_doc_referencia.Wrap(-1)
        lay_detal_rotulos_02.Add(self.lb_doc_referencia, 0, wx.ALL, 5)

        self.lb_doc_compensacao = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Doc. compensação:", wx.DefaultPosition,
                                                wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_doc_compensacao.Wrap(-1)
        lay_detal_rotulos_02.Add(self.lb_doc_compensacao, 0, wx.ALL, 5)

        self.lb_montante_doc = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Montante:", wx.DefaultPosition,
                                             wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_montante_doc.Wrap(-1)
        lay_detal_rotulos_02.Add(self.lb_montante_doc, 0, wx.ALL, 5)

        self.lb_moeda = wx.StaticText(self.pn_detalhes, wx.ID_ANY, u"Moeda:", wx.DefaultPosition, wx.Size(150, 26),
                                      wx.ALIGN_RIGHT)
        self.lb_moeda.Wrap(-1)
        lay_detal_rotulos_02.Add(self.lb_moeda, 0, wx.ALL, 5)

        lay_detalhes1.Add(lay_detal_rotulos_02, 0, wx.EXPAND, 5)

        lay_detal_campos_02 = wx.BoxSizer(wx.VERTICAL)

        self.tc_descricao = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(300, 26), 0)
        lay_detal_campos_02.Add(self.tc_descricao, 0, wx.ALL, 5)

        self.tc_doc_referencia = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(150, 26), 0)
        lay_detal_campos_02.Add(self.tc_doc_referencia, 0, wx.ALL, 5)

        self.tc_doc_compensacao = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(150, 26), 0)
        lay_detal_campos_02.Add(self.tc_doc_compensacao, 0, wx.ALL, 5)

        self.tc_montante = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(150, 26), 0)
        lay_detal_campos_02.Add(self.tc_montante, 0, wx.ALL, 5)

        self.tc_moeda = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26), 0)
        lay_detal_campos_02.Add(self.tc_moeda, 0, wx.ALL, 5)

        lay_detalhes1.Add(lay_detal_campos_02, 1, wx.EXPAND, 5)

        self.pn_detalhes.SetSizer(lay_detalhes1)
        self.pn_detalhes.Layout()
        lay_detalhes1.Fit(self.pn_detalhes)
        lay_detalhes.Add(self.pn_detalhes, 1, wx.EXPAND | wx.ALL, 5)

        lay_botao = wx.BoxSizer(wx.HORIZONTAL)

        self.bt_adicionar = wx.BitmapButton(self, wx.ID_ANY,
                                            wx.Bitmap(u"icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.bt_adicionar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_adicionar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_adicionar.Enable(False)

        lay_botao.Add(self.bt_adicionar, 0, wx.ALL, 5)

        self.bt_consultar = wx.BitmapButton(self, wx.ID_ANY,
                                            wx.Bitmap(u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.bt_consultar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_cancelar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_consultar.Enable(False)

        lay_botao.Add(self.bt_consultar, 0, wx.ALL, 5)

        self.bt_estonar = wx.Button(self, wx.ID_ANY, u"Estornar", wx.DefaultPosition, wx.DefaultSize, 0)
        lay_botao.Add(self.bt_estonar, 0, wx.ALL, 5)

        lay_detalhes.Add(lay_botao, 0, wx.EXPAND, 5)

        lay_slip.Add(lay_detalhes, 1, wx.BOTTOM | wx.EXPAND, 5)

        lay_body.Add(lay_slip, 1, wx.EXPAND, 5)

        self.SetSizer(lay_body)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, 0, wx.ID_ANY)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
