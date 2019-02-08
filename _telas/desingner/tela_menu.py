# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrmMenu
###########################################################################

class FrmMenu(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Menu Principal", pos=wx.DefaultPosition,
                          size=wx.Size(883, 620), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.MnbMenu = wx.MenuBar(0)
        self.MnPrincipal = wx.Menu()
        self.mn_cadastro = wx.Menu()
        self.mn_dbemp01 = wx.MenuItem(self.mn_cadastro, wx.ID_ANY, u"Empresas", wx.EmptyString, wx.ITEM_NORMAL)
        self.mn_cadastro.Append(self.mn_dbemp01)

        self.mn_prm01 = wx.MenuItem(self.mn_cadastro, wx.ID_ANY, u"Pessoas", wx.EmptyString, wx.ITEM_NORMAL)
        self.mn_cadastro.Append(self.mn_prm01)

        self.mn_crctm = wx.MenuItem(self.mn_cadastro, wx.ID_ANY, u"Contratos", wx.EmptyString, wx.ITEM_NORMAL)
        self.mn_cadastro.Append(self.mn_crctm)

        self.MnPrincipal.AppendSubMenu(self.mn_cadastro, u"Cadastros")

        self.MniSair = wx.MenuItem(self.MnPrincipal, wx.ID_ANY, u"&Sair", wx.EmptyString, wx.ITEM_NORMAL)
        self.MnPrincipal.Append(self.MniSair)

        self.MnbMenu.Append(self.MnPrincipal, u"Principal")

        self.mn_sistema = wx.Menu()
        self.mn_backup = wx.MenuItem(self.mn_sistema, wx.ID_ANY, u"Backup", u"Cópia de segurança do BD", wx.ITEM_NORMAL)
        self.mn_sistema.Append(self.mn_backup)

        self.MnbMenu.Append(self.mn_sistema, u"Sistema")

        self.MnSobre = wx.Menu()
        self.mn_info = wx.MenuItem(self.MnSobre, wx.ID_ANY, u"Sobre o sistema", wx.EmptyString, wx.ITEM_NORMAL)
        self.MnSobre.Append(self.mn_info)

        self.MnbMenu.Append(self.MnSobre, u"S&obre")

        self.SetMenuBar(self.MnbMenu)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.lb_executar = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"Executar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lb_executar.Wrap(-1)

        self.m_toolBar1.AddControl(self.lb_executar)
        self.tc_executar = wx.TextCtrl(self.m_toolBar1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.m_toolBar1.AddControl(self.tc_executar)
        self.bt_executar = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"tool",
                                                        wx.Bitmap(u"icons/ac_executar_16x16.png", wx.BITMAP_TYPE_ANY),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)

        self.m_toolBar1.AddSeparator()

        self.m_toolBar1.Realize()

        self.StbMenu = self.CreateStatusBar(3, wx.STB_DEFAULT_STYLE, wx.ID_ANY)
        SizPrincipal = wx.BoxSizer(wx.VERTICAL)

        SizBody = wx.BoxSizer(wx.HORIZONTAL)

        SizLeft = wx.BoxSizer(wx.HORIZONTAL)

        SizLeft.SetMinSize(wx.Size(300, -1))
        self.m_treeCtrl1 = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        SizLeft.Add(self.m_treeCtrl1, 1, wx.EXPAND, 5)

        SizBody.Add(SizLeft, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        SizBody.Add(bSizer5, 1, wx.EXPAND, 5)

        SizPrincipal.Add(SizBody, 1, wx.EXPAND, 5)

        self.SetSizer(SizPrincipal)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.ac_emp01, id=self.mn_dbemp01.GetId())
        self.Bind(wx.EVT_MENU, self.ac_prm01, id=self.mn_prm01.GetId())
        self.Bind(wx.EVT_MENU, self.ac_crctm, id=self.mn_crctm.GetId())
        self.Bind(wx.EVT_MENU, self.on_sair, id=self.MniSair.GetId())
        self.Bind(wx.EVT_MENU, self.ac_backup, id=self.mn_backup.GetId())
        self.Bind(wx.EVT_MENU, self.ac_sobre, id=self.mn_info.GetId())
        self.tc_executar.Bind(wx.EVT_TEXT_ENTER, self.ac_executar)
        self.Bind(wx.EVT_TOOL, self.ac_executar, id=self.bt_executar.GetId())

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def ac_emp01(self, event):
        event.Skip()

    def ac_prm01(self, event):
        event.Skip()

    def ac_crctm(self, event):
        event.Skip()

    def on_sair(self, event):
        event.Skip()

    def ac_backup(self, event):
        event.Skip()

    def ac_sobre(self, event):
        event.Skip()

    def ac_executar(self, event):
        event.Skip()
