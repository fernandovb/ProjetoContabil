# -*- coding: utf-8 -*-

import datetime
from wx.lib.pubsub import pub

from _telas.desingner.tela_login import FrmLogin
import _dados.dsulog01 as dados_log


class SULOG01(FrmLogin):

    def __init__(self, *args, **kwargs):
        super(SULOG01, self).__init__(None, *args, *kwargs)

    def on_cancelar(self, event):
        exit()

    def on_login(self, event):
        self.usuario = dados_log.SULOG01(self.TxHost.Value,
                                         self.TxUser.Value,
                                         self.TxSenha.Value,
                                         self.TxDatabase.Value)
        if self.usuario.conectado[0]:
            pub.sendMessage('frameListener', message='show')
            self.Destroy()
        else:
            self.tb_mensagem.Value = self.tb_mensagem.Value + \
                                     '\n' + \
                                     str(datetime.datetime.today().hour) + ':' + \
                                     str(datetime.datetime.today().minute) + ':' + \
                                     str(datetime.datetime.today().second) + ': ' + \
                                     self.usuario.conectado[1]
