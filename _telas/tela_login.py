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
## Class FrmLogin
###########################################################################

class FrmLogin(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Credenciais", pos=wx.DefaultPosition,
                           size=wx.Size(233, 390), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.LbHost = wx.StaticText(self, wx.ID_ANY, u"Servidor", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbHost.Wrap(-1)
        fgSizer2.Add(self.LbHost, 0, wx.ALL, 5)

        self.TxHost = wx.TextCtrl(self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.TxHost, 0, wx.ALL, 5)

        self.LbUser = wx.StaticText(self, wx.ID_ANY, u"Usuário", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbUser.Wrap(-1)
        fgSizer2.Add(self.LbUser, 0, wx.ALL, 5)

        self.TxUser = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.TxUser, 0, wx.ALL, 5)

        self.LbSenha = wx.StaticText(self, wx.ID_ANY, u"Senha", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbSenha.Wrap(-1)
        fgSizer2.Add(self.LbSenha, 0, wx.ALL, 5)

        self.TxSenha = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer2.Add(self.TxSenha, 0, wx.ALL, 5)

        self.LbDatabase = wx.StaticText(self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbDatabase.Wrap(-1)
        fgSizer2.Add(self.LbDatabase, 0, wx.ALL, 5)

        self.TxDatabase = wx.TextCtrl(self, wx.ID_ANY, u"fvb_db", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.TxDatabase, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer2, 0, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(1, 2, 1, 2)

        gSizer2.SetMinSize(wx.Size(50, -1))
        self.BtnLogin = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.BtnLogin, 0, wx.ALL, 5)

        self.BtnCancel = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.BtnCancel, 0, wx.ALL, 5)

        bSizer1.Add(gSizer2, 0, wx.EXPAND, 10)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Mensagem"), wx.VERTICAL)

        sbSizer3.SetMinSize(wx.Size(200, -1))
        self.tb_mensagem = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY,
                                       u"Bem vindo ao ERP Caseiro. Favor entrar com suas credenciais.",
                                       wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer3.Add(self.tb_mensagem, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_cancelar)
        self.BtnLogin.Bind(wx.EVT_BUTTON, self.on_login)
        self.BtnCancel.Bind(wx.EVT_BUTTON, self.on_cancelar)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_cancelar(self, event):
        event.Skip()

    def on_login(self, event):
        event.Skip()
