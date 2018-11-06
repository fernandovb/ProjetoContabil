# -*- coding: utf-8 -*-

import datetime
from wx.lib.pubsub import pub

from _telas.tela_login import FrmLogin


class SBLOG01(FrmLogin):

    def __init__(self, conexao, *args, **kwargs):
        super(SBLOG01, self).__init__(None, *args, *kwargs)
        self.conn = conexao

    def on_cancelar(self, event):
        exit()

    def on_login(self, event):
        conectado = self.conn.on_conectar(self.TxHost.Value, self.TxUser.Value, self.TxSenha.Value,
                                          self.TxDatabase.Value)
        if conectado[0]:
            pub.sendMessage('frameListener', message='show')
            self.Destroy()
        else:
            self.tb_mensagem.Value = self.tb_mensagem.Value + \
                                     '\n' + \
                                     str(datetime.datetime.today().hour) + ':' + \
                                     str(datetime.datetime.today().minute) + ':' + \
                                     str(datetime.datetime.today().second) + ': ' + \
                                     conectado[1]
