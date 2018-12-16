# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class TEREMP
###########################################################################

class TEREMP ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cadastro de Empresas", pos = wx.DefaultPosition, size = wx.Size( 1064,730 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.tb_geral = self.CreateToolBar( 0, wx.ID_ANY ) 
		self.bt_buscar = self.tb_geral.AddLabelTool( wx.ID_FIND, u"Localizar registro", wx.Bitmap( u"icons/ac_buscar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.bt_adicionar = self.tb_geral.AddLabelTool( wx.ID_ADD, u"Novo", wx.Bitmap( u"icons/ac_adicionar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.bt_editar = self.tb_geral.AddLabelTool( wx.ID_EDIT, u"Alterar registro", wx.Bitmap( u"icons/ac_editar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tb_geral.AddSeparator()
		
		self.bt_confirmar = self.tb_geral.AddLabelTool( wx.ID_APPLY, u"Salvar modificações", wx.Bitmap( u"icons/ac_confirmar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.bt_cancelar = self.tb_geral.AddLabelTool( wx.ID_ABORT, u"Cancelar alterações", wx.Bitmap( u"icons/ac_cancelar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tb_geral.AddSeparator()
		
		self.bt_sair = self.tb_geral.AddLabelTool( wx.ID_CLOSE, u"tool", wx.Bitmap( u"icons/ac_sair_32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tb_geral.Realize() 
		
		lay_corpo = wx.BoxSizer( wx.VERTICAL )
		
		lay_cabecalho = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lb_codigo = wx.StaticText( self, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 60,26 ), 0 )
		self.lb_codigo.Wrap( -1 )
		lay_cabecalho.Add( self.lb_codigo, 0, wx.ALL, 5 )
		
		self.tc_codigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lay_cabecalho.Add( self.tc_codigo, 0, wx.ALL, 5 )
		
		self.lb_nome = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,26 ), 0 )
		self.lb_nome.Wrap( -1 )
		self.lb_nome.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		lay_cabecalho.Add( self.lb_nome, 0, wx.ALL, 5 )
		
		self.lb_tipo = wx.StaticText( self, wx.ID_ANY, u"Tipo:", wx.DefaultPosition, wx.Size( 100,26 ), wx.ALIGN_RIGHT )
		self.lb_tipo.Wrap( -1 )
		lay_cabecalho.Add( self.lb_tipo, 0, wx.ALL, 5 )
		
		cb_tipoChoices = [ u"PF", u"PJ" ]
		self.cb_tipo = wx.ComboBox( self, wx.ID_ANY, u"PF", wx.DefaultPosition, wx.DefaultSize, cb_tipoChoices, 0 )
		self.cb_tipo.Enable( False )
		
		lay_cabecalho.Add( self.cb_tipo, 0, wx.ALL, 5 )
		
		self.lb_situacao = wx.StaticText( self, wx.ID_ANY, u"Situação:", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
		self.lb_situacao.Wrap( -1 )
		lay_cabecalho.Add( self.lb_situacao, 0, wx.ALL, 5 )
		
		cb_situacaoChoices = [ u"Ativo", u"Análise", u"Bloqueado", u"Saneamento", u"Cancelado" ]
		self.cb_situacao = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_situacaoChoices, 0 )
		self.cb_situacao.Enable( False )
		
		lay_cabecalho.Add( self.cb_situacao, 0, wx.ALL, 5 )
		
		
		lay_corpo.Add( lay_cabecalho, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		lay_guias = wx.BoxSizer( wx.VERTICAL )
		
		self.nb_dados = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_dados_basicos = wx.Panel( self.nb_dados, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		lay_dados_basicos = wx.BoxSizer( wx.VERTICAL )
		
		lay_basico_dados1 = wx.BoxSizer( wx.HORIZONTAL )
		
		lay_cadastrais = wx.StaticBoxSizer( wx.StaticBox( self.pn_dados_basicos, wx.ID_ANY, u"Informações Cadastrais" ), wx.HORIZONTAL )
		
		lay_cad_lab1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lb_nome_formal = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Nome formal:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_nome_formal.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_nome_formal, 0, wx.ALL, 5 )
		
		self.lb_nome_alternativo = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Nome alternativo:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_nome_alternativo.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_nome_alternativo, 0, wx.ALL, 5 )
		
		self.lb_logradouro = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Logradouro:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_logradouro.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_logradouro, 0, wx.ALL, 5 )
		
		self.lb_numero = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Número:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_numero.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_numero, 0, wx.ALL, 5 )
		
		self.lb_bairro = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Bairro:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_bairro.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_bairro, 0, wx.ALL, 5 )
		
		self.lb_municipio = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Município:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_municipio.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_municipio, 0, wx.ALL, 5 )
		
		self.lb_estado = wx.StaticText( lay_cadastrais.GetStaticBox(), wx.ID_ANY, u"Estado:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_estado.Wrap( -1 )
		lay_cad_lab1.Add( self.lb_estado, 0, wx.ALL, 5 )
		
		
		lay_cadastrais.Add( lay_cad_lab1, 0, wx.EXPAND, 5 )
		
		lay_cad_text1 = wx.BoxSizer( wx.VERTICAL )
		
		self.tc_nome_formal = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_nome_formal.Enable( False )
		
		lay_cad_text1.Add( self.tc_nome_formal, 0, wx.ALL, 5 )
		
		self.tc_nome_alternativo = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_nome_alternativo.Enable( False )
		
		lay_cad_text1.Add( self.tc_nome_alternativo, 0, wx.ALL, 5 )
		
		self.tc_logradouro = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_logradouro.Enable( False )
		
		lay_cad_text1.Add( self.tc_logradouro, 0, wx.ALL, 5 )
		
		self.tc_numero = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,26 ), 0 )
		self.tc_numero.Enable( False )
		
		lay_cad_text1.Add( self.tc_numero, 0, wx.ALL, 5 )
		
		self.tc_bairro = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,26 ), 0 )
		self.tc_bairro.Enable( False )
		
		lay_cad_text1.Add( self.tc_bairro, 0, wx.ALL, 5 )
		
		self.tc_municipio = wx.TextCtrl( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_municipio.Enable( False )
		
		lay_cad_text1.Add( self.tc_municipio, 0, wx.ALL, 5 )
		
		cb_estadoChoices = [ u"MT", u"MS", u"MG", u"RJ", u"RG", u"RN", u"RR", u"ES", u"SP", u"SC", u"PR", u"PI", u"BA" ]
		self.cb_estado = wx.ComboBox( lay_cadastrais.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), cb_estadoChoices, 0 )
		self.cb_estado.Enable( False )
		
		lay_cad_text1.Add( self.cb_estado, 0, wx.ALL, 5 )
		
		
		lay_cadastrais.Add( lay_cad_text1, 1, wx.EXPAND, 5 )
		
		
		lay_basico_dados1.Add( lay_cadastrais, 0, wx.EXPAND|wx.TOP, 0 )
		
		lay_caracteristicas = wx.StaticBoxSizer( wx.StaticBox( self.pn_dados_basicos, wx.ID_ANY, u"Características" ), wx.VERTICAL )
		
		lay_carac_lab1 = wx.BoxSizer( wx.VERTICAL )
		
		
		lay_caracteristicas.Add( lay_carac_lab1, 0, wx.EXPAND, 5 )
		
		lay_carac_text1 = wx.BoxSizer( wx.VERTICAL )
		
		
		lay_caracteristicas.Add( lay_carac_text1, 0, wx.EXPAND, 5 )
		
		
		lay_basico_dados1.Add( lay_caracteristicas, 1, wx.EXPAND, 5 )
		
		
		lay_dados_basicos.Add( lay_basico_dados1, 1, wx.EXPAND, 5 )
		
		lay_registros = wx.StaticBoxSizer( wx.StaticBox( self.pn_dados_basicos, wx.ID_ANY, u"Registros" ), wx.HORIZONTAL )
		
		lay_reg_lab1 = wx.BoxSizer( wx.VERTICAL )
		
		
		lay_registros.Add( lay_reg_lab1, 0, wx.EXPAND, 5 )
		
		lay_reg_lab2 = wx.BoxSizer( wx.VERTICAL )
		
		
		lay_registros.Add( lay_reg_lab2, 1, wx.EXPAND, 5 )
		
		
		lay_dados_basicos.Add( lay_registros, 1, wx.EXPAND, 5 )
		
		
		self.pn_dados_basicos.SetSizer( lay_dados_basicos )
		self.pn_dados_basicos.Layout()
		lay_dados_basicos.Fit( self.pn_dados_basicos )
		self.nb_dados.AddPage( self.pn_dados_basicos, u"Dados Básicos", True )
		self.pn_comunicacao = wx.Panel( self.nb_dados, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_comunicacao = wx.BoxSizer( wx.VERTICAL )
		
		lay_contatos = wx.StaticBoxSizer( wx.StaticBox( self.pn_comunicacao, wx.ID_ANY, u"Contatos" ), wx.VERTICAL )
		
		
		lay_comunicacao.Add( lay_contatos, 1, wx.EXPAND|wx.TOP, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		lay_email = wx.StaticBoxSizer( wx.StaticBox( self.pn_comunicacao, wx.ID_ANY, u"Correio eletrônico" ), wx.VERTICAL )
		
		
		bSizer8.Add( lay_email, 1, wx.EXPAND, 5 )
		
		lay_enderecos = wx.StaticBoxSizer( wx.StaticBox( self.pn_comunicacao, wx.ID_ANY, u"Endereços" ), wx.VERTICAL )
		
		
		bSizer8.Add( lay_enderecos, 1, wx.EXPAND, 5 )
		
		
		lay_comunicacao.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.pn_comunicacao.SetSizer( lay_comunicacao )
		self.pn_comunicacao.Layout()
		lay_comunicacao.Fit( self.pn_comunicacao )
		self.nb_dados.AddPage( self.pn_comunicacao, u"Comunicação", False )
		self.pn_fiscal = wx.Panel( self.nb_dados, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nb_dados.AddPage( self.pn_fiscal, u"Dados Fiscais", False )
		self.pn_socios = wx.Panel( self.nb_dados, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_socios = wx.BoxSizer( wx.VERTICAL )
		
		self.pn_lista_socios = wx.Panel( self.pn_socios, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		lay_total = wx.BoxSizer( wx.VERTICAL )
		
		lay_label = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lb_quotas = wx.StaticText( self.pn_lista_socios, wx.ID_ANY, u"Total de Quotas", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_CENTRE )
		self.lb_quotas.Wrap( -1 )
		lay_label.Add( self.lb_quotas, 0, wx.ALL, 5 )
		
		self.lb_capital = wx.StaticText( self.pn_lista_socios, wx.ID_ANY, u"Capital Total", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_CENTRE )
		self.lb_capital.Wrap( -1 )
		lay_label.Add( self.lb_capital, 0, wx.ALL, 5 )
		
		
		lay_total.Add( lay_label, 1, wx.EXPAND, 5 )
		
		lay_campos = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tc_quotas = wx.TextCtrl( self.pn_lista_socios, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), wx.TE_RIGHT )
		lay_campos.Add( self.tc_quotas, 0, wx.ALL, 5 )
		
		self.tc_capital = wx.TextCtrl( self.pn_lista_socios, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), wx.TE_RIGHT )
		lay_campos.Add( self.tc_capital, 0, wx.ALL, 5 )
		
		
		lay_total.Add( lay_campos, 1, wx.EXPAND, 5 )
		
		
		bSizer20.Add( lay_total, 0, wx.EXPAND, 5 )
		
		lay_tabela = wx.BoxSizer( wx.VERTICAL )
		
		self.gd_socios = wx.grid.Grid( self.pn_lista_socios, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gd_socios.CreateGrid( 0, 8 )
		self.gd_socios.EnableEditing( False )
		self.gd_socios.EnableGridLines( False )
		self.gd_socios.EnableDragGridSize( False )
		self.gd_socios.SetMargins( 0, 0 )
		
		# Columns
		self.gd_socios.SetColSize( 0, 50 )
		self.gd_socios.SetColSize( 1, 50 )
		self.gd_socios.SetColSize( 2, 90 )
		self.gd_socios.SetColSize( 3, 400 )
		self.gd_socios.SetColSize( 4, 120 )
		self.gd_socios.SetColSize( 5, 100 )
		self.gd_socios.SetColSize( 6, 100 )
		self.gd_socios.SetColSize( 7, 100 )
		self.gd_socios.EnableDragColMove( False )
		self.gd_socios.EnableDragColSize( False )
		self.gd_socios.SetColLabelSize( 30 )
		self.gd_socios.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gd_socios.EnableDragRowSize( True )
		self.gd_socios.SetRowLabelSize( 30 )
		self.gd_socios.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gd_socios.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_tabela.Add( self.gd_socios, 1, wx.EXPAND, 5 )
		
		
		bSizer20.Add( lay_tabela, 1, wx.EXPAND, 5 )
		
		
		self.pn_lista_socios.SetSizer( bSizer20 )
		self.pn_lista_socios.Layout()
		bSizer20.Fit( self.pn_lista_socios )
		lay_socios.Add( self.pn_lista_socios, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pn_form_socios = wx.Panel( self.pn_socios, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pn_form_socios.Hide()
		
		lay_form_soc = wx.BoxSizer( wx.HORIZONTAL )
		
		lay_label_soc1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lb_empresa = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Empresa:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_empresa.Wrap( -1 )
		lay_label_soc1.Add( self.lb_empresa, 0, wx.ALL, 5 )
		
		self.lb_soc_codigo = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_codigo.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_codigo, 0, wx.ALL, 5 )
		
		self.lb_soc_situacao = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Situação:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_situacao.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_situacao, 0, wx.ALL, 5 )
		
		self.lb_soc_nome = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Nome do Sócio:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_nome.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_nome, 0, wx.ALL, 5 )
		
		self.lc_soc_federal = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Cadastro Federal:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lc_soc_federal.Wrap( -1 )
		lay_label_soc1.Add( self.lc_soc_federal, 0, wx.ALL, 5 )
		
		self.lb_soc_capital = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Capital Integralizado:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_capital.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_capital, 0, wx.ALL, 5 )
		
		self.lb_soc_quotas = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Qtde. de Quotas:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_quotas.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_quotas, 0, wx.ALL, 5 )
		
		self.lb_soc_vquota = wx.StaticText( self.pn_form_socios, wx.ID_ANY, u"Valor da Quota:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_soc_vquota.Wrap( -1 )
		lay_label_soc1.Add( self.lb_soc_vquota, 0, wx.ALL, 5 )
		
		
		lay_form_soc.Add( lay_label_soc1, 0, wx.EXPAND, 5 )
		
		lay_text_soc1 = wx.BoxSizer( wx.VERTICAL )
		
		self.tc_soc_empresa = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_soc_empresa.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_empresa, 0, wx.ALL, 5 )
		
		self.tc_soc_codigo = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_soc_codigo.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_codigo, 0, wx.ALL, 5 )
		
		cb_soc_situacaoChoices = [ u"Ativo", u"Análise", u"Bloqueado", u"Saneamento", u"Cancelado" ]
		self.cb_soc_situacao = wx.ComboBox( self.pn_form_socios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,26 ), cb_soc_situacaoChoices, 0 )
		self.cb_soc_situacao.Enable( False )
		
		lay_text_soc1.Add( self.cb_soc_situacao, 0, wx.ALL, 5 )
		
		self.tc_soc_nome = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_soc_nome.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_nome, 0, wx.ALL, 5 )
		
		self.tc_soc_federal = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,26 ), 0 )
		self.tc_soc_federal.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_federal, 0, wx.ALL, 5 )
		
		self.tc_soc_capital = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		self.tc_soc_capital.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_capital, 0, wx.ALL, 5 )
		
		self.tc_soc_quotas = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		self.tc_soc_quotas.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_quotas, 0, wx.ALL, 5 )
		
		self.tc_soc_vquota = wx.TextCtrl( self.pn_form_socios, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		self.tc_soc_vquota.Enable( False )
		
		lay_text_soc1.Add( self.tc_soc_vquota, 0, wx.ALL, 5 )
		
		
		lay_form_soc.Add( lay_text_soc1, 1, wx.EXPAND, 5 )
		
		
		self.pn_form_socios.SetSizer( lay_form_soc )
		self.pn_form_socios.Layout()
		lay_form_soc.Fit( self.pn_form_socios )
		lay_socios.Add( self.pn_form_socios, 1, wx.EXPAND |wx.ALL, 5 )
		
		lay_botao = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bt_soc_consultar = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bt_soc_consultar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_consultar.Enable( False )
		
		lay_botao.Add( self.bt_soc_consultar, 0, wx.ALL, 5 )
		
		self.bt_soc_adicionar = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bt_soc_adicionar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_adicionar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_adicionar.SetDefault() 
		self.bt_soc_adicionar.Enable( False )
		
		lay_botao.Add( self.bt_soc_adicionar, 0, wx.ALL, 5 )
		
		self.bt_soc_editar = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_editar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_BOTTOM )
		
		self.bt_soc_editar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_editar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_editar.Enable( False )
		
		lay_botao.Add( self.bt_soc_editar, 0, wx.ALL, 5 )
		
		self.bt_soc_excluir = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bt_soc_excluir.SetBitmapDisabled( wx.Bitmap( u"icons/ac_lixeira_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_excluir.Enable( False )
		
		lay_botao.Add( self.bt_soc_excluir, 0, wx.ALL, 5 )
		
		self.bt_soc_confirmar = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bt_soc_confirmar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_confirmar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_confirmar.Enable( False )
		
		lay_botao.Add( self.bt_soc_confirmar, 0, wx.ALL, 5 )
		
		self.bt_soc_cancelar = wx.BitmapButton( self.pn_socios, wx.ID_ANY, wx.Bitmap( u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bt_soc_cancelar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_cancelar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_soc_cancelar.Enable( False )
		
		lay_botao.Add( self.bt_soc_cancelar, 0, wx.ALL, 5 )
		
		
		lay_socios.Add( lay_botao, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		self.pn_socios.SetSizer( lay_socios )
		self.pn_socios.Layout()
		lay_socios.Fit( self.pn_socios )
		self.nb_dados.AddPage( self.pn_socios, u"Quadro Societário", False )
		
		lay_guias.Add( self.nb_dados, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		lay_corpo.Add( lay_guias, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( lay_corpo )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.ac_buscar, id = self.bt_buscar.GetId() )
		self.Bind( wx.EVT_TOOL, self.ac_adicionar, id = self.bt_adicionar.GetId() )
		self.Bind( wx.EVT_TOOL, self.ac_editar, id = self.bt_editar.GetId() )
		self.Bind( wx.EVT_TOOL, self.ac_confirmar, id = self.bt_confirmar.GetId() )
		self.Bind( wx.EVT_TOOL, self.ac_cancelar, id = self.bt_cancelar.GetId() )
		self.Bind( wx.EVT_TOOL, self.ac_sair, id = self.bt_sair.GetId() )
		self.gd_socios.Bind( wx.EVT_LEFT_DCLICK, self.soc_consultar )
		self.bt_soc_consultar.Bind( wx.EVT_BUTTON, self.soc_consultar )
		self.bt_soc_adicionar.Bind( wx.EVT_BUTTON, self.soc_adicionar )
		self.bt_soc_editar.Bind( wx.EVT_BUTTON, self.soc_editar )
		self.bt_soc_excluir.Bind( wx.EVT_BUTTON, self.soc_excluir )
		self.bt_soc_confirmar.Bind( wx.EVT_BUTTON, self.soc_confirmar )
		self.bt_soc_cancelar.Bind( wx.EVT_BUTTON, self.soc_cancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ac_buscar( self, event ):
		event.Skip()
	
	def ac_adicionar( self, event ):
		event.Skip()
	
	def ac_editar( self, event ):
		event.Skip()
	
	def ac_confirmar( self, event ):
		event.Skip()
	
	def ac_cancelar( self, event ):
		event.Skip()
	
	def ac_sair( self, event ):
		event.Skip()
	
	def soc_consultar( self, event ):
		event.Skip()
	
	
	def soc_adicionar( self, event ):
		event.Skip()
	
	def soc_editar( self, event ):
		event.Skip()
	
	def soc_excluir( self, event ):
		event.Skip()
	
	def soc_confirmar( self, event ):
		event.Skip()
	
	def soc_cancelar( self, event ):
		event.Skip()
	

