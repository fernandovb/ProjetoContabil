# -*- coding: utf-8 -*-

from _dados.accl.difprp import DIFPRP
import _regras.sys.ssglob as ssglob


class RIFPRP:

    def __init__(self):
        pass

    def fc_busca_codigo(self, codigo):
        imob = DIFPRP()
        if imob.fc_busca_codigo(empresa=ssglob.SSGLOB.empresa, codigo=codigo) == True:
            self.empresa = ssglob.SSGLOB.empresa
            self.codigo = codigo
            self.descricao = imob.descricao
            self.medidor_1 = imob.medidor_1
            self.medidor_2 = imob.medidor_2
            return True
        else:
            return False
