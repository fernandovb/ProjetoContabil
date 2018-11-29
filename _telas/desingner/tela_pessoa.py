# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class FrmPessoa
###########################################################################

class FrmPessoa(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gestão de Pessoas", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.tb_pessoa = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.btn_adicionar = self.tb_pessoa.AddLabelTool(wx.ID_ANY, u"Novo",
                                                         wx.Bitmap(u"icons/ac_adicionar_32x32.png", wx.BITMAP_TYPE_ANY),
                                                         wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                         None)

        self.btn_editar = self.tb_pessoa.AddLabelTool(wx.ID_ANY, u"Editar",
                                                      wx.Bitmap(u"icons/ac_editar_32x32.png", wx.BITMAP_TYPE_ANY),
                                                      wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                      None)

        self.btn_consultar = self.tb_pessoa.AddLabelTool(wx.ID_ANY, u"Consultar",
                                                         wx.Bitmap(u"icons/ac_buscar_32x32.png", wx.BITMAP_TYPE_ANY),
                                                         wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                         None)

        self.tb_pessoa.AddSeparator()

        self.btn_cancelar = self.tb_pessoa.AddLabelTool(wx.ID_ANY, u"Cancelar",
                                                        wx.Bitmap(u"icons/ac_cancelar_32x32.png", wx.BITMAP_TYPE_ANY),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)

        self.btn_gravar = self.tb_pessoa.AddLabelTool(wx.ID_ANY, u"Gravar",
                                                      wx.Bitmap(u"icons/ac_confirmar_32x32.png", wx.BITMAP_TYPE_ANY),
                                                      wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                      None)

        self.tb_pessoa.Realize()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.ac_adicionar, id=self.btn_adicionar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_editar, id=self.btn_editar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_consultar, id=self.btn_consultar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_cancelar, id=self.btn_cancelar.GetId())
        self.Bind(wx.EVT_TOOL, self.ac_gravar, id=self.btn_gravar.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ac_adicionar(self, event):
        event.Skip()

    def ac_editar(self, event):
        event.Skip()

    def ac_consultar(self, event):
        event.Skip()

    def ac_cancelar(self, event):
        event.Skip()

    def ac_gravar(self, event):
        event.Skip()
