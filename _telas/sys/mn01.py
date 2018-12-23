# -*- coding: utf-8 -*-

import wx
import wx.xrc
from wx.lib.pubsub import pub
from _telas.desingner.tela_menu import FrmMenu
from _telas.sys.sulog import SULOG
from _telas import *
import _dados.sys.ssgcon as conexao
import _regras.sys.ssglob as ssglob

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
        # Definições da Barra de Status
        self.StbMenu.SetStatusWidths([200, 300, 300])
        self.StbMenu.SetStatusText('Usuário:', 0)
        self.StbMenu.SetStatusText('Status da conexão: OFF', 1)
        self.StbMenu.SetStatusText(f'Empresa: ', 2)
        pub.subscribe(self.my_listener, 'frameListener')
        credencial = ssglob.SSGLOB()
        dlg = SULOG()
        dlg.ShowModal()

    def on_sair(self, event):
        conexao.conn.on_encerrar()
        exit()

    def my_listener(self, message, arg2=None):
        if not conexao.conn.user_name[0] == None:
            self.StbMenu.SetStatusText(f'Usuário: { ssglob.SSGLOB.nome_user}', 0)
            self.StbMenu.SetStatusText('Status da conexão: ON', 1)
            self.StbMenu.SetStatusText(f'Empresa: { ssglob.SSGLOB.nome_emp}', 2)
        self.Show()

    def ac_prm01(self, event):
        self.ac_chama_form('ARSLC')

    def ac_executar(self, event):
        self.ac_chama_form(self.tc_executar.Value)

    def ac_chama_form(self, tela=''):
        try:
            t = tela.lower() + '.' + tela.upper()
            exec('frame = ' + t + '(self)')
            exec('frame.Show()')
        except:
            self.StbMenu.SetStatusText(f'Erro ao chamar {self.tc_executar.Value}.', 2)


    def ac_emp01(self, event):
        self.ac_chama_form('EREMP')

    def ac_sobre(self, event):
        wx.MessageBox(f'Eu sou uma mensagem, {conexao.conn.user}', caption='Olá!!!', style=wx.OK | wx.ICON_INFORMATION)
