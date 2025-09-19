# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"字幕查询下载工具-liugngg"), pos = wx.DefaultPosition, size = wx.Size( 748,561 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        main_sizer = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, _(u"文件目录设置") ), wx.VERTICAL )

        h0_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"片名:"), wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )

        h0_sizer.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.name_input = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        h0_sizer.Add( self.name_input, 1, wx.ALL, 5 )

        self.reset_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"重置"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h0_sizer.Add( self.reset_button, 0, wx.ALL, 5 )

        self.rename_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"创建目录"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h0_sizer.Add( self.rename_button, 0, wx.ALL, 5 )


        sbSizer1.Add( h0_sizer, 0, wx.ALL|wx.EXPAND, 5 )

        h1_sizer = wx.BoxSizer( wx.HORIZONTAL )


        h1_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.is_av = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"番号"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.is_av.SetValue(True)
        h1_sizer.Add( self.is_av, 0, wx.ALL, 5 )

        self.is_4k = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"4K"), wx.DefaultPosition, wx.DefaultSize, 0 )
        h1_sizer.Add( self.is_4k, 0, wx.ALL, 5 )

        self.is_crack = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"破解"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.is_crack.SetValue(True)
        h1_sizer.Add( self.is_crack, 0, wx.ALL, 5 )

        self.is_enhance = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"增强"), wx.DefaultPosition, wx.DefaultSize, 0 )
        h1_sizer.Add( self.is_enhance, 0, wx.ALL, 5 )

        self.is_leaked = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"流出"), wx.DefaultPosition, wx.DefaultSize, 0 )
        h1_sizer.Add( self.is_leaked, 0, wx.ALL, 5 )

        self.is_cn = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"中字"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.is_cn.SetValue(True)
        h1_sizer.Add( self.is_cn, 0, wx.ALL, 5 )


        sbSizer1.Add( h1_sizer, 1, wx.ALL|wx.EXPAND, 5 )

        h3_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"保存目录:"), wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )

        h3_sizer.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.dir_input = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.dir_input.DragAcceptFiles( True )

        h3_sizer.Add( self.dir_input, 1, wx.ALL, 5 )

        self.browse_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"浏览..."), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h3_sizer.Add( self.browse_button, 0, wx.ALL, 5 )

        self.open_dir_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"打开目录"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h3_sizer.Add( self.open_dir_button, 0, wx.ALL, 5 )


        sbSizer1.Add( h3_sizer, 1, wx.ALL|wx.EXPAND, 5 )


        main_sizer.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, _(u"字幕查询下载") ), wx.VERTICAL )

        h4_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"批量下载数量："), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        h4_sizer.Add( self.m_staticText6, 0, wx.ALL, 10 )

        self.batch_count_spin = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 5 )
        h4_sizer.Add( self.batch_count_spin, 0, wx.ALL, 5 )


        h4_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.batch_download_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"批量下载"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h4_sizer.Add( self.batch_download_button, 0, wx.ALL, 5 )

        self.download_selected_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"下载选中"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h4_sizer.Add( self.download_selected_button, 0, wx.ALL, 5 )

        self.search_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"查询字幕"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        h4_sizer.Add( self.search_button, 0, wx.ALL, 5 )


        h4_sizer.Add( ( 5, 0), 0, wx.EXPAND, 5 )


        sbSizer2.Add( h4_sizer, 0, wx.EXPAND, 5 )

        v_listCtrl = wx.BoxSizer( wx.VERTICAL )

        self.result_list = wx.ListCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
        v_listCtrl.Add( self.result_list, 1, wx.EXPAND, 0 )


        sbSizer2.Add( v_listCtrl, 1, wx.EXPAND, 5 )


        main_sizer.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_panel.SetSizer( main_sizer )
        self.m_panel.Layout()
        main_sizer.Fit( self.m_panel )
        bSizer1.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.status_bar = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.name_input.Bind( wx.EVT_TEXT_ENTER, self.on_search )
        self.reset_button.Bind( wx.EVT_BUTTON, self.on_reset )
        self.rename_button.Bind( wx.EVT_BUTTON, self.on_create_dir )
        self.browse_button.Bind( wx.EVT_BUTTON, self.on_browse )
        self.open_dir_button.Bind( wx.EVT_BUTTON, self.on_open_dir )
        self.batch_download_button.Bind( wx.EVT_BUTTON, self.on_batch_download )
        self.download_selected_button.Bind( wx.EVT_BUTTON, self.on_download_selected )
        self.search_button.Bind( wx.EVT_BUTTON, self.on_search )
        self.status_bar.Bind( wx.EVT_LEFT_DCLICK, self.on_top_window )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_search( self, event ):
        event.Skip()

    def on_reset( self, event ):
        event.Skip()

    def on_create_dir( self, event ):
        event.Skip()

    def on_browse( self, event ):
        event.Skip()

    def on_open_dir( self, event ):
        event.Skip()

    def on_batch_download( self, event ):
        event.Skip()

    def on_download_selected( self, event ):
        event.Skip()


    def on_top_window( self, event ):
        event.Skip()


