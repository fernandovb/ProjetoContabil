from datetime import datetime


class PlanoContas:
    def __init__(self):
        self.plano_contas = []

    def __iter__(self):
        self.b = len(self.plano_contas)
        self.a = -1
        return self

    def __next__(self):
        self.a = + 1
        if self.a == self.b:
            raise StopIteration
        return self.plano_contas[self.a]

    def add_conta(self, codigo, nome, nivel):
        self.plano_contas.append([str(nivel), str(nome), codigo])

    def lista_contas(self):
        self.plano_contas.sort()
        for i in self.plano_contas:
            print('{0:6} - {1:30} - {2}'.format(i[2], i[1], i[0]))


class Slip:
    def __init__(self, **kwargs):
        self.codigo = kwargs.get('cod')
        self.descricao = kwargs.get('desc')
        self.dt_lcto = datetime.now().date()
        self.hr_lcto = datetime.now().time()
        self.periodo = datetime.now().month
        self.exercicio = datetime.now().year
        self.user = kwargs.get('user')
        self.valor = 0.00
        self.itens = []
        self.linha = 0

    def __str__(self):
        return '{0:12};{1:15};{2:2};{3:4};{4}'.format(self.codigo, self.descricao, self.periodo, self.exercicio,
                                                      self.valor)

    def add_item(self, DC='D', valor=0.00, desc=''):
        self.linha = self.linha + 1
        if (DC.upper() == 'D') or (DC.upper() == 'C'):
            self.itens.append([DC.upper(), self.linha, desc, valor])
            self.valor = self.valor + valor

    def equalizado(self):
        tot_d = 0.00
        tot_c = 0.00
        for i in self.itens:
            if i[0] == 'D':
                tot_d = tot_d + i[3]
            if i[0] == 'C':
                tot_c = tot_c + i[3]
        if tot_c == tot_d:
            return 'Slip equalizado: {:.2f}'.format(self.valor)
        else:
            return 'Slip divergente: D={:.2f} / C={:.2f}'.format(tot_d, tot_c)
