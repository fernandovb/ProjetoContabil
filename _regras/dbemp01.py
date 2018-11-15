# -*- coding: utf-8 -*-

from _telas.tela_empresa import FrmEmpresa
import wx


class EMP01(FrmEmpresa):
    acao = 0  # 0-Consultar, 1-Inlcuir, 2-Alterar
    situacao = {'Ativo': 1, 'Análise': 2, 'Bloqueado': 3, 'Saneamento': 4, 'Cancelado': 9}

    def __init__(self, conexao, *args, **kwargs):
        super(EMP01, self).__init__(*args, **kwargs)
        self.tb_geral.EnableTool(wx.ID_FIND, True)
        self.tb_geral.EnableTool(wx.ID_ADD, True)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, False)
        self.tb_geral.EnableTool(wx.ID_ABORT, False)
        self.c_dados = {'emp_codigo': '',
                        'emp_situacao': '',
                        'emp_tipo': '',
                        'emp_nome_formal': '',
                        'emp_nome_alternativo': '',
                        'emp_logradouro': '',
                        'emp_numero': '',
                        'emp_bairro': '',
                        'emp_municipio': '',
                        'emp_estado': ''}
        self.lsocios = []
        self.gd_socios.SetColLabelValue(0, 'Empresa')
        self.gd_socios.SetColLabelValue(1, 'Codigo')
        self.gd_socios.SetColLabelValue(2, 'Situacao')
        self.gd_socios.SetColLabelValue(3, 'Nome do Sócio')
        self.gd_socios.SetColLabelValue(4, 'Cad.Federal')
        self.gd_socios.SetColLabelValue(5, 'Capital')
        self.gd_socios.SetColLabelValue(6, 'Quotas')
        self.gd_socios.SetColLabelValue(7, 'V.Quotas')
        self.conexao = conexao

    def ac_sair(self, event):
        self.Close()

    def ac_buscar(self, event):
        self.acao = 0
        try:
            self.conexao.on_cursor()
            sql = f"SELECT " \
                  f"emp_codigo, " \
                  f"emp_situacao, " \
                  f"emp_tipo, " \
                  f"emp_nome_formal, " \
                  f"emp_nome_alternativo, " \
                  f"emp_logradouro, " \
                  f"emp_numero, " \
                  f"emp_bairro, " \
                  f"emp_municipio, " \
                  f"emp_estado " \
                  f"FROM dba_empresa WHERE emp_codigo = " + \
                  str(self.tc_codigo.Value)
            self.conexao.cursor.execute(sql)
            busca = self.conexao.cursor.fetchone()
            i = 0
            for campo in self.c_dados:
                self.c_dados[campo] = busca[i]
                i += 1
            self.carrega_campos()
            self.conexao.off_cursor()
            # Carrega dados dos sócios
            self.soc_carregar()
            self.soc_atualiza_grade()
            # Exibe botões
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, True)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
        except:
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            wx.MessageBox(f'Erro ao carregar o registro {self.tc_codigo.Value}. \n{sql}',
                          caption='Erro', style=wx.OK | wx.ICON_ERROR)
        finally:
            self.conexao.off_cursor()

    def ac_adicionar(self, event):
        self.acao = 1
        self.tb_geral.EnableTool(wx.ID_FIND, False)
        self.tb_geral.EnableTool(wx.ID_ADD, False)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, True)
        self.tb_geral.EnableTool(wx.ID_ABORT, True)
        self.bt_soc_adicionar(True)
        self.bt_soc_editar(False)
        self.bt_soc_excluir(False)
        self.bt_soc_cancelar(False)
        self.limpa_campos()
        self.on_campos()

    def ac_editar(self, event):
        self.acao = 2
        self.tb_geral.EnableTool(wx.ID_FIND, False)
        self.tb_geral.EnableTool(wx.ID_ADD, False)
        self.tb_geral.EnableTool(wx.ID_EDIT, False)
        self.tb_geral.EnableTool(wx.ID_APPLY, True)
        self.tb_geral.EnableTool(wx.ID_ABORT, True)
        self.bt_soc_adicionar.Enable(True)
        self.bt_soc_editar.Enable(False)
        self.bt_soc_excluir.Enable(False)
        self.bt_soc_cancelar.Enable(False)
        self.on_campos()

    def ac_confirmar(self, event):
        self.tb_geral.EnableTool(wx.ID_FIND, True)
        self.tb_geral.EnableTool(wx.ID_ADD, True)
        self.tb_geral.EnableTool(wx.ID_EDIT, True)
        self.tb_geral.EnableTool(wx.ID_APPLY, False)
        self.tb_geral.EnableTool(wx.ID_ABORT, False)
        self.off_campos()
        self.muda_campos()
        if self.acao == 1:
            sql = "INSERT INTO dba_empresa (" \
                  "emp_situacao, " \
                  "emp_tipo, " \
                  "emp_nome_formal, " \
                  "emp_nome_alternativo, " \
                  "emp_logradouro, " \
                  "emp_numero, " \
                  "emp_bairro, " \
                  "emp_municipio, " \
                  "emp_estado) " \
                  "VALUES ("
            sql = sql + "'" + self.c_dados['emp_situacao'] + "', "
            sql = sql + "'" + self.c_dados['emp_tipo'] + "', "
            sql = sql + "'" + self.c_dados['emp_nome_formal'] + "', "
            sql = sql + "'" + self.c_dados['emp_nome_alternativo'] + "', "
            sql = sql + "'" + self.c_dados['emp_logradouro'] + "', "
            sql = sql + "'" + self.c_dados['emp_numero'] + "', "
            sql = sql + "'" + self.c_dados['emp_bairro'] + "', "
            sql = sql + "'" + self.c_dados['emp_municipio'] + "', "
            sql = sql + "'" + self.c_dados['emp_estado'] + "') "
        elif self.acao == 2:
            sql = 'UPDATE dba_empresa SET '
            sql = sql + 'emp_tipo = ' + "'" + self.c_dados['emp_tipo'] + "', "
            sql = sql + 'emp_situacao = ' + "'" + self.c_dados['emp_situacao'] + "', "
            sql = sql + 'emp_nome_formal = ' + "'" + self.c_dados['emp_nome_formal'] + "', "
            sql = sql + 'emp_nome_alternativo = ' + "'" + self.c_dados['emp_nome_alternativo'] + "', "
            sql = sql + 'emp_logradouro = ' + "'" + self.c_dados['emp_logradouro'] + "', "
            sql = sql + 'emp_numero = ' + "'" + self.c_dados['emp_numero'] + "', "
            sql = sql + 'emp_bairro = ' + "'" + self.c_dados['emp_bairro'] + "', "
            sql = sql + 'emp_municipio = ' + "'" + self.c_dados['emp_municipio'] + "', "
            sql = sql + 'emp_estado = ' + "'" + self.c_dados['emp_estado'] + "' "
            sql = sql + 'WHERE ' + self.tc_codigo.Value
        try:
            self.conexao.on_cursor()
            self.conexao.cursor.execute(sql)
            if self.acao == 1:
                self.tc_codigo.Value = self.conexao.retorna_id()
            self.conexao.commit()
        except:
            wx.MessageBox(f"Erro ao salvar o registro {self.tc_codigo.Value}. \n{sql}",
                          caption='Erro', style=wx.OK | wx.ICON_ERROR)
        finally:
            self.conexao.off_cursor()

    def ac_cancelar(self, event):
        if self.acao == 1:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
        elif self.acao == 2:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, True)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
        elif self.acao == 0:
            self.tb_geral.EnableTool(wx.ID_FIND, True)
            self.tb_geral.EnableTool(wx.ID_ADD, True)
            self.tb_geral.EnableTool(wx.ID_EDIT, False)
            self.tb_geral.EnableTool(wx.ID_APPLY, False)
            self.tb_geral.EnableTool(wx.ID_ABORT, False)
            self.limpa_campos()
        self.acao = 0
        self.off_campos()
        self.carrega_campos()

    def on_campos(self):
        self.tc_codigo.Enable(False)
        self.cb_tipo.Enable(True)
        self.cb_situacao.Enable(True)
        self.tc_nome_formal.Enable(True)
        self.tc_nome_alternativo.Enable(True)
        self.tc_logradouro.Enable(True)
        self.tc_numero.Enable(True)
        self.tc_bairro.Enable(True)
        self.tc_municipio.Enable(True)
        self.cb_estado.Enable(True)

    def off_campos(self):
        self.tc_codigo.Enable(True)
        self.cb_tipo.Enable(False)
        self.cb_situacao.Enable(False)
        self.tc_nome_formal.Enable(False)
        self.tc_nome_alternativo.Enable(False)
        self.tc_logradouro.Enable(False)
        self.tc_numero.Enable(False)
        self.tc_bairro.Enable(False)
        self.tc_municipio.Enable(False)
        self.cb_estado.Enable(False)

    def carrega_campos(self):
        self.cb_tipo.Value = self.c_dados['emp_tipo']
        self.cb_situacao.Value = loc_sitacao(self.situacao, self.c_dados['emp_situacao'])
        self.tc_nome_formal.Value = self.c_dados['emp_nome_formal']
        self.tc_nome_alternativo.Value = self.c_dados['emp_nome_alternativo']
        self.tc_logradouro.Value = self.c_dados['emp_logradouro']
        self.tc_numero.Value = self.c_dados['emp_numero']
        self.tc_bairro.Value = self.c_dados['emp_bairro']
        self.tc_municipio.Value = self.c_dados['emp_municipio']
        self.cb_estado.Value = self.c_dados['emp_estado']

    def limpa_campos(self):
        self.tc_codigo.Value = ''
        self.cb_tipo.Value = ''
        self.cb_situacao.Value = ''
        self.tc_nome_formal.Value = ''
        self.tc_nome_alternativo.Value = ''
        self.tc_logradouro.Value = ''
        self.tc_numero.Value = ''
        self.tc_bairro.Value = ''
        self.tc_municipio.Value = ''
        self.cb_estado.Value = ''

    def muda_campos(self):
        self.c_dados['emp_codigo'] = self.tc_codigo.Value
        self.c_dados['emp_tipo'] = self.cb_tipo.Value
        self.c_dados['emp_situacao'] = self.situacao[self.cb_situacao.Value]
        self.c_dados['emp_nome_formal'] = self.tc_nome_formal.Value
        self.c_dados['emp_nome_alternativo'] = self.tc_nome_alternativo.Value
        self.c_dados['emp_logradouro'] = self.tc_logradouro.Value
        self.c_dados['emp_numero'] = self.tc_numero.Value
        self.c_dados['emp_bairro'] = self.tc_bairro.Value
        self.c_dados['emp_municipio'] = self.tc_municipio.Value
        self.c_dados['emp_estado'] = self.cb_estado.Value

    def soc_consultar(self):
        pass

    def soc_nova_linha(self, valor):
        campo = valor
        self.gd_socios.AppendRows(1)
        linha = self.gd_socios.GetNumberRows() - 1
        for i in range(8):
            self.gd_socios.SetCellValue(linha, i, str(campo[i]))

    def soc_adicionar(self, event):
        self.m_notebook2.ChangeSelection(1)
        self.bt_soc_adicionar.Enable(False)
        self.bt_soc_cancelar.Enable(True)
        self.bt_soc_editar.Enable(True)
        self.bt_soc_excluir.Enable(True)

    def soc_editar(self, event):
        pass

    def soc_excluir(self, event):
        pass

    def soc_cancelar(self, event):
        self.m_notebook2.ChangeSelection(0)

    def soc_carregar(self):
        try:
            self.conexao.on_cursor()
            sql = 'SELECT * FROM dba_emp_socio WHERE esc_empresa = ' + str(self.tc_codigo.Value)
            self.conexao.cursor.execute(sql)
            socios = self.conexao.cursor.fetchall()
            if len(socios) > 0:
                for i in socios:
                    socio = SOC01(empresa=i[0],
                                  codigo=i[1],
                                  situacao=i[2],
                                  nome=i[3],
                                  federal=i[4],
                                  capital=float(i[5]),
                                  quotas=float(i[6]),
                                  val_quot=float(i[7]))
                    self.lsocios.append(socio)
        except:
            wx.MessageBox(f"Erro ao carregar os socios da empresa {self.tc_codigo.Value}. \n{sql}",
                          caption='Erro', style=wx.OK | wx.ICON_ERROR)
        finally:
            self.conexao.off_cursor()

    def soc_atualiza_grade(self):
        #for i in range(len(self.lsocios)):
        linha = 0
        for socio in self.lsocios:
            self.gd_socios.AppendRows(1)
            self.gd_socios.SetCellValue(linha, 0, str(socio.empresa))
            self.gd_socios.SetCellValue(linha, 1, str(socio.codigo))
            self.gd_socios.SetCellValue(linha, 2, str(socio.situacao))
            self.gd_socios.SetCellValue(linha, 3, str(socio.nome))
            self.gd_socios.SetCellValue(linha, 4, str(socio.federal))
            self.gd_socios.SetCellValue(linha, 5, str(socio.capital))
            self.gd_socios.SetCellValue(linha, 6, str(socio.quotas))
            self.gd_socios.SetCellValue(linha, 7, str(socio.val_quotas))
            linha += 1

class SOC01:
    def __init__(self, empresa, codigo, situacao=1, nome='', federal='', capital=None, quotas=None,
                 val_quot=None):
        self.empresa = int(empresa)
        self.codigo = int(codigo)
        self.situacao = int(situacao)
        self.nome = str(nome)
        self.federal = str(federal)
        self.capital = float(capital)
        self.quotas = float(quotas)
        self.val_quotas = float(val_quot)

    def ac_adicionar_socio(self):
        pass

    def ac_excluir_socio(self):
        self.situacao = 9

def loc_sitacao(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i
