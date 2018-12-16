# -*- coding: utf-8 -*-

from datetime import datetime
from wx.lib.pubsub import pub

from _telas.desingner.tsulog import TSULOG
import _dados.dsulog01 as dados_log


class SULOG(TSULOG):

    def __init__(self, *args, **kwargs):
        super(SULOG, self).__init__(None, *args, *kwargs)

    def on_cancelar(self, event):
        exit()

    def on_login(self, event):
        hora = datetime.today()
        if str(self.tc_empresa.Value).isnumeric():
            self.usuario = dados_log.DSULOG(self.tc_host.Value,
                                            self.tc_user.Value,
                                            self.tc_senha.Value,
                                            self.tc_database.Value,
                                            int(self.tc_empresa.Value))
            if self.usuario.conectado[0]:
                pub.sendMessage('frameListener', message='show')
                self.Destroy()
            else:
                self.tb_mensagem.Value = self.tb_mensagem.Value + '\n' + \
                                         hora.strftime('%H:%M:%S: ') + \
                                         self.usuario.conectado[1]
        else:
            self.tb_mensagem.Value = self.tb_mensagem.Value + '\n' + \
                                     hora.strftime('%H:%M:%S: ') + \
                                     'Campo empresa deve conter apenas números.'
