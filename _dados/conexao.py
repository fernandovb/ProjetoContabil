import pymysql


class Conexao(object):

    def on_conectar(self, host='localhost', user='', senha='', db='fvb_db'):
        self.user = user
        self.host = host
        self.db = db
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=senha, db=self.db)
            self.on_cursor()
            self.cursor.execute(f"SELECT usr_nome FROM sys_usuario WHERE usr_matricula = '{self.user}'")
            self.user_name = self.cursor.fetchone()
            if not self.user_name == None:
                mensagem = 'Conectado em "localhost.fvb_db"'
                conectado = True
            else:
                mensagem = 'Usuário não registrado. Entre em contato com o administrador do sistema.'
                conectado = False
        except:
            mensagem = 'Erro ao conectar com o banco de dados!'
            conectado = False
        finally:
            self.off_cursor()
            return [conectado, mensagem]

    def on_encerrar(self):
        try:
            self.conn.close()
        except:
            pass

    def on_cursor(self):
        self.cursor = self.conn.cursor()

    def off_cursor(self):
        self.cursor.close()

    def commit(self):
        self.conn.commit()

    def retorna_id(self):
        self.conn.insert_id()
        id = self.cursor.lastrowid
        self.cursor.execute('SELECT @@identity')
        cod = self.cursor.fetchone()
        return str(cod[0])
