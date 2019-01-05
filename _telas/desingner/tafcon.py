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
## Class TAFCON
###########################################################################

class TAFCON(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Procurar conta", pos=wx.DefaultPosition,
                           size=wx.Size(636, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        lay_body = wx.BoxSizer(wx.VERTICAL)

        self.pn_body = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.pn_lista = wx.Panel(self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        lay_lista = wx.BoxSizer(wx.VERTICAL)

        self.gd_resultado = wx.grid.Grid(self.pn_lista, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.gd_resultado.CreateGrid(0, 3)
        self.gd_resultado.EnableEditing(False)
        self.gd_resultado.EnableGridLines(False)
        self.gd_resultado.EnableDragGridSize(False)
        self.gd_resultado.SetMargins(0, 0)

        # Columns
        self.gd_resultado.SetColSize(0, 90)
        self.gd_resultado.SetColSize(1, 310)
        self.gd_resultado.SetColSize(2, 150)
        self.gd_resultado.EnableDragColMove(False)
        self.gd_resultado.EnableDragColSize(True)
        self.gd_resultado.SetColLabelSize(30)
        self.gd_resultado.SetColLabelValue(0, u"CÓDIGO")
        self.gd_resultado.SetColLabelValue(1, u"DESCRIÇÃO")
        self.gd_resultado.SetColLabelValue(2, u"ORDEM")
        self.gd_resultado.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.gd_resultado.EnableDragRowSize(True)
        self.gd_resultado.SetRowLabelSize(30)
        self.gd_resultado.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.gd_resultado.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        lay_lista.Add(self.gd_resultado, 1, wx.EXPAND, 5)

        self.pn_lista.SetSizer(lay_lista)
        self.pn_lista.Layout()
        lay_lista.Fit(self.pn_lista)
        bSizer8.Add(self.pn_lista, 1, wx.ALL | wx.EXPAND, 5)

        self.pn_dados = wx.Panel(self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.pn_dados.Hide()

        lay_dados = wx.BoxSizer(wx.HORIZONTAL)

        lay_titulos = wx.BoxSizer(wx.VERTICAL)

        self.lb_conta_contabil = wx.StaticText(self.pn_dados, wx.ID_ANY, u"Conta contábil:", wx.DefaultPosition,
                                               wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_conta_contabil.Wrap(-1)

        lay_titulos.Add(self.lb_conta_contabil, 0, wx.ALL, 5)

        self.lb_descricao = wx.StaticText(self.pn_dados, wx.ID_ANY, u"Nome da conta:", wx.DefaultPosition,
                                          wx.Size(150, 26), wx.ALIGN_RIGHT)
        self.lb_descricao.Wrap(-1)

        lay_titulos.Add(self.lb_descricao, 0, wx.ALL, 5)

        self.lb_ordem = wx.StaticText(self.pn_dados, wx.ID_ANY, u"Ordem:", wx.DefaultPosition, wx.Size(150, 26),
                                      wx.ALIGN_RIGHT)
        self.lb_ordem.Wrap(-1)

        lay_titulos.Add(self.lb_ordem, 0, wx.ALL, 5)

        lay_dados.Add(lay_titulos, 0, wx.EXPAND, 5)

        lay_campos = wx.BoxSizer(wx.VERTICAL)

        self.tc_conta_contabil = wx.TextCtrl(self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(80, 26), 0)
        lay_campos.Add(self.tc_conta_contabil, 0, wx.ALL, 5)

        self.tc_descricao = wx.TextCtrl(self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 26),
                                        0)
        lay_campos.Add(self.tc_descricao, 0, wx.ALL, 5)

        self.tc_ordem = wx.TextCtrl(self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 26), 0)
        lay_campos.Add(self.tc_ordem, 0, wx.ALL, 5)

        lay_dados.Add(lay_campos, 1, wx.EXPAND, 5)

        self.pn_dados.SetSizer(lay_dados)
        self.pn_dados.Layout()
        lay_dados.Fit(self.pn_dados)
        bSizer8.Add(self.pn_dados, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.pn_botoes = wx.Panel(self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC)
        gSizer1 = wx.GridSizer(1, 3, 0, 0)

        self.bt_confirmar = wx.Button(self.pn_botoes, wx.ID_OK, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bt_confirmar.Enable(False)

        gSizer1.Add(self.bt_confirmar, 0, wx.ALL | wx.EXPAND, 5)

        self.bt_localizar = wx.Button(self.pn_botoes, wx.ID_FIND, u"Localizar", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.bt_localizar, 0, wx.ALL | wx.EXPAND, 5)

        self.bt_cancelar = wx.Button(self.pn_botoes, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.bt_cancelar, 0, wx.ALL | wx.EXPAND, 5)

        self.pn_botoes.SetSizer(gSizer1)
        self.pn_botoes.Layout()
        gSizer1.Fit(self.pn_botoes)
        bSizer7.Add(self.pn_botoes, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 5)

        bSizer6.Add(bSizer7, 0, wx.EXPAND, 5)

        self.pn_body.SetSizer(bSizer6)
        self.pn_body.Layout()
        bSizer6.Fit(self.pn_body)
        lay_body.Add(self.pn_body, 1, wx.EXPAND, 5)

        self.SetSizer(lay_body)
        self.Layout()

        # Connect Events
        self.gd_resultado.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.ac_selecionar)
        self.bt_localizar.Bind(wx.EVT_BUTTON, self.ac_localizar)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ac_selecionar(self, event):
        event.Skip()

    def ac_localizar(self, event):
        event.Skip()
