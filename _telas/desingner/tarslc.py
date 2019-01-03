# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
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
                          size=wx.Size(900, 537), style=wx.DEFAULT_FRAME_STYLE | wx.BORDER_STATIC)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.tb_slip = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.bt_reg_adicionar = self.tb_slip.AddLabelTool(wx.ID_ADD, u"Novo lançamento",
                                                          wx.Bitmap(u"icons/ac_adicionar_16x16.png",
                                                                    wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                          wx.EmptyString, wx.EmptyString, None)

        self.bt_reg_consultar = self.tb_slip.AddLabelTool(wx.ID_FIND, u"Consultar",
                                                          wx.Bitmap(u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY),
                                                          wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                          None)

        self.bt_reg_estornar = self.tb_slip.AddLabelTool(wx.ID_DELETE, u"Estornar",
                                                         wx.Bitmap(u"icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY),
                                                         wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                         None)

        self.tb_slip.AddSeparator()

        self.bt_confirmar = self.tb_slip.AddLabelTool(wx.ID_SAVE, u"Grava registro",
                                                      wx.Bitmap(u"icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY),
                                                      wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                      None)

        self.bt_reg_cancelar = self.tb_slip.AddLabelTool(wx.ID_CANCEL, u"Cancelar",
                                                         wx.Bitmap(u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY),
                                                         wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                         None)

        self.tb_slip.Realize()

        lay_body = wx.BoxSizer(wx.VERTICAL)

        lay_options = wx.BoxSizer(wx.VERTICAL)

        lay_body.Add(lay_options, 1, wx.EXPAND, 5)

        lay_slip = wx.BoxSizer(wx.VERTICAL)

        self.pn_cabecalho = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC)
        lay_cabecalho = wx.BoxSizer(wx.HORIZONTAL)

        lay_cabec_rotulo_01 = wx.BoxSizer(wx.VERTICAL)

        self.lb_empresa = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Empresa:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_empresa.Wrap(-1)

        lay_cabec_rotulo_01.Add(self.lb_empresa, 0, wx.ALL, 5)

        self.lb_documento = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Número lançamento:", wx.DefaultPosition,
                                          wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_documento.Wrap(-1)

        lay_cabec_rotulo_01.Add(self.lb_documento, 0, wx.ALL, 5)

        self.lb_dt_criacao = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Criado em:", wx.DefaultPosition,
                                           wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_dt_criacao.Wrap(-1)

        lay_cabec_rotulo_01.Add(self.lb_dt_criacao, 0, wx.ALL, 5)

        self.lb_dt_movimento = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Data do movimento:", wx.DefaultPosition,
                                             wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_dt_movimento.Wrap(-1)

        lay_cabec_rotulo_01.Add(self.lb_dt_movimento, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_rotulo_01, 0, wx.EXPAND, 5)

        lay_cabec_campos_01 = wx.BoxSizer(wx.VERTICAL)

        self.tc_empresa = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                      0)
        self.tc_empresa.Enable(False)

        lay_cabec_campos_01.Add(self.tc_empresa, 0, wx.ALL, 5)

        self.tc_num_documento = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(150, 26), 0)
        self.tc_num_documento.Enable(False)

        lay_cabec_campos_01.Add(self.tc_num_documento, 0, wx.ALL, 5)

        self.tc_dt_criacao = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(-1, 26), 0)
        self.tc_dt_criacao.Enable(False)

        lay_cabec_campos_01.Add(self.tc_dt_criacao, 0, wx.ALL, 5)

        self.tc_dt_movimento = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(-1, 26), 0)
        self.tc_dt_movimento.Enable(False)

        lay_cabec_campos_01.Add(self.tc_dt_movimento, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_campos_01, 1, wx.EXPAND, 5)

        lay_cabec_rotulo_02 = wx.BoxSizer(wx.VERTICAL)

        self.lb_periodo = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Período:", wx.DefaultPosition, wx.Size(150, 26),
                                        wx.ALIGN_RIGHT)
        self.lb_periodo.Wrap(-1)

        lay_cabec_rotulo_02.Add(self.lb_periodo, 0, wx.ALL, 5)

        self.lb_exercicio = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Exercício:", wx.DefaultPosition,
                                          wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_exercicio.Wrap(-1)

        lay_cabec_rotulo_02.Add(self.lb_exercicio, 0, wx.ALL, 5)

        self.lb_usuario = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Criado por:", wx.DefaultPosition,
                                        wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_usuario.Wrap(-1)

        lay_cabec_rotulo_02.Add(self.lb_usuario, 0, wx.ALL, 5)

        self.lb_condicao = wx.StaticText(self.pn_cabecalho, wx.ID_ANY, u"Condição:", wx.DefaultPosition,
                                         wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_condicao.Wrap(-1)

        lay_cabec_rotulo_02.Add(self.lb_condicao, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_rotulo_02, 0, wx.EXPAND, 5)

        lay_cabec_campos_02 = wx.BoxSizer(wx.VERTICAL)

        self.tc_periodo = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                      0)
        self.tc_periodo.Enable(False)

        lay_cabec_campos_02.Add(self.tc_periodo, 0, wx.ALL, 5)

        self.tc_exercicio = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(100, 26), 0)
        self.tc_exercicio.Enable(False)

        lay_cabec_campos_02.Add(self.tc_exercicio, 0, wx.ALL, 5)

        self.tc_usuario = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(200, 26), 0)
        self.tc_usuario.Enable(False)

        lay_cabec_campos_02.Add(self.tc_usuario, 0, wx.ALL, 5)

        self.tc_condicao = wx.TextCtrl(self.pn_cabecalho, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(150, 26), 0)
        self.tc_condicao.Enable(False)

        lay_cabec_campos_02.Add(self.tc_condicao, 0, wx.ALL, 5)

        lay_cabecalho.Add(lay_cabec_campos_02, 1, wx.EXPAND, 5)

        self.pn_cabecalho.SetSizer(lay_cabecalho)
        self.pn_cabecalho.Layout()
        lay_cabecalho.Fit(self.pn_cabecalho)
        lay_slip.Add(self.pn_cabecalho, 0, wx.EXPAND, 5)

        self.pn_registros = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE)
        lay_detalhes = wx.BoxSizer(wx.VERTICAL)

        self.pn_partidas = wx.Panel(self.pn_registros, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        lay_partidas = wx.BoxSizer(wx.VERTICAL)

        self.gd_partidas = wx.grid.Grid(self.pn_partidas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.gd_partidas.CreateGrid(0, 5)
        self.gd_partidas.EnableEditing(False)
        self.gd_partidas.EnableGridLines(False)
        self.gd_partidas.EnableDragGridSize(False)
        self.gd_partidas.SetMargins(0, 0)

        # Columns
        self.gd_partidas.SetColSize(0, 70)
        self.gd_partidas.SetColSize(1, 100)
        self.gd_partidas.SetColSize(2, 350)
        self.gd_partidas.SetColSize(3, 150)
        self.gd_partidas.SetColSize(4, 60)
        self.gd_partidas.EnableDragColMove(False)
        self.gd_partidas.EnableDragColSize(False)
        self.gd_partidas.SetColLabelSize(30)
        self.gd_partidas.SetColLabelValue(0, u"Registro")
        self.gd_partidas.SetColLabelValue(1, u"Conta")
        self.gd_partidas.SetColLabelValue(2, u"Descrição")
        self.gd_partidas.SetColLabelValue(3, u"Montante")
        self.gd_partidas.SetColLabelValue(4, u"Moeda")
        self.gd_partidas.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)

        # Rows
        self.gd_partidas.EnableDragRowSize(True)
        self.gd_partidas.SetRowLabelSize(30)
        self.gd_partidas.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.gd_partidas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        lay_partidas.Add(self.gd_partidas, 1, wx.EXPAND, 5)

        self.pn_partidas.SetSizer(lay_partidas)
        self.pn_partidas.Layout()
        lay_partidas.Fit(self.pn_partidas)
        lay_detalhes.Add(self.pn_partidas, 1, wx.EXPAND, 5)

        self.pn_detalhes = wx.Panel(self.pn_registros, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.pn_detalhes.Hide()

        lay_detalhes1 = wx.BoxSizer(wx.HORIZONTAL)

        lay_detal_rotulos_01 = wx.BoxSizer(wx.VERTICAL)

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

        self.tc_registro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                       0)
        self.tc_registro.Enable(False)

        lay_detal_campos_01.Add(self.tc_registro, 0, wx.ALL, 5)

        self.tc_situacao = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(35, 26),
                                       0)
        self.tc_situacao.Enable(False)

        lay_detal_campos_01.Add(self.tc_situacao, 0, wx.ALL, 5)

        self.tc_tipo_registro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, 26), 0)
        self.tc_tipo_registro.Enable(False)

        lay_detal_campos_01.Add(self.tc_tipo_registro, 0, wx.ALL, 5)

        lay_unidade = wx.BoxSizer(wx.HORIZONTAL)

        self.tc_unidade = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 26),
                                      0)
        self.tc_unidade.Enable(False)

        lay_unidade.Add(self.tc_unidade, 0, wx.ALL, 5)

        self.bt_cons_unidade = wx.BitmapButton(self.pn_detalhes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                               wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_cons_unidade.SetBitmap(wx.Bitmap(u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY))
        lay_unidade.Add(self.bt_cons_unidade, 0, wx.ALL, 5)

        lay_detal_campos_01.Add(lay_unidade, 1, wx.EXPAND, 5)

        cb_chave_registroChoices = [u"D", u"C"]
        self.cb_chave_registro = wx.ComboBox(self.pn_detalhes, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size(50, 26),
                                             cb_chave_registroChoices, 0)
        self.cb_chave_registro.SetSelection(0)
        self.cb_chave_registro.Enable(False)

        lay_detal_campos_01.Add(self.cb_chave_registro, 0, wx.ALL, 5)

        lay_conta = wx.BoxSizer(wx.HORIZONTAL)

        self.tc_conta_contabil = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(70, 26), 0)
        self.tc_conta_contabil.SetMaxLength(6)
        self.tc_conta_contabil.Enable(False)

        lay_conta.Add(self.tc_conta_contabil, 0, wx.ALL, 5)

        self.bt_cons_conta_contabil = wx.BitmapButton(self.pn_detalhes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                      wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_cons_conta_contabil.SetBitmap(wx.Bitmap(u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY))
        lay_conta.Add(self.bt_cons_conta_contabil, 0, wx.ALL, 5)

        lay_detal_campos_01.Add(lay_conta, 1, wx.EXPAND, 1)

        lay_centro_lucro = wx.BoxSizer(wx.HORIZONTAL)

        self.tc_centro_lucro = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(70, 26), 0)
        self.tc_centro_lucro.SetMaxLength(6)
        self.tc_centro_lucro.Enable(False)

        lay_centro_lucro.Add(self.tc_centro_lucro, 0, wx.ALL, 5)

        self.bt_cons_centro_lucro = wx.BitmapButton(self.pn_detalhes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_cons_centro_lucro.SetBitmap(wx.Bitmap(u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY))
        lay_centro_lucro.Add(self.bt_cons_centro_lucro, 0, wx.ALL, 5)

        lay_detal_campos_01.Add(lay_centro_lucro, 1, wx.EXPAND, 5)

        lay_detalhes1.Add(lay_detal_campos_01, 0, wx.EXPAND, 5)

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
        self.tc_descricao.Enable(False)

        lay_detal_campos_02.Add(self.tc_descricao, 0, wx.ALL, 5)

        self.tc_doc_referencia = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(150, 26), 0)
        self.tc_doc_referencia.Enable(False)

        lay_detal_campos_02.Add(self.tc_doc_referencia, 0, wx.ALL, 5)

        self.tc_doc_compensacao = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(150, 26), 0)
        self.tc_doc_compensacao.Enable(False)

        lay_detal_campos_02.Add(self.tc_doc_compensacao, 0, wx.ALL, 5)

        self.tc_montante = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(150, 26), 0)
        self.tc_montante.Enable(False)

        lay_detal_campos_02.Add(self.tc_montante, 0, wx.ALL, 5)

        self.tc_moeda = wx.TextCtrl(self.pn_detalhes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, 26), 0)
        self.tc_moeda.SetMaxLength(3)
        self.tc_moeda.Enable(False)

        lay_detal_campos_02.Add(self.tc_moeda, 0, wx.ALL, 5)

        lay_detalhes1.Add(lay_detal_campos_02, 1, wx.EXPAND, 5)

        self.pn_detalhes.SetSizer(lay_detalhes1)
        self.pn_detalhes.Layout()
        lay_detalhes1.Fit(self.pn_detalhes)
        lay_detalhes.Add(self.pn_detalhes, 1, wx.EXPAND, 5)

        self.pn_botoes = wx.Panel(self.pn_registros, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL | wx.BORDER_RAISED)
        lay_botao = wx.BoxSizer(wx.HORIZONTAL)

        self.bt_part_adicionar = wx.BitmapButton(self.pn_botoes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                 wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_part_adicionar.SetBitmap(wx.Bitmap(u"icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_adicionar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_adicionar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_adicionar.Enable(False)

        lay_botao.Add(self.bt_part_adicionar, 0, wx.ALL, 5)

        self.bt_part_consultar = wx.BitmapButton(self.pn_botoes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                 wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_part_consultar.SetBitmap(wx.Bitmap(u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_consultar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_consultar.Enable(False)

        lay_botao.Add(self.bt_part_consultar, 0, wx.ALL, 5)

        self.bt_part_excluir = wx.BitmapButton(self.pn_botoes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                               wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_part_excluir.SetBitmap(wx.Bitmap(u"icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_excluir.SetBitmapDisabled(wx.Bitmap(u"icons/ac_lixeira_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_excluir.Enable(False)

        lay_botao.Add(self.bt_part_excluir, 0, wx.ALL, 5)

        self.bt_part_confirmar = wx.BitmapButton(self.pn_botoes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                 wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_part_confirmar.SetBitmap(wx.Bitmap(u"icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_confirmar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_confirmar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_confirmar.Enable(False)

        lay_botao.Add(self.bt_part_confirmar, 0, wx.ALL, 5)

        self.bt_part_cancelar = wx.BitmapButton(self.pn_botoes, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.bt_part_cancelar.SetBitmap(wx.Bitmap(u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_cancelar.SetBitmapDisabled(wx.Bitmap(u"icons/ac_cancelar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        self.bt_part_cancelar.Enable(False)

        lay_botao.Add(self.bt_part_cancelar, 0, wx.ALL, 5)

        self.pn_botoes.SetSizer(lay_botao)
        self.pn_botoes.Layout()
        lay_botao.Fit(self.pn_botoes)
        lay_detalhes.Add(self.pn_botoes, 0, wx.EXPAND | wx.ALL, 5)

        self.pn_registros.SetSizer(lay_detalhes)
        self.pn_registros.Layout()
        lay_detalhes.Fit(self.pn_registros)
        lay_slip.Add(self.pn_registros, 1, wx.EXPAND, 5)

        lay_body.Add(lay_slip, 1, wx.EXPAND, 5)

        self.SetSizer(lay_body)
        self.Layout()
        self.sb_slip = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.ac_reg_adicionar, id=self.bt_reg_adicionar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_reg_consultar, id=self.bt_reg_consultar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_reg_estornar, id=self.bt_reg_estornar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_confirmar, id=self.bt_confirmar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_reg_cancelar, id=self.bt_reg_cancelar.GetId())
        self.bt_cons_unidade.Bind(wx.EVT_BUTTON, self.ac_cons_unidade)
        self.bt_cons_conta_contabil.Bind(wx.EVT_BUTTON, self.ac_cons_conta)
        self.bt_cons_centro_lucro.Bind(wx.EVT_BUTTON, self.ac_cons_clucro)
        self.bt_part_adicionar.Bind(wx.EVT_BUTTON, self.ac_part_adicionar)
        self.bt_part_consultar.Bind(wx.EVT_BUTTON, self.ac_part_consultar)
        self.bt_part_excluir.Bind(wx.EVT_BUTTON, self.ac_part_excluir)
        self.bt_part_confirmar.Bind(wx.EVT_BUTTON, self.ac_part_confirmar)
        self.bt_part_cancelar.Bind(wx.EVT_BUTTON, self.ac_part_cancelar)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ac_reg_adicionar(self, event):
        event.Skip()

    def ac_reg_consultar(self, event):
        event.Skip()

    def ac_reg_estornar(self, event):
        event.Skip()

    def ac_confirmar(self, event):
        event.Skip()

    def ac_reg_cancelar(self, event):
        event.Skip()

    def ac_cons_unidade(self, event):
        event.Skip()

    def ac_cons_conta(self, event):
        event.Skip()

    def ac_cons_clucro(self, event):
        event.Skip()

    def ac_part_adicionar(self, event):
        event.Skip()

    def ac_part_consultar(self, event):
        event.Skip()

    def ac_part_excluir(self, event):
        event.Skip()

    def ac_part_confirmar(self, event):
        event.Skip()

    def ac_part_cancelar(self, event):
        event.Skip()
