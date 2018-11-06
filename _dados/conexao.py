import pymysql


class Conexao(object):

    def on_conectar(self, host='localhost', user='', senha='', db='fvb_db'):
        self.user = user
        self.host = host
        self.db = db
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=senha, db=self.db)
            self.cursor = self.conn.cursor()
            mensagem = 'Conectado em "localhost.fvb_db"'
            conectado = True
        except:
            mensagem = 'Erro ao conectar com o banco de dados!'
            conectado = False
        finally:
            return [conectado, mensagem]

    def on_encerrar(self):
        try:
            self.conn.close()
        except:
            pass
