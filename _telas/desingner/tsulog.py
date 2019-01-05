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
## Class TSULOG
###########################################################################

class TSULOG(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Credenciais", pos=wx.DefaultPosition,
                           size=wx.Size(233, 390), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        lay_bady = wx.BoxSizer(wx.VERTICAL)

        lay_dados = wx.FlexGridSizer(0, 2, 0, 0)
        lay_dados.SetFlexibleDirection(wx.BOTH)
        lay_dados.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.LbHost = wx.StaticText(self, wx.ID_ANY, u"Servidor", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbHost.Wrap(-1)
        lay_dados.Add(self.LbHost, 0, wx.ALL, 5)

        self.tc_host = wx.TextCtrl(self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize, 0)
        lay_dados.Add(self.tc_host, 0, wx.ALL, 5)

        self.LbUser = wx.StaticText(self, wx.ID_ANY, u"Usuário", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbUser.Wrap(-1)
        lay_dados.Add(self.LbUser, 0, wx.ALL, 5)

        self.tc_user = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        lay_dados.Add(self.tc_user, 0, wx.ALL, 5)

        self.LbSenha = wx.StaticText(self, wx.ID_ANY, u"Senha", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbSenha.Wrap(-1)
        lay_dados.Add(self.LbSenha, 0, wx.ALL, 5)

        self.tc_senha = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        lay_dados.Add(self.tc_senha, 0, wx.ALL, 5)

        self.LbDatabase = wx.StaticText(self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LbDatabase.Wrap(-1)
        lay_dados.Add(self.LbDatabase, 0, wx.ALL, 5)

        self.tc_database = wx.TextCtrl(self, wx.ID_ANY, u"fvb_db", wx.DefaultPosition, wx.DefaultSize, 0)
        lay_dados.Add(self.tc_database, 0, wx.ALL, 5)

        self.lb_empresa = wx.StaticText(self, wx.ID_ANY, u"Empresa", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lb_empresa.Wrap(-1)
        lay_dados.Add(self.lb_empresa, 0, wx.ALL, 5)

        self.tc_empresa = wx.TextCtrl(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.tc_empresa.SetMaxLength(4)
        lay_dados.Add(self.tc_empresa, 0, wx.ALL, 5)

        lay_bady.Add(lay_dados, 0, wx.EXPAND, 5)

        lay_botoes = wx.GridSizer(1, 2, 1, 2)

        lay_botoes.SetMinSize(wx.Size(50, -1))
        self.BtnLogin = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        lay_botoes.Add(self.BtnLogin, 0, wx.ALL, 5)

        self.BtnCancel = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        lay_botoes.Add(self.BtnCancel, 0, wx.ALL, 5)

        lay_bady.Add(lay_botoes, 0, wx.EXPAND, 10)

        lay_mensagem = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Mensagem"), wx.VERTICAL)

        lay_mensagem.SetMinSize(wx.Size(200, -1))
        self.tb_mensagem = wx.TextCtrl(lay_mensagem.GetStaticBox(), wx.ID_ANY,
                                       u"Bem vindo ao ERP Caseiro. Favor entrar com suas credenciais.",
                                       wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        lay_mensagem.Add(self.tb_mensagem, 1, wx.EXPAND, 5)

        lay_bady.Add(lay_mensagem, 1, wx.EXPAND, 5)

        self.SetSizer(lay_bady)
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
