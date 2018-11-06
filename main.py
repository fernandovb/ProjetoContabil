# -*- coding: utf-8 -*-

import wx.xrc
from wx.lib.pubsub import pub
from _telas.tela_menu import FrmMenu
from _regras.sblog01 import SBLOG01
from _regras.prm01 import PRM01
from _regras.dbemp01 import EMP01
from _dados.conexao import Conexao


class Sistema(FrmMenu):

    def __init__(self, *args, **kwargs):
        super(Sistema, self).__init__(*args, **kwargs)
        pub.subscribe(self.my_listener, 'frameListener')
        dlg = SBLOG01(conexao=conn)
        # dlg = Login()
        dlg.ShowModal()

    def on_sair(self, event):
        conn.on_encerrar()
        exit()

    def my_listener(self, message, arg2=None):
        self.Show()

    def cad_pessoas(self, event):
        p = PRM01(None)
        p.Show()

    def cad_empresas(self, event):
        p = EMP01(None)
        p.Show()


class App(wx.App):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        frame = Sistema(None)
        frame.Show()


if __name__ == '__main__':
    conn = Conexao()
    App().MainLoop()
