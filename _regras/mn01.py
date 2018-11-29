# -*- coding: utf-8 -*-

import wx
import wx.xrc
from wx.lib.pubsub import pub
from _telas import *
from _telas.desingner.tela_menu import FrmMenu
from _telas.tsulog01 import SULOG01
import _dados.ssgcon as conexao

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


class MN01(FrmMenu):

    def __init__(self, *args, **kwargs):
        super(MN01, self).__init__(*args, **kwargs)
        # Definições do menu TreeCtrl
        self.TrcTransacoes = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, -1), wx.TR_HAS_BUTTONS)
        #lay_left.Add(self.TrcTransacoes, 0, wx.EXPAND)

        # Definições da Barra de Status
        self.StbMenu.SetStatusWidths([200, 300, 300])
        self.StbMenu.SetStatusText('Usuário:', 0)
        self.StbMenu.SetStatusText('Status da conexão: OFF', 1)

        pub.subscribe(self.my_listener, 'frameListener')
        dlg = SULOG01()
        dlg.ShowModal()

    def on_sair(self, event):
        conexao.conn.on_encerrar()
        exit()

    def my_listener(self, message, arg2=None):
        if not conexao.conn.user_name[0] == None:
            self.StbMenu.SetStatusText(f'Usuário: {conexao.conn.user_name[0]}', 0)
            self.StbMenu.SetStatusText('Status da conexão: ON', 1)
        self.Show()

    def ac_prm01(self, event):
        self.ac_chama_form('ARSLIP01')

    def ac_chama_form(self, tela=''):
        t = tela.lower() + '.' + tela.upper()
        exec('frame = ' + t + '(self)')
        exec('frame.Show()')

    def ac_emp01(self, event):
        self.ac_chama_form('EREMP01')

    def ac_sobre(self, event):
        wx.MessageBox(f'Eu sou uma mensagem, {conexao.conn.user}', caption='Olá!!!', style=wx.OK | wx.ICON_INFORMATION)
