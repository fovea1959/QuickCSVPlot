# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class QuickplotFrame
###########################################################################

class QuickplotFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QuickPlot", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.plot_button = wx.Button( self.m_panel3, wx.ID_ANY, u"&Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.plot_button.Enable( False )

		bSizer8.Add( self.plot_button, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer8 )
		self.m_panel3.Layout()
		bSizer8.Fit( self.m_panel3 )
		self.sizer.Add( self.m_panel3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.sizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.cb_window = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.cb_window.SetScrollRate( 5, 5 )
		self.cb_sizer = wx.BoxSizer( wx.VERTICAL )


		self.cb_window.SetSizer( self.cb_sizer )
		self.cb_window.Layout()
		self.cb_sizer.Fit( self.cb_window )
		self.sizer.Add( self.cb_window, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( self.sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.plot_button.Bind( wx.EVT_BUTTON, self.on_plot_button_pressed )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_plot_button_pressed( self, event ):
		event.Skip()


