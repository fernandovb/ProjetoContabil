import pymysql
import _regras.sys.ssglob as ssglob

class Conexao(object):

    def on_conectar(self, host='localhost', user='', senha='', db='fvb_db', emp=0):
        self.user = user
        self.host = host
        self.db = db
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=senha, db=self.db)
            self.on_cursor()
            self.cursor.execute(f"SELECT usr_nome FROM sys_usuario WHERE usr_matricula = '{self.user}'")
            self.user_name = self.cursor.fetchone()
            if len(self.user_name) > 0:
                ssglob.SSGLOB.matricula = self.user
                ssglob.SSGLOB.nome_user = self.user_name[0]
                mensagem = 'Conectado em "localhost.fvb_db"'
                conectado = True
            else:
                mensagem = 'Usuário não registrado. Entre em contato com o administrador do sistema.'
                conectado = False
            self.cursor.execute(f"SELECT emp_nome_formal, emp_situacao, cfe_periodo, cfe_exercicio "
                                f"FROM sebd_eremp, sebd_epcfe "
                                f"WHERE emp_codigo = {str(emp)} AND cfe_empresa = {str(emp)}")
            self.empresa = self.cursor.fetchone()
            if len(self.empresa) > 0:
                ssglob.SSGLOB.empresa = emp
                ssglob.SSGLOB.nome_emp = self.empresa[0]
                ssglob.SSGLOB.situacao = self.empresa[1]
                ssglob.SSGLOB.periodo = self.empresa[2]
                ssglob.SSGLOB.exercicio = self.empresa[3]
            else:
                mensagem = 'Empresa não localizada. Favor verificar!'
                conectado = False
            self.off_cursor()
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

    def on_cursor(self):
        self.cursor = self.conn.cursor()

    def off_cursor(self):
        if self.cursor.connection is not None:
            self.cursor.close()

    def commit(self):
        self.conn.commit()

    def retorna_id(self):
        self.conn.insert_id()
        id = self.cursor.lastrowid
        self.cursor.execute('SELECT @@identity')
        cod = self.cursor.fetchone()
        return str(cod[0])

    def fc_gera_cod_doc(self, empresa, tipo_documento):
        documento = ''
        try:
            sql = f'SELECT ecdoc_numeracao ' \
                f'FROM sebd_ecdoc ' \
                f'WHERE ecdoc_empresa={empresa} ' \
                f'AND ecdoc_tipo_documento={tipo_documento}'
            self.on_cursor()
            self.cursor.execute(sql)
            doc = self.cursor.fetchone()[0] + 1
            documento = str(tipo_documento) + '0' * (8 - len(str(doc))) + str(doc)
            sql = f"UPDATE sebd_ecdoc " \
                f"SET ecdoc_numeracao={str(doc)} " \
                f"WHERE ecdoc_empresa={empresa} " \
                f"AND ecdoc_tipo_documento={tipo_documento}"
            self.cursor.execute(sql)
            self.commit()
            return documento
        except:
            return 0
        finally:
            self.off_cursor()
