import pymysql
import sys


class Conexao:
    def __init__(self, user, senha):
        self.host = 'localhost'
        self.user = user
        self.senha = senha
        self.db = 'sys'

    def conectar(self):
        c = False
        try:
            self.db_cnn = pymysql.connect(host=self.host, user=self.user, password=self.senha, db=self.db)
            c = True
        except:
            c = False
        finally:
            return c


u = str(input('Usuário: '))
s = str(input('Senha: '))
c = Conexao(u, s)
if c.conectar():
    print('Conexão bem sucedida!')
else:
    print('Erro na conexão.')
    sys.exit()

while True:
    print('''
    1 - Cadastro
    2 - Relatório
    
    9 - Sair
    ''')
    o = str(input('Digite uma opção: '))
    if o == '9':
        break
    if o == '1':
        import cadastro.py
