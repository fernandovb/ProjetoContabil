# -*- coding: utf-8 -*-

import _dados.ssgcon as conexao


class SULOG01:
    global conn

    def __init__(self, host='localhost', user='', senha='', db='fvb_db'):
        self.conectado = conexao.conn.on_conectar(host=host, user=user, senha=senha, db=db)
