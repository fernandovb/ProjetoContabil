# -*- coding: utf-8 -*-

import _dados.sys.ssgcon as conexao


class DSULOG:

    def __init__(self, host='localhost', user='', senha='', db='fvb_db', emp=0):
        self.conectado = conexao.conn.on_conectar(host=host, user=user, senha=senha, db=db, emp=int(emp))
