# -*- coding: utf-8 -*- 

import wx
import wx.xrc

at = ['Cadastro', ['Geral', ['Atividade', 'Ocupacao'],
                   'Controle']]


class MyTree(wx.TreeCtrl):

    def __init__(self, parent, id, position, size, style):
        wx.TreeCtrl.__init__(self, parent, id, position, size, style)
        root = self.AddRoot('Transações')
        self.SetItemData(root, ('key', 'value'))
        # Inclusão do primeiro nível
        self.on_preenche_lista(root, at)

        self.Expand(root)

    def on_preenche_lista(self, item, lista):
        """Lê uma lista de valores, e suas sublistas, para montar uma árvore
        É necessário a criação de uma lista, com suas sublistas para fazer a montagem.
        Ao ser invocado, on_preenche_lista incluíra o item que não for uma lista no
        elemento TreeCtrl.

        :param lista: lista com valores string para preenchimento da árvore
        :param item: item inicial que as strings serão incluidas
        """
        novo_item = item
        for e in lista:
            if type(e) is list:
                self.on_preenche_lista(novo_item, e)
            else:
                novo_item = self.AppendItem(item, e)


class FrmMenu(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Menu Principal", pos=wx.DefaultPosition,
                          size=wx.Size(883, 620), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        ## Definições do menu suspenso
        # Menu Sistema. Contém os menus cadastro, sair
        self.mn_sistema = wx.Menu()
        # Submenu cadastro e item menu pessoa
        self.mn_cadastro = wx.Menu()
        self.mn_pessoa = wx.MenuItem(self.mn_cadastro, wx.ID_ANY, 'Pessoas', 'Cdastro de pessoas')
        self.mn_empresa = wx.MenuItem(self.mn_cadastro, wx.ID_ANY, 'Empresas', 'Cadastro de empresas')
        self.mn_cadastro.Append(self.mn_pessoa)
        self.mn_cadastro.Append(self.mn_empresa)
        self.mn_sistema.AppendSubMenu(self.mn_cadastro, 'Cadastros')
        # Item menu 'sair'
        self.mn_sistema.AppendSeparator()
        self.mn_sair = self.mn_sistema.Append(wx.ID_EXIT, 'Sair', 'Encerra o sistema')
        # Menu Sistema. Não contém menus atrelados
        self.mn_sobre = wx.Menu()
        # Instacia barra de menus
        self.menu = wx.MenuBar()
        # Inclui barra de menu ao formulário
        self.SetMenuBar(self.menu)
        # Inclui menus à barra de menus
        self.menu.Append(self.mn_sistema, 'Sistema')
        self.menu.Append(self.mn_sobre, 'Sobre')

        # Definições da Barra de Status
        self.StbMenu = self.CreateStatusBar(3, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.StbMenu.SetStatusWidths([200, 300, 300])
        self.StbMenu.SetStatusText('Usuário: ', 0)
        self.StbMenu.SetStatusText('Status da conexão: ', 1)

        # Definições do Sizer principal (organizador)
        lay_principal = wx.BoxSizer(wx.VERTICAL)

        lay_body = wx.BoxSizer(wx.HORIZONTAL)

        # Definições do menu TreeCtrl
        self.TrcTransacoes = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, -1), wx.TR_HAS_BUTTONS)

        # Definições do Size esquerdo - Exibição de menu TreeView
        lay_left = wx.BoxSizer(wx.HORIZONTAL)
        lay_left.Add(self.TrcTransacoes, 0, wx.EXPAND)
        lay_body.Add(lay_left, 1, wx.EXPAND)

        lay_principal.Add(lay_body, 1, wx.EXPAND)

        self.SetSizer(lay_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        # Ligação de eventos com objetos
        self.Bind(wx.EVT_CLOSE, self.on_sair)
        self.Bind(wx.EVT_MENU, self.cad_pessoas, self.mn_pessoa)
        self.Bind(wx.EVT_MENU, self.on_sair, self.mn_sair)
        self.Bind(wx.EVT_MENU, self.cad_empresas, self.mn_empresa)

    def __del__(self):
        pass

    def on_sair(self, event):
        event.Skip()

    def cad_pessoas(self, event):
        event.Skip()

    def cad_empresas(self, event):
        event.Skip()
