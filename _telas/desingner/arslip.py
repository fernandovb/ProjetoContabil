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
## Class TARSLIP01
###########################################################################

class TARSLIP01 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lançamento Contábil", pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.STATIC_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.tb_geral = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.tb_geral.Realize() 
		
		lay_body = wx.BoxSizer( wx.VERTICAL )
		
		lay_options = wx.BoxSizer( wx.VERTICAL )
		
		
		lay_body.Add( lay_options, 1, wx.EXPAND, 5 )
		
		lay_slip = wx.BoxSizer( wx.VERTICAL )
		
		lay_cabecalho = wx.BoxSizer( wx.HORIZONTAL )
		
		lay_cabec_rotulo_01 = wx.BoxSizer( wx.VERTICAL )
		
		self.lb_empresa = wx.StaticText( self, wx.ID_ANY, u"Empresa:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_empresa.Wrap( -1 )
		lay_cabec_rotulo_01.Add( self.lb_empresa, 0, wx.ALL, 5 )
		
		self.lb_documento = wx.StaticText( self, wx.ID_ANY, u"Número lançamento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_documento.Wrap( -1 )
		lay_cabec_rotulo_01.Add( self.lb_documento, 0, wx.ALL, 5 )
		
		self.lb_dt_criacao = wx.StaticText( self, wx.ID_ANY, u"Criado em:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_dt_criacao.Wrap( -1 )
		lay_cabec_rotulo_01.Add( self.lb_dt_criacao, 0, wx.ALL, 5 )
		
		self.lb_dt_movimento = wx.StaticText( self, wx.ID_ANY, u"Data do movimento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_dt_movimento.Wrap( -1 )
		lay_cabec_rotulo_01.Add( self.lb_dt_movimento, 0, wx.ALL, 5 )
		
		
		lay_cabecalho.Add( lay_cabec_rotulo_01, 0, wx.EXPAND, 5 )
		
		lay_cabec_campos_01 = wx.BoxSizer( wx.VERTICAL )
		
		self.tc_empresa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		lay_cabec_campos_01.Add( self.tc_empresa, 0, wx.ALL, 5 )
		
		self.tc_num_documento = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		lay_cabec_campos_01.Add( self.tc_num_documento, 0, wx.ALL, 5 )
		
		
		lay_cabecalho.Add( lay_cabec_campos_01, 1, wx.EXPAND, 5 )
		
		lay_cabec_rotulo_02 = wx.BoxSizer( wx.VERTICAL )
		
		self.lb_periodo = wx.StaticText( self, wx.ID_ANY, u"Período:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_periodo.Wrap( -1 )
		lay_cabec_rotulo_02.Add( self.lb_periodo, 0, wx.ALL, 5 )
		
		self.lb_exercicio = wx.StaticText( self, wx.ID_ANY, u"Exercício:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_exercicio.Wrap( -1 )
		lay_cabec_rotulo_02.Add( self.lb_exercicio, 0, wx.ALL, 5 )
		
		self.lb_usuario = wx.StaticText( self, wx.ID_ANY, u"Criado por:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_usuario.Wrap( -1 )
		lay_cabec_rotulo_02.Add( self.lb_usuario, 0, wx.ALL, 5 )
		
		
		lay_cabecalho.Add( lay_cabec_rotulo_02, 0, wx.EXPAND, 5 )
		
		lay_cabec_campos_02 = wx.BoxSizer( wx.VERTICAL )
		
		self.tc_periodo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_periodo.Enable( False )
		
		lay_cabec_campos_02.Add( self.tc_periodo, 0, wx.ALL, 5 )
		
		self.tc_exercicio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), 0 )
		lay_cabec_campos_02.Add( self.tc_exercicio, 0, wx.ALL, 5 )
		
		self.tc_usuario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,26 ), 0 )
		lay_cabec_campos_02.Add( self.tc_usuario, 0, wx.ALL, 5 )
		
		
		lay_cabecalho.Add( lay_cabec_campos_02, 1, wx.EXPAND, 5 )
		
		
		lay_slip.Add( lay_cabecalho, 0, wx.EXPAND, 5 )
		
		lay_detalhes = wx.BoxSizer( wx.VERTICAL )
		
		self.nb_detalhes = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_partidas = wx.Panel( self.nb_detalhes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pn_partidas.Enable( False )
		
		lay_partidas = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid3 = wx.grid.Grid( self.pn_partidas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_partidas.Add( self.m_grid3, 0, wx.EXPAND, 5 )
		
		
		self.pn_partidas.SetSizer( lay_partidas )
		self.pn_partidas.Layout()
		lay_partidas.Fit( self.pn_partidas )
		self.nb_detalhes.AddPage( self.pn_partidas, u"Partidas", True )
		self.m_panel4 = wx.Panel( self.nb_detalhes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.Enable( False )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.m_panel4.SetSizer( bSizer11 )
		self.m_panel4.Layout()
		bSizer11.Fit( self.m_panel4 )
		self.nb_detalhes.AddPage( self.m_panel4, u"a page", False )
		
		lay_detalhes.Add( self.nb_detalhes, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		lay_slip.Add( lay_detalhes, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		
		lay_body.Add( lay_slip, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( lay_body )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

