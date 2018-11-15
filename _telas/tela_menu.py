# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrmMenu
###########################################################################

class FrmMenu ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Principal", pos = wx.DefaultPosition, size = wx.Size( 883,620 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.MnbMenu = wx.MenuBar( 0 )
		self.MnSistema = wx.Menu()
		self.mn_cadastro = wx.Menu()
		self.mn_dbemp01 = wx.MenuItem( self.mn_cadastro, wx.ID_ANY, u"Empresas", wx.EmptyString, wx.ITEM_NORMAL )
		self.mn_cadastro.AppendItem( self.mn_dbemp01 )
		
		self.mn_prm01 = wx.MenuItem( self.mn_cadastro, wx.ID_ANY, u"Pessoas", wx.EmptyString, wx.ITEM_NORMAL )
		self.mn_cadastro.AppendItem( self.mn_prm01 )
		
		self.MnSistema.AppendSubMenu( self.mn_cadastro, u"Cadastros" )
		
		self.MniSair = wx.MenuItem( self.MnSistema, wx.ID_ANY, u"&Sair", wx.EmptyString, wx.ITEM_NORMAL )
		self.MnSistema.AppendItem( self.MniSair )
		
		self.MnbMenu.Append( self.MnSistema, u"Sistema" ) 
		
		self.MnSobre = wx.Menu()
		self.mn_info = wx.MenuItem( self.MnSobre, wx.ID_ANY, u"Sobre o sistema", wx.EmptyString, wx.ITEM_NORMAL )
		self.MnSobre.AppendItem( self.mn_info )
		
		self.MnbMenu.Append( self.MnSobre, u"S&obre" ) 
		
		self.SetMenuBar( self.MnbMenu )
		
		self.StbMenu = self.CreateStatusBar( 3, 0, wx.ID_ANY )
		SizPrincipal = wx.BoxSizer( wx.VERTICAL )
		
		SizBody = wx.BoxSizer( wx.HORIZONTAL )
		
		SizLeft = wx.BoxSizer( wx.HORIZONTAL )
		
		SizLeft.SetMinSize( wx.Size( 300,-1 ) ) 
		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		SizLeft.Add( self.m_treeCtrl1, 1, wx.EXPAND, 5 )
		
		
		SizBody.Add( SizLeft, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		SizBody.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		SizPrincipal.Add( SizBody, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( SizPrincipal )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.ac_emp01, id = self.mn_dbemp01.GetId() )
		self.Bind( wx.EVT_MENU, self.ac_prm01, id = self.mn_prm01.GetId() )
		self.Bind( wx.EVT_MENU, self.on_sair, id = self.MniSair.GetId() )
		self.Bind( wx.EVT_MENU, self.ac_sobre, id = self.mn_info.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ac_emp01( self, event ):
		event.Skip()
	
	def ac_prm01( self, event ):
		event.Skip()
	
	def on_sair( self, event ):
		event.Skip()
	
	def ac_sobre( self, event ):
		event.Skip()
	

