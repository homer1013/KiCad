# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Nov 12 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class loginDialog
###########################################################################

class loginDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( 750,450 ) )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer68 = wx.BoxSizer( wx.VERTICAL )


        bSizer68.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer72 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer72.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bpButton1 = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

        try:
            self.m_bpButton1.SetBitmap( wx.NullBitmap )
        except:
            self.m_bpButton1.SetBitmap( wx.BitmapBundle(wx.NullBitmap ))
        bSizer72.Add( self.m_bpButton1, 1, 0, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Sierra Circuits Online Quote", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Login with your email address and password below\nfor realtime, online quotes from your KiCad project", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer72.Add( bSizer8, 6, wx.EXPAND, 5 )


        bSizer68.Add( bSizer72, 1, wx.BOTTOM|wx.EXPAND, 50 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer7.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText21 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Email Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer7.Add( self.m_staticText21, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_username = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        # self.m_username.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer7.Add( self.m_username, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button19 = wx.Button( self.m_panel6, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button19.Enable( False )
        self.m_button19.Hide()

        bSizer7.Add( self.m_button19, 4, wx.ALIGN_CENTER_VERTICAL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 3 )


        bSizer7.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer68.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer71 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer71.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText211 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText211.Wrap( -1 )

        bSizer71.Add( self.m_staticText211, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_password = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer71.Add( self.m_password, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_forgotPassword = wx.Button( self.m_panel6, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.m_forgotPassword.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

        bSizer71.Add( self.m_forgotPassword, 4, wx.ALIGN_CENTER_VERTICAL, 0 )


        bSizer71.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer68.Add( bSizer71, 1, wx.EXPAND, 5 )


        bSizer68.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_createAccount = wx.Button( self.m_panel6, wx.ID_ANY, u"Create New Account", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_createAccount.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.m_createAccount.SetBackgroundColour( wx.Colour( 253, 201, 73 ) )

        bSizer12.Add( self.m_createAccount, 0, wx.ALL, 5 )

        self.m_login = wx.Button( self.m_panel6, wx.ID_OK, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_login.SetDefault()
        bSizer12.Add( self.m_login, 0, wx.ALL, 5 )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_spacerText = wx.StaticText( self.m_panel6, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE )
        self.m_spacerText.Wrap( -1 )

        self.m_spacerText.Hide()

        bSizer12.Add( self.m_spacerText, 0, wx.ALL, 5 )


        bSizer68.Add( bSizer12, 1, wx.EXPAND, 5 )


        bSizer68.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText63 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )

        self.m_staticText63.Hide()

        bSizer68.Add( self.m_staticText63, 0, wx.ALL, 5 )

        bSizer84 = wx.BoxSizer( wx.VERTICAL )

        self.m_ccpa = wx.Button( self.m_panel6, wx.ID_ANY, u"California CCPA Compliance", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.m_ccpa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

        bSizer84.Add( self.m_ccpa, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        bSizer68.Add( bSizer84, 1, wx.EXPAND, 5 )
        self.m_panel6.SetSizer( bSizer68 )
        self.m_panel6.Layout()
        bSizer68.Fit( self.m_panel6 )
        bSizer6.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel7.Enable( False )
        self.m_panel7.Hide()

        bSizer70 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText59 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"New User Registration", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText59.Wrap( -1 )

        self.m_staticText59.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer70.Add( self.m_staticText59, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 1 )

        # self.m_staticline8 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        # bSizer70.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer73 = wx.BoxSizer( wx.HORIZONTAL )


        # bSizer73.Add( ( 0, 0), 3, wx.EXPAND, 5 )
        bSizer73.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText212 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Email :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText212.Wrap( -1 )

        bSizer73.Add( self.m_staticText212, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_email = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73.Add( self.m_email, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        bSizer73.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer73, 1, wx.EXPAND, 0 )

        bSizer74 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer74.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText213 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText213.Wrap( -1 )

        bSizer74.Add( self.m_staticText213, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_rgpassword = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer74.Add( self.m_rgpassword, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)


        bSizer74.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer74, 1, wx.EXPAND, 0 )

        bSizer75 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer75.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText214 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Confirm Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText214.Wrap( -1 )

        bSizer75.Add( self.m_staticText214, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_confirmpassword = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer75.Add( self.m_confirmpassword, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        bSizer75.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer75, 1, wx.EXPAND, 0 )

        bSizer76 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer76.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText215 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"First Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText215.Wrap( -1 )

        bSizer76.Add( self.m_staticText215, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_firstname = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer76.Add( self.m_firstname, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        bSizer76.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer76, 1, wx.EXPAND, 0 )

        bSizer77 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer77.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText216 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Last Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText216.Wrap( -1 )

        bSizer77.Add( self.m_staticText216, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_lastname = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer77.Add( self.m_lastname, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)


        bSizer77.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer77, 1, wx.EXPAND, 0 )

        bSizer78 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer78.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText217 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Company :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText217.Wrap( -1 )

        bSizer78.Add( self.m_staticText217, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_company = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer78.Add( self.m_company, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        bSizer78.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer78, 1, wx.EXPAND, 0)

        bSizer79 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer79.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText218 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Phone Number :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText218.Wrap( -1 )

        bSizer79.Add( self.m_staticText218, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.m_phonenumber = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer79.Add( self.m_phonenumber, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        bSizer79.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer70.Add( bSizer79, 1, wx.EXPAND, 0 )


        # bSizer70.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer90 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer90.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_button35 = wx.Button( self.m_panel7, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer90.Add( self.m_button35, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

        self.m_button34 = wx.Button( self.m_panel7, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer90.Add( self.m_button34, 0, wx.ALIGN_CENTER|wx.ALL, 0)


        bSizer90.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer70.Add( bSizer90, 1, wx.EXPAND, 0)


        bSizer70.Add( ( 0, 0), 1, wx.EXPAND, 0)

        self.m_staticText631 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText631.Wrap( -1 )

        self.m_staticText631.Hide()

        bSizer70.Add( self.m_staticText631, 0, wx.ALL, 1 )


        self.m_panel7.SetSizer( bSizer70 )
        self.m_panel7.Layout()
        bSizer70.Fit( self.m_panel7 )
        bSizer6.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel9.Enable( False )
        self.m_panel9.Hide()

        bSizer681 = wx.BoxSizer( wx.VERTICAL )


        bSizer681.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer721 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer721.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer81 = wx.BoxSizer( wx.VERTICAL )


        bSizer81.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer81.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer721.Add( bSizer81, 6, wx.EXPAND, 5 )


        bSizer681.Add( bSizer721, 1, wx.BOTTOM|wx.EXPAND, 50 )

        self.m_staticText411 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"No worries, we can help you reset your password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText411.Wrap( -1 )

        self.m_staticText411.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer681.Add( self.m_staticText411, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticline7 = wx.StaticLine( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline7.Enable( False )
        self.m_staticline7.Hide()

        bSizer681.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer710 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer710.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText219 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Email :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.m_staticText219.Wrap( -1 )

        bSizer710.Add( self.m_staticText219, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_resetEmail = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_resetEmail.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        # self.m_resetEmail.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer710.Add( self.m_resetEmail, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button191 = wx.Button( self.m_panel9, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button191.Enable( False )
        self.m_button191.Hide()

        bSizer710.Add( self.m_button191, 4, wx.ALIGN_CENTER_VERTICAL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 3 )


        bSizer710.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer681.Add( bSizer710, 1, wx.EXPAND, 5 )

        bSizer121 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer121.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer121.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_reset = wx.Button( self.m_panel9, wx.ID_OK, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_reset.SetDefault()
        bSizer121.Add( self.m_reset, 0, wx.ALL, 5 )

        self.m_resetCancel = wx.Button( self.m_panel9, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer121.Add( self.m_resetCancel, 0, wx.ALL, 5 )


        bSizer121.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer681.Add( bSizer121, 1, wx.EXPAND, 5 )


        bSizer681.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText632 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText632.Wrap( -1 )

        self.m_staticText632.Hide()

        bSizer681.Add( self.m_staticText632, 0, wx.ALL, 5 )


        self.m_panel9.SetSizer( bSizer681 )
        self.m_panel9.Layout()
        bSizer681.Fit( self.m_panel9 )
        bSizer6.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel11.Enable( False )
        self.m_panel11.Hide()

        bSizer682 = wx.BoxSizer( wx.VERTICAL )


        bSizer682.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer7211 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer7211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer811 = wx.BoxSizer( wx.VERTICAL )


        bSizer811.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer7211.Add( bSizer811, 6, wx.EXPAND, 5 )


        bSizer682.Add( bSizer7211, 1, wx.EXPAND, 5 )

        self.m_staticText31 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"User profile password change !!", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText31.Wrap( -1 )

        self.m_staticText31.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

        bSizer682.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticline81 = wx.StaticLine( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer682.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer711 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer711.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText2110 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Old Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2110.Wrap( -1 )

        bSizer711.Add( self.m_staticText2110, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_cpassword = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        # self.m_cpassword.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        # self.m_cpassword.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer711.Add( self.m_cpassword, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button1911 = wx.Button( self.m_panel11, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1911.Enable( False )
        self.m_button1911.Hide()

        bSizer711.Add( self.m_button1911, 0, wx.ALL, 5 )


        bSizer711.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer682.Add( bSizer711, 1, wx.EXPAND, 5 )

        bSizer712 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer712.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText2111 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"New Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2111.Wrap( -1 )

        bSizer712.Add( self.m_staticText2111, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_newpassword = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer712.Add( self.m_newpassword, 6, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button1912 = wx.Button( self.m_panel11, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1912.Enable( False )
        self.m_button1912.Hide()

        bSizer712.Add( self.m_button1912, 0, wx.ALL, 5 )


        bSizer712.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer682.Add( bSizer712, 1, wx.EXPAND, 5 )

        bSizer122 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer122.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer122.Add( ( 0, 0), 6, wx.EXPAND, 5 )

        self.m_uPassword = wx.Button( self.m_panel11, wx.ID_OK, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_uPassword.SetDefault()
        bSizer122.Add( self.m_uPassword, 0, wx.ALL, 5 )

        self.m_uCancel = wx.Button( self.m_panel11, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer122.Add( self.m_uCancel, 0, wx.ALL, 5 )


        bSizer122.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer682.Add( bSizer122, 1, wx.EXPAND, 5 )


        bSizer682.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6321 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6321.Wrap( -1 )

        self.m_staticText6321.Hide()

        bSizer682.Add( self.m_staticText6321, 0, wx.ALL, 5 )


        self.m_panel11.SetSizer( bSizer682 )
        self.m_panel11.Layout()
        bSizer682.Fit( self.m_panel11 )
        bSizer6.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel10.Enable( False )
        self.m_panel10.Hide()

        bSizer6811 = wx.BoxSizer( wx.VERTICAL )


        bSizer6811.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer7212 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer7212.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer812 = wx.BoxSizer( wx.VERTICAL )


        bSizer812.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer812.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer7212.Add( bSizer812, 6, wx.EXPAND, 5 )


        bSizer6811.Add( bSizer7212, 1, wx.BOTTOM|wx.EXPAND, 50 )

        self.m_staticText4111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"User profile password change !!", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4111.Wrap( -1 )

        self.m_staticText4111.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer6811.Add( self.m_staticText4111, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticline11 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer6811.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer71011 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer71011.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText21911 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Old Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21911.Wrap( -1 )

        bSizer71011.Add( self.m_staticText21911, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_uPassword11 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        # self.m_uPassword11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        # self.m_uPassword11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer71011.Add( self.m_uPassword11, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button19131 = wx.Button( self.m_panel10, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button19131.Enable( False )
        self.m_button19131.Hide()

        bSizer71011.Add( self.m_button19131, 4, wx.ALIGN_CENTER_VERTICAL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 3 )


        bSizer71011.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer6811.Add( bSizer71011, 1, wx.EXPAND, 5 )

        self.m_staticline71 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline71.Enable( False )
        self.m_staticline71.Hide()

        bSizer6811.Add( self.m_staticline71, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer7101 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer7101.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_staticText2191 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"New Password :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.m_staticText2191.Wrap( -1 )

        bSizer7101.Add( self.m_staticText2191, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_uNewPassword1 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        # self.m_uNewPassword1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        # self.m_uNewPassword1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer7101.Add( self.m_uNewPassword1, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button1913 = wx.Button( self.m_panel10, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1913.Enable( False )
        self.m_button1913.Hide()

        bSizer7101.Add( self.m_button1913, 4, wx.ALIGN_CENTER_VERTICAL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 3 )


        bSizer7101.Add( ( 0, 0), 2, wx.EXPAND, 0 )


        bSizer6811.Add( bSizer7101, 1, wx.EXPAND, 5 )

        bSizer1211 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer1211.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer1211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_changePassword1 = wx.Button( self.m_panel10, wx.ID_OK, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_changePassword1.SetDefault()
        bSizer1211.Add( self.m_changePassword1, 0, wx.ALL, 5 )

        self.m_changeCancel1 = wx.Button( self.m_panel10, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1211.Add( self.m_changeCancel1, 0, wx.ALL, 5 )


        bSizer1211.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer6811.Add( bSizer1211, 1, wx.EXPAND, 5 )


        bSizer6811.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6322 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6322.Wrap( -1 )

        self.m_staticText6322.Hide()

        bSizer6811.Add( self.m_staticText6322, 0, wx.ALL, 5 )


        self.m_panel10.SetSizer( bSizer6811 )
        self.m_panel10.Layout()
        bSizer6811.Fit( self.m_panel10 )
        bSizer6.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_forgotPassword.Bind( wx.EVT_BUTTON, self.onForgotPassword )
        self.m_createAccount.Bind( wx.EVT_BUTTON, self.onCreateAccount )
        self.m_login.Bind( wx.EVT_BUTTON, self.onLogin )
        self.m_button35.Bind( wx.EVT_BUTTON, self.onRegister )
        self.m_button34.Bind( wx.EVT_BUTTON, self.onRegCancel )
        self.m_reset.Bind( wx.EVT_BUTTON, self.onReset )
        self.m_resetCancel.Bind( wx.EVT_BUTTON, self.onResetCancel )
        self.m_uPassword.Bind( wx.EVT_BUTTON, self.onChangePassword )
        self.m_uCancel.Bind( wx.EVT_BUTTON, self.onChangeCancel )
        self.m_changePassword1.Bind( wx.EVT_BUTTON, self.onChangePassword )
        self.m_changeCancel1.Bind( wx.EVT_BUTTON, self.onChangeCancel )
        self.m_ccpa.Bind( wx.EVT_BUTTON, self.onCCPA )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onForgotPassword( self, event ):
        event.Skip()

    def onCreateAccount( self, event ):
        event.Skip()

    def onLogin( self, event ):
        event.Skip()

    def onRegister( self, event ):
        event.Skip()

    def onRegCancel( self, event ):
        event.Skip()

    def onReset( self, event ):
        event.Skip()

    def onResetCancel( self, event ):
        event.Skip()

    def onChangePassword( self, event ):
        event.Skip()

    def onChangeCancel( self, event ):
        event.Skip()

    def onCCPA( self, event ):
        event.Skip()



###########################################################################
## Class quoteDialog
###########################################################################

class quoteDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,650 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

        try:
            self.m_bpButton1.SetBitmap( wx.NullBitmap )
        except:
            self.m_bpButton1.SetBitmap(wx.BitmapBundle(wx.NullBitmap ))
        bSizer7.Add( self.m_bpButton1, 1, 0, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Sierra Circuits Online Quote", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Please review the selections below and \nselect \"Get Quote\" when you are satisfied with your choices.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer7.Add( bSizer8, 3, wx.EXPAND, 5 )


        bSizer5.Add( bSizer7, 4, wx.ALL|wx.EXPAND, 5 )

        # self.m_orderHisory = wx.Button( self, wx.ID_ANY, u"Order History", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER)
        # # self.m_orderHisory.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        # bSizer5.Add( self.m_orderHisory, 0, wx.ALL, 5 )
        # self.m_ordHisTip = wx.StaticBitmap( bSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer5.Add( self.m_ordHisTip, 0, wx.ALL, 5 )

        bSizer105 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_orderHisory = wx.Button( self, wx.ID_ANY, u"Order History", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
        # self.m_orderHisory.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        # self.m_orderHisory.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

        bSizer105.Add( self.m_orderHisory, 0, wx.ALL, 5 )

        self.m_ordHisTip = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer105.Add( self.m_ordHisTip, 0, wx.ALL, 5 )


        bSizer5.Add( bSizer105, 1, wx.EXPAND, 5 )

        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP )
        self.m_panel_geometry = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_geometry, wx.ID_ANY, u"Dimensions" ), wx.VERTICAL )


        sbSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_width = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Width", wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
        self.m_width.Enable( False )

        bSizer10.Add( self.m_width, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        

        self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText5.Wrap( -1 )

        bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_length = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Length", wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
        self.m_length.Enable( False )

        bSizer10.Add( self.m_length, 1, wx.ALL|wx.EXPAND, 5 )

        
        sbSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )


        sbSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer11.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 10 )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_geometry, wx.ID_ANY, u"Quantities" ), wx.VERTICAL )


        sbSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        self.m_qtyTip = wx.StaticBitmap( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.m_qtyTip, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

        self.m_quant1 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
        self.m_quant1.Enable( True )
        self.m_quant1.Bind(wx.EVT_TEXT, self.onAction_m_quant1)

        gSizer1.Add( self.m_quant1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_quant2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
        self.m_quant2.Enable( True )
        self.m_quant2.Bind(wx.EVT_TEXT, self.onAction_m_quant2)

        gSizer1.Add( self.m_quant2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_quant3 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
        self.m_quant3.Enable( True )
        self.m_quant3.Bind(wx.EVT_TEXT, self.onAction_m_quant3)

        gSizer1.Add( self.m_quant3, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_quant4 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
        self.m_quant4.Enable( True )
        self.m_quant4.Bind(wx.EVT_TEXT, self.onAction_m_quant4)

        gSizer1.Add( self.m_quant4, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer3.Add( gSizer1, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer11.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 10 )


        bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_geometry, wx.ID_ANY, u"Layers" ), wx.VERTICAL )


        sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        m_layerCountChoices = [ u"2 Layers", u"4 Layers", u"6 Layers", u"8 Layers", u"10 Layers" ]
        self.m_layerCount = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_layerCountChoices, 0 )
        self.m_layerCount.SetSelection( 0 )
        sbSizer2.Add( self.m_layerCount, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 15 )


        sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer12.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 10 )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_geometry, wx.ID_ANY, u"Thickness" ), wx.VERTICAL )


        sbSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        self.m_layThicknessTip = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer4.Add( self.m_layThicknessTip, 0, wx.ALL, 5 )

        m_thicknessChoices = [ u"0.062 inches", u"0.031 inches" ]
        self.m_thickness = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_thicknessChoices, 0 )
        self.m_thickness.SetSelection( 0 )
        sbSizer4.Add( self.m_thickness, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 15 )


        sbSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer12.Add( sbSizer4, 1, wx.ALL|wx.EXPAND, 10 )


        bSizer9.Add( bSizer12, 0, wx.EXPAND, 5 )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_panel_geometry.SetSizer( bSizer9 )
        self.m_panel_geometry.Layout()
        bSizer9.Fit( self.m_panel_geometry )
        self.m_notebook.AddPage( self.m_panel_geometry, u"Board Geometry", True )
        self.m_panelClearance = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer91 = wx.BoxSizer( wx.VERTICAL )

        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelClearance, wx.ID_ANY, u"Outer Layers" ), wx.VERTICAL )

        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

        
        self.m_staticText26 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Minimum Trace Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        bSizer101.Add( self.m_staticText26, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_outerMinTrace = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_outerMinTrace.Enable( False )

        bSizer101.Add( self.m_outerMinTrace, 1, wx.ALL, 5 )

        self.m_minOuterTraceWidthTip = wx.StaticBitmap( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_minOuterTraceWidthTip, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_highlightMinTrace = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_highlightMinTrace.Hide()

        bSizer101.Add( self.m_highlightMinTrace, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizer11.Add( bSizer101, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer1012 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText261 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Minimum Trace Spacing:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText261.Wrap( -1 )

        bSizer1012.Add( self.m_staticText261, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_outerMinSpace = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_outerMinSpace.Enable( False )

        bSizer1012.Add( self.m_outerMinSpace, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_minOuterTraceSpaceTip = wx.StaticBitmap( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1012.Add( self.m_minOuterTraceSpaceTip, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_highlightMinSpace = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_highlightMinSpace.Hide()

        bSizer1012.Add( self.m_highlightMinSpace, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer1012.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizer11.Add( bSizer1012, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer91.Add( sbSizer11, 0, wx.ALL|wx.EXPAND, 10 )

        sbSizerInnerLayer = wx.StaticBoxSizer( wx.StaticBox( self.m_panelClearance, wx.ID_ANY, u"Inner Layers" ), wx.VERTICAL )

        bSizer1013 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText262 = wx.StaticText( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, u"Minimum Trace Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText262.Wrap( -1 )

        bSizer1013.Add( self.m_staticText262, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_innerMinTrace = wx.TextCtrl( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_innerMinTrace.Enable( False )

        bSizer1013.Add( self.m_innerMinTrace, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.m_minInnerTraceWidthTip = wx.StaticBitmap( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1013.Add( self.m_minInnerTraceWidthTip, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_innerMinTraceHighlight = wx.Button( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_innerMinTraceHighlight.Hide()

        bSizer1013.Add( self.m_innerMinTraceHighlight, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer1013.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizerInnerLayer.Add( bSizer1013, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer10121 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2611 = wx.StaticText( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, u"Minimum Trace Spacing:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2611.Wrap( -1 )

        self.m_innerMinSpace = wx.TextCtrl( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_innerMinSpace.Enable( False )

        bSizer10121.Add( self.m_staticText2611, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        bSizer10121.Add( self.m_innerMinSpace, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL,5 )
        self.m_minInnerTraceSpaceTip = wx.StaticBitmap( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10121.Add( self.m_minInnerTraceSpaceTip, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_innerMinSpaceHighlight = wx.Button( sbSizerInnerLayer.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_innerMinSpaceHighlight.Hide()

        bSizer10121.Add( self.m_innerMinSpaceHighlight, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer10121.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizerInnerLayer.Add( bSizer10121, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer91.Add( sbSizerInnerLayer, 0, wx.ALL|wx.EXPAND, 10 )


        bSizer91.Add( ( 0, 0), 0, wx.EXPAND, 5 )


        self.m_panelClearance.SetSizer( bSizer91 )
        self.m_panelClearance.Layout()
        bSizer91.Fit( self.m_panelClearance )
        self.m_notebook.AddPage( self.m_panelClearance, u"Board Clearances", False )
        self.m_panelHoles = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer911 = wx.BoxSizer( wx.VERTICAL )

        bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )

        sbDrillHoles = wx.StaticBoxSizer( wx.StaticBox( self.m_panelHoles, wx.ID_ANY, u"Drill Holes" ), wx.VERTICAL )

        bSizer232 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer232.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText62 = wx.StaticText( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Count", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText62.Wrap( -1 )

        bSizer232.Add( self.m_staticText62, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_holeCount = wx.TextCtrl( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_holeCount.Enable( False )

        bSizer232.Add( self.m_holeCount, 2, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.TOP, 5 )

        self.m_HolesCountTip = wx.StaticBitmap( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer232.Add( self.m_HolesCountTip, 0, wx.ALL, 5 )

        self.m_HighlightMinHole11 = wx.Button( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HighlightMinHole11.Enable( False )
        self.m_HighlightMinHole11.Hide()

        bSizer232.Add( self.m_HighlightMinHole11, 1, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer232.Add( ( 0, 0), 2, 0, 5 )


        sbDrillHoles.Add( bSizer232, 1, wx.EXPAND, 5 )

        bSizer242 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer242.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText72 = wx.StaticText( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Density", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText72.Wrap( -1 )

        bSizer242.Add( self.m_staticText72, 3, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        self.m_holeDensity = wx.TextCtrl( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_holeDensity.Enable( False )

        bSizer242.Add( self.m_holeDensity, 2, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.TOP, 5 )

        self.m_HolesDensityTip = wx.StaticBitmap( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer242.Add( self.m_HolesDensityTip, 0, wx.ALL, 5 )

        self.m_Placeholder1 = wx.Button( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Placeholder1.Enable( False )
        self.m_Placeholder1.Hide()

        bSizer242.Add( self.m_Placeholder1, 1, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer242.Add( ( 0, 0), 2, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )


        sbDrillHoles.Add( bSizer242, 0, wx.EXPAND, 5 )

        bSizer24121 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer24121.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText7121 = wx.StaticText( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Minimum Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7121.Wrap( -1 )

        bSizer24121.Add( self.m_staticText7121, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_minHoleSize = wx.TextCtrl( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_minHoleSize.Enable( False )

        bSizer24121.Add( self.m_minHoleSize, 2, wx.BOTTOM|wx.TOP, 5 )

        self.m_HolesMinSizeTip = wx.StaticBitmap( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24121.Add( self.m_HolesMinSizeTip, 0, wx.ALL, 5 )

        self.m_HighlightMinHole = wx.Button( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HighlightMinHole.Hide()

        bSizer24121.Add( self.m_HighlightMinHole, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT, 5 )


        bSizer24121.Add( ( 0, 0), 2, wx.EXPAND, 5 )


        sbDrillHoles.Add( bSizer24121, 0, wx.EXPAND, 5 )

        bSizer241211 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer241211.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText71211 = wx.StaticText( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Minimum Annular Ring", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText71211.Wrap( -1 )

        bSizer241211.Add( self.m_staticText71211, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_minAnnularRing = wx.TextCtrl( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_minAnnularRing.Enable( False )

        bSizer241211.Add( self.m_minAnnularRing, 2, wx.BOTTOM|wx.TOP, 5 )

        self.m_HolesMinRingTip = wx.StaticBitmap( sbDrillHoles.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer241211.Add( self.m_HolesMinRingTip, 0, wx.ALL, 5 )

        self.m_HighlightMinRing = wx.Button( sbDrillHoles.GetStaticBox(), wx.ID_ANY, u"Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HighlightMinRing.Hide()

        bSizer241211.Add( self.m_HighlightMinRing, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT, 5 )


        bSizer241211.Add( ( 0, 0), 2, wx.EXPAND, 5 )


        sbDrillHoles.Add( bSizer241211, 0, wx.EXPAND, 5 )


        bSizer1111.Add( sbDrillHoles, 1, wx.ALL|wx.EXPAND, 10 )


        bSizer911.Add( bSizer1111, 0, wx.EXPAND, 5 )

        bSizer1211 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelHoles, wx.ID_ANY, u"Slots and Cutouts" ), wx.VERTICAL )

        bSizer2321 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer2321.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText621 = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Count", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText621.Wrap( -1 )

        bSizer2321.Add( self.m_staticText621, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_cutoutCount = wx.TextCtrl( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_cutoutCount.Enable( False )

        bSizer2321.Add( self.m_cutoutCount, 2, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.TOP, 5 )

        self.m_cutoutCountTip = wx.StaticBitmap( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2321.Add( self.m_cutoutCountTip, 0, wx.ALL, 5 )

        self.m_button19 = wx.Button( sbSizer211.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button19.Enable( False )
        self.m_button19.Hide()

        bSizer2321.Add( self.m_button19, 1, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer2321.Add( ( 0, 0), 2, 0, 5 )


        sbSizer211.Add( bSizer2321, 0, wx.EXPAND, 5 )

        bSizer52 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer52.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText6211 = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Plating", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6211.Wrap( -1 )

        bSizer52.Add( self.m_staticText6211, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_platingChoices = [ u"Plated", u"Non Plated", u"Both", u"None" ]
        self.m_plating = wx.Choice( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_platingChoices, 0 )
        self.m_plating.SetSelection( 0 )
        bSizer52.Add( self.m_plating, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_platingTip = wx.StaticBitmap( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer52.Add( self.m_platingTip, 0, wx.ALL, 5 )

        self.m_button20 = wx.Button( sbSizer211.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button20.Enable( False )
        self.m_button20.Hide()

        bSizer52.Add( self.m_button20, 1, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer52.Add( ( 0, 0), 2, 0, 5 )


        sbSizer211.Add( bSizer52, 1, wx.EXPAND, 5 )


        bSizer1211.Add( sbSizer211, 1, wx.ALL|wx.EXPAND, 10 )


        bSizer911.Add( bSizer1211, 0, wx.EXPAND, 5 )


        self.m_panelHoles.SetSizer( bSizer911 )
        self.m_panelHoles.Layout()
        bSizer911.Fit( self.m_panelHoles )
        self.m_notebook.AddPage( self.m_panelHoles, u"Holes", False )
        self.m_panelSurface = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        sbSilkscreen = wx.StaticBoxSizer( wx.StaticBox( self.m_panelSurface, wx.ID_ANY, u"Silkscreen" ), wx.VERTICAL )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( sbSilkscreen.GetStaticBox(), wx.ID_ANY, u"Sides", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer23.Add( self.m_staticText6, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_SilkSidesChoices = [ u"Top", u"Bottom", u"Both", u"None" ]
        self.m_SilkSides = wx.Choice( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_SilkSidesChoices, 0 )
        self.m_SilkSides.SetSelection( 0 )
        bSizer23.Add( self.m_SilkSides, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_SilkSideTip = wx.StaticBitmap( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_SilkSideTip, 0, wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, 0, 5 )


        sbSilkscreen.Add( bSizer23, 1, wx.EXPAND, 5 )

        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText7 = wx.StaticText( sbSilkscreen.GetStaticBox(), wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer24.Add( self.m_staticText7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_SilkColorChoices = [ u"White", u"Yellow", u"Black" ]
        self.m_SilkColor = wx.Choice( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_SilkColorChoices, 0 )
        self.m_SilkColor.SetSelection( 0 )
        self.m_SilkColor.Enable( True )

        bSizer24.Add( self.m_SilkColor, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_SilkColorTip = wx.StaticBitmap( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_SilkColorTip, 0, wx.ALL, 5 )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSilkscreen.Add( bSizer24, 1, wx.EXPAND, 5 )

        bSizer25 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer25.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText10 = wx.StaticText( sbSilkscreen.GetStaticBox(), wx.ID_ANY, u"Material", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer25.Add( self.m_staticText10, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_materialChoices = [ u"FR4", u"FR4- lead free", u"Polyimide", u"Nan Ya NP-175", u"FR4-06" ]
        self.m_material = wx.Choice( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_materialChoices, 0 )
        self.m_material.SetSelection( 0 )
        self.m_material.Enable( True )

        bSizer25.Add( self.m_material, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_materialTip = wx.StaticBitmap( sbSilkscreen.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_materialTip, 0, wx.ALL, 5 )

        bSizer25.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSilkscreen.Add( bSizer25, 1, wx.EXPAND, 5 )



        bSizer2412 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer16.Add( sbSilkscreen, 1, wx.ALL|wx.EXPAND, 5 )


        sbSoldermask = wx.StaticBoxSizer( wx.StaticBox( self.m_panelSurface, wx.ID_ANY, u"Soldermask" ), wx.VERTICAL )

        bSizer231 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer231.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText61 = wx.StaticText( sbSoldermask.GetStaticBox(), wx.ID_ANY, u"Sides", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )

        bSizer231.Add( self.m_staticText61, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_maskSidesChoices = [ u"Top", u"Bottom", u"Both"]
        self.m_maskSides = wx.Choice( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_maskSidesChoices, 0 )
        self.m_maskSides.SetSelection( 0 )
        bSizer231.Add( self.m_maskSides, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_MaskSidesTip = wx.StaticBitmap( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer231.Add( self.m_MaskSidesTip, 0, wx.ALL, 5 )


        bSizer231.Add( ( 0, 0), 1, 0, 5 )


        sbSoldermask.Add( bSizer231, 1, wx.EXPAND, 5 )

        bSizer241 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer241.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText71 = wx.StaticText( sbSoldermask.GetStaticBox(), wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText71.Wrap( -1 )

        bSizer241.Add( self.m_staticText71, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_maskColorChoices = [ u"Green", u"Blue", u"Black", u"Red", u"White" ]
        self.m_maskColor = wx.Choice( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_maskColorChoices, 0 )
        self.m_maskColor.SetSelection( 0 )
        self.m_maskColor.Enable( True )

        bSizer241.Add( self.m_maskColor, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_MaskColorTip = wx.StaticBitmap( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer241.Add( self.m_MaskColorTip, 0, wx.ALL, 5 )

        bSizer241.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        sbSoldermask.Add( bSizer241, 1, wx.EXPAND, 5 )

        bSizer2411 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2411.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText711 = wx.StaticText( sbSoldermask.GetStaticBox(), wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText711.Wrap( -1 )

        bSizer2411.Add( self.m_staticText711, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_maskFinishChoices = [ u"Standard (Semi-Gloss)" ]
        self.m_maskFinish = wx.Choice( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_maskFinishChoices, 0 )
        self.m_maskFinish.SetSelection( 0 )
        self.m_maskFinish.Enable( True )

        bSizer2411.Add( self.m_maskFinish, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_MaskFinishTip = wx.StaticBitmap( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2411.Add( self.m_MaskFinishTip, 0, wx.ALL, 5 )

        bSizer2411.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        sbSoldermask.Add( bSizer2411, 1, wx.EXPAND, 5 )

        bSizer2412 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer2412.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText712 = wx.StaticText( sbSoldermask.GetStaticBox(), wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText712.Wrap( -1 )

        bSizer2412.Add( self.m_staticText712, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_maskProcessChoices = [ u"LPI" ]
        self.m_maskProcess = wx.Choice( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_maskProcessChoices, 0 )
        self.m_maskProcess.SetSelection( 0 )
        self.m_maskProcess.Enable( True )

        bSizer2412.Add( self.m_maskProcess, 2, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_MaskTypeTip = wx.StaticBitmap( sbSoldermask.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2412.Add( self.m_MaskTypeTip, 0, wx.ALL, 5 )


        bSizer2412.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSoldermask.Add( bSizer2412, 1, wx.EXPAND, 5 )


        bSizer16.Add( sbSoldermask, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer15.Add( bSizer16, 0, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelSurface, wx.ID_ANY, u"Surface Finish" ), wx.VERTICAL )

        bSizer2311 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer2311.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText611 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText611.Wrap( -1 )

        bSizer2311.Add( self.m_staticText611, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_sufaceFinishChoices = [ u"Immersion Gold", u"HASL", u"Immersion Silver", u"Hard Gold", u"Soft Bondable Gold" ]
        self.m_sufaceFinish = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_sufaceFinishChoices, 0 )
        self.m_sufaceFinish.SetSelection( 0 )
        self.m_sufaceFinish.Enable( True )

        bSizer2311.Add( self.m_sufaceFinish, 3, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_FinishTypeTip = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2311.Add( self.m_FinishTypeTip, 0, wx.ALL, 5 )


        bSizer2311.Add( ( 0, 0), 2, 0, 5 )


        sbSizer8.Add( bSizer2311, 1, wx.EXPAND, 5 )

        bSizer23111 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer23111.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText6111 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Outer Layer Copper", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6111.Wrap( -1 )

        bSizer23111.Add( self.m_staticText6111, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_sufaceFinishThicknessChoices = [ u"1oz", u"2 oz" ]
        self.m_sufaceFinishThickness = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_sufaceFinishThicknessChoices, 0 )
        self.m_sufaceFinishThickness.SetSelection( 0 )
        bSizer23111.Add( self.m_sufaceFinishThickness, 3, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_FinishThickTip = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23111.Add( self.m_FinishThickTip, 0, wx.ALL, 5 )


        bSizer23111.Add( ( 0, 0), 2, 0, 5 )


        sbSizer8.Add( bSizer23111, 1, wx.EXPAND, 5 )

        bSizer231111 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer231111.Add( ( 0, 0), 2, wx.EXPAND, 5 )

        self.m_staticText61111 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Inner Layer Copper", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61111.Wrap( -1 )

        bSizer231111.Add( self.m_staticText61111, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_sufaceFinishThickness1Choices = [ u"1oz", u"2 oz", u"Not Applicable" ]
        self.m_sufaceFinishThickness1 = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_sufaceFinishThickness1Choices, 0 )
        self.m_sufaceFinishThickness1.SetSelection( 2 )
        bSizer231111.Add( self.m_sufaceFinishThickness1, 3, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_FinishThickTip1 = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer231111.Add( self.m_FinishThickTip1, 0, wx.ALL, 5 )


        bSizer231111.Add( ( 0, 0), 2, 0, 5 )


        sbSizer8.Add( bSizer231111, 1, wx.EXPAND, 5 )


        sbSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer17.Add( sbSizer8, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer15.Add( bSizer17, 0, wx.EXPAND, 5 )


        self.m_panelSurface.SetSizer( bSizer15 )
        self.m_panelSurface.Layout()
        bSizer15.Fit( self.m_panelSurface )
        self.m_notebook.AddPage( self.m_panelSurface, u"Surface", False )
        self.m_panelFinalize = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelFinalize, wx.ID_ANY, u"Board Options" ), wx.VERTICAL )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_NetlistTesting = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Electrical Netlist Testing", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_NetlistTesting, 0, wx.ALL, 5 )

        self.m_electricalTip = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_electricalTip, 0, wx.ALL, 5 )


        sbSizer5.Add( bSizer18, 0, 0, 5 )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_vendorMark = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Vendor Marking", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_vendorMark.SetValue(True)
        self.m_vendorMark.Enable( False )

        bSizer19.Add( self.m_vendorMark, 0, wx.ALL, 5 )

        self.m_VendorTip = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer19.Add( self.m_VendorTip, 0, wx.ALL, 5 )


        sbSizer5.Add( bSizer19, 0, 0, 5 )

        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_rohsMark = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"RoHS Marking", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rohsMark.Enable( False )

        bSizer20.Add( self.m_rohsMark, 0, wx.ALL, 5 )

        self.m_RoHSTip = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer20.Add( self.m_RoHSTip, 0, wx.ALL, 5 )


        sbSizer5.Add( bSizer20, 1, 0, 0 )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )


        bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizer5.Add( bSizer22, 1, wx.EXPAND, 5 )


        sbSizer5.Add( ( 0, 0), 5, wx.EXPAND, 5 )


        bSizer14.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )


        self.m_panelFinalize.SetSizer( bSizer13 )
        self.m_panelFinalize.Layout()
        bSizer13.Fit( self.m_panelFinalize )
        self.m_notebook.AddPage( self.m_panelFinalize, u"Finalize", False )

        bSizer5.Add( self.m_notebook, 10, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( ( 0, 0), 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_webRedirect = wx.Button( self, wx.ID_ANY, u"Quote using Sierra Circuits Website", wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.m_webRedirect.SetLabelMarkup( u"Quote using Sierra Circuits Website" )
        bSizer6.Add( self.m_webRedirect, 1, wx.ALIGN_CENTER, 5 )


        bSizer6.Add( ( 0, 0), 5, wx.EXPAND, 5 )

        self.m_validate = wx.Button( self, wx.ID_ANY, u"Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_validate, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        m_okCancel = wx.StdDialogButtonSizer()
        self.m_okCancelOK = wx.Button( self, wx.ID_OK )
        m_okCancel.AddButton( self.m_okCancelOK )
        self.m_okCancelCancel = wx.Button( self, wx.ID_CANCEL )
        m_okCancel.AddButton( self.m_okCancelCancel )
        m_okCancel.Realize();

        bSizer6.Add( m_okCancel, 1, wx.EXPAND, 20 )

        # self.m_validate = wx.Button( self, wx.ID_ANY, u"Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer6.Add( self.m_validate, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        bSizer5.Add( bSizer6, 2, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )

        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_UPDATE_UI, self.onUpdateUI )
        self.m_orderHisory.Bind( wx.EVT_BUTTON, self.onOrderHistory )
        self.m_highlightMinTrace.Bind( wx.EVT_BUTTON, self.onHighlightMinTrace )
        self.m_highlightMinSpace.Bind( wx.EVT_BUTTON, self.onHighlightMinSpace )
        self.m_innerMinTraceHighlight.Bind( wx.EVT_BUTTON, self.onHighlightMinInnerWidth )
        self.m_innerMinSpaceHighlight.Bind( wx.EVT_BUTTON, self.onHighlightMinInnerSpace )
        self.m_HighlightMinHole11.Bind( wx.EVT_BUTTON, self.onHighlightMinHole )
        self.m_Placeholder1.Bind( wx.EVT_BUTTON, self.onHighlightMinHole )
        self.m_HighlightMinHole.Bind( wx.EVT_BUTTON, self.onHighlightMinHole )
        self.m_webRedirect.Bind( wx.EVT_BUTTON, self.onRedirect )
        self.m_okCancelCancel.Bind( wx.EVT_BUTTON, self.onCancel )
        self.m_okCancelOK.Bind( wx.EVT_BUTTON, self.onQuote )
        self.m_validate.Bind( wx.EVT_BUTTON, self.onValidate )
        self.m_electricalTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipElectricNetTest )
        self.m_FinishThickTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipFinishThickTip )
        self.m_FinishTypeTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipFinishTypeTip )
        self.m_HolesCountTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipHolesCountTip )
        self.m_HolesDensityTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipHolesDensityTip )
        self.m_HolesMinRingTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipHolesMinRingTip )
        self.m_MaskColorTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMaskColorTip )
        self.m_MaskFinishTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMaskFinishTip )
        self.m_MaskSidesTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMaskSidesTip )
        self.m_minInnerTraceSpaceTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMinInnerTraceSpaceTip )
        self.m_minInnerTraceWidthTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMinInnerTraceWidthTip )
        self.m_minOuterTraceSpaceTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMinOuterTraceSpaceTip )
        self.m_minOuterTraceWidthTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMinOuterTraceWidthTip )
        self.m_platingTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipPlatingTip )
        self.m_RoHSTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipRoHSTip )
        self.m_SilkColorTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipSilkColorTip )
        self.m_materialTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMaterialTip )
        self.m_SilkSideTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipSilkSideTip )
        self.m_MaskTypeTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipMaskTypeTip )
        self.m_VendorTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipVendorTip )
        self.m_HolesMinSizeTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipHolesMinSizeTip )
        self.m_qtyTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipQtyTip )
        self.m_layThicknessTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipLayThicknessTip )
        self.m_ordHisTip.Bind( wx.EVT_LEFT_DOWN, self.onSetTipOrdHisTip )

    def __del__( self ):
        pass

    
                
    # Virtual event handlers, overide them in your derived class
    def onSetTipElectricNetTest(self, event):
        event.Skip()
    def onSetTipFinishThickTip(self, event):
        event.Skip()
    def onSetTipFinishTypeTip(self, event):
        event.Skip()
    def onSetTipHolesCountTip(self, event):
        event.Skip()
    def onSetTipHolesDensityTip(self, event):
        event.Skip()
    def onSetTipHolesMinRingTip(self, event):
        event.Skip()
    def onSetTipMaskColorTip(self, event):
        event.Skip()
    def onSetTipMaskFinishTip(self, event):
        event.Skip()
    def onSetTipMaskSidesTip(self, event):
        event.Skip()
    def onSetTipMinInnerTraceSpaceTip(self, event):
        event.Skip()
    def onSetTipMinInnerTraceWidthTip(self, event):
        event.Skip()
    def onSetTipMinOuterTraceSpaceTip(self, event):
        event.Skip()
    def onSetTipMinOuterTraceWidthTip(self, event):
        event.Skip()
    def onSetTipPlatingTip(self, event):
        event.Skip()
    def onSetTipRoHSTip(self, event):
        event.Skip()
    def onSetTipSilkColorTip(self, event):
        event.Skip()
    def onSetTipMaterialTip(self, event):
        event.Skip()
    def onSetTipSilkSideTip(self, event):
        event.Skip()
    def onSetTipMaskTypeTip(self, event):
        event.Skip()
    def onSetTipVendorTip(self, event):
        event.Skip()
    def onSetTipHolesMinSizeTip(self, event):
        event.Skip()
    def onSetTipQtyTip(self, event):
        event.Skip()
    def onSetTipLayThicknessTip(self, event):
        event.Skip()
    def onSetTipOrdHisTip(self, event):
        event.Skip()
    def onAction_m_quant1(self, event):
        event.Skip()
        # m_quant1 = self.m_quant1.GetValue().strip()
        # if m_quant1.isnumeric():
        #     pass
        # else:
        #     # dlg112 = wx.MessageDialog(self,"Service not Available", 'Validate Files', wx.OK | wx.ICON_ERROR)
        #     # dlg112.ShowModal()
        #     # dlg112.Destroy()  
        #     self.m_quant1.ChangeValue("")
    def onAction_m_quant2(self, event):
        event.Skip()
        
    def onAction_m_quant3(self, event):
        event.Skip()
    def onAction_m_quant4(self, event):
        event.Skip()
    
    def onUpdateUI( self, event ):
        event.Skip()

    def onSelectUnits( self, event ):
        event.Skip()

    def onChangeTraceUnits( self, event ):
        event.Skip()

    def onHighlightMinTrace( self, event ):
        event.Skip()


    def onHighlightMinSpace( self, event ):
        event.Skip()


    def onHighlightMinInnerWidth( self, event ):
        event.Skip()


    def onHighlightMinInnerSpace( self, event ):
        event.Skip()

    def onHighlightMinHole( self, event ):
        event.Skip()

    def onRedirect( self, event ):
        event.Skip()

    def onValidate( self, event ):
        event.Skip()

    def onCancel( self, event ):
        event.Skip()

    def onQuote( self, event ):
        event.Skip()

    def onOrderHistory( self, event ):
        event.Skip()

###########################################################################
## Class validateDialog
###########################################################################

class validateDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Validate Files", pos = wx.DefaultPosition, size = wx.Size( 494,314 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        # bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"messages", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText5.Wrap( -1 )

        bSizer8.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Error", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"messages", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"You can now click on Get Quote button", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText6.Wrap( -1 )

        bSizer8.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_ok, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        # bSizer7.Add( bSizer8, 3, wx.EXPAND, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.m_ok.Bind( wx.EVT_BUTTON, self.onOk )

    def __del__( self ):
        pass

    def onOk( self, event ):
        # event.Skip()
        self.Close()


###########################################################################
## Class orderHistoryDialog
###########################################################################

class orderHistoryDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u'Order History', pos = wx.DefaultPosition, size = wx.Size( 676,265  ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer67 = wx.BoxSizer( wx.VERTICAL )

        self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.BORDER_SUNKEN )
        bSizer67.Add( self.m_listCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
        # self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.m_listCtrl1)
        

        self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer67.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"* Disclaimer : Order amount is exclusive of tax, shipping and testing charges, if any.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText57.Wrap( -1 )

        bSizer67.Add( self.m_staticText57, 0, wx.ALL, 5 )

        self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"   Double click any of the orders to navigate to the customer portal", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText58.Wrap( -1 )

        bSizer67.Add( self.m_staticText58, 0, wx.ALL, 5 )

        self.SetSizer( bSizer67 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
   

###########################################################################
## Class uploadDialog
###########################################################################

class uploadDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 893,500 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

        self.m_bpButton1.SetBitmap( wx.NullBitmap )
        bSizer7.Add( self.m_bpButton1, 1, 0, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Sierra Circuits Online Quote", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Uploading...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer7.Add( bSizer8, 3, wx.EXPAND, 5 )


        bSizer5.Add( bSizer7, 3, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_uploadProgress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_uploadProgress.SetValue( 0 )
        bSizer131.Add( self.m_uploadProgress, 4, wx.ALL, 25 )


        bSizer5.Add( bSizer131, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_cancel, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 3, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_cancel.Bind( wx.EVT_BUTTON, self.onCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onCancel( self, event ):
        event.Skip()


###########################################################################
## Class matrixDialog
###########################################################################

class matrixDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 750,600 ), style = wx.DEFAULT_DIALOG_STYLE )
        self.SetDoubleBuffered(True)
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|wx.BORDER_NONE )
        try:
            self.m_bpButton1.SetBitmap( wx.NullBitmap )

        except:
            self.m_bpButton1.SetBitmap(wx.BitmapBundle(wx.NullBitmap ))  #modifiedbyvenky

        bSizer7.Add( self.m_bpButton1, 1, 0, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Sierra Circuits Online Quote", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer7.Add( bSizer8, 3, wx.EXPAND, 5 )


        bSizer5.Add( bSizer7, 4, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( ( 0, 0), 0, wx.EXPAND, 5 )

        bSizer66 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer66.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer67 = wx.BoxSizer( wx.VERTICAL )

        bSizer65 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_qtyLabel = wx.StaticText( self, wx.ID_ANY, u"Turn-Time", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_qtyLabel.Wrap( -1 )

        self.m_qtyLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer65.Add( self.m_qtyLabel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer67.Add( bSizer65, 1, wx.EXPAND, 5 )

        self.m_staticline88 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL ) #modifedbyvenky
        bSizer67.Add( self.m_staticline88,0, wx.ALL|wx.EXPAND, 5)

        self.t_qty1Text = wx.StaticText( self, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.t_qty1Text.Wrap( -1 )

        self.t_qty1Text.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer67.Add( self.t_qty1Text, 1,  wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        # self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        # self.m_staticline4.Hide()

        # bSizer67.Add( self.m_staticline4, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

        self.m_qty1Text = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_qty1Text.Wrap( -1 )

        self.m_qty1Text.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer67.Add( self.m_qty1Text, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty2Text = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_qty2Text.Wrap( -1 )

        self.m_qty2Text.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer67.Add( self.m_qty2Text, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty3Text = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_qty3Text.Wrap( -1 )

        self.m_qty3Text.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer67.Add( self.m_qty3Text, 1,  wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty4Text = wx.StaticText( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_qty4Text.Wrap( -1 )

        self.m_qty4Text.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer67.Add( self.m_qty4Text, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer66.Add( bSizer67, 2, wx.EXPAND, 5 )

        self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer66.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
        

        bSizer68 = wx.BoxSizer( wx.VERTICAL )

        bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_turn1 = wx.StaticText( self, wx.ID_ANY, u"2 days", wx.DefaultPosition, wx.DefaultSize)
        self.m_turn1.Wrap( -1 )

        self.m_turn1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer131.Add( self.m_turn1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_turn2 = wx.StaticText( self, wx.ID_ANY, u"3 days", wx.DefaultPosition, wx.DefaultSize)
        self.m_turn2.Wrap( -1 )

        self.m_turn2.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer131.Add( self.m_turn2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_turn3 = wx.StaticText( self, wx.ID_ANY, u"4 days", wx.DefaultPosition, wx.DefaultSize)
        self.m_turn3.Wrap( -1 )

        self.m_turn3.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer131.Add( self.m_turn3, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_turn4 = wx.StaticText( self, wx.ID_ANY, u"5 days", wx.DefaultPosition, wx.DefaultSize)
        self.m_turn4.Wrap( -1 )

        self.m_turn4.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer131.Add( self.m_turn4, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer131, 1, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer68.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 1 )

        ### Empty place for allignemt of price  tag - START
        bSizer1310 = wx.BoxSizer( wx.HORIZONTAL )

        self.t_qty11 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize)
        # self.t_qty11.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer1310.Add( self.t_qty11, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.t_qty12 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1310.Add( self.t_qty12, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.t_qty13 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1310.Add( self.t_qty13, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.t_qty14 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1310.Add( self.t_qty14, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer1310, 1, wx.EXPAND, 5 )
        ### Empty place for allignemt of price  tag - END

        bSizer1311 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_qty11 = wx.RadioButton( self, wx.ID_ANY, u"$50/ea", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.m_qty11.SetValue(True)
        # self.m_qty11.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer1311.Add( self.m_qty11, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty12 = wx.RadioButton( self, wx.ID_ANY, u"$40/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1311.Add( self.m_qty12, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty13 = wx.RadioButton( self, wx.ID_ANY, u"$32/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1311.Add( self.m_qty13, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty14 = wx.RadioButton( self, wx.ID_ANY, u"$30/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1311.Add( self.m_qty14, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer1311, 1, wx.EXPAND, 5 )

        bSizer13112 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_qty21 = wx.RadioButton( self, wx.ID_ANY, u"$50/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_qty21.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13112.Add( self.m_qty21, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty22 = wx.RadioButton( self, wx.ID_ANY, u"$40/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13112.Add( self.m_qty22, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty23 = wx.RadioButton( self, wx.ID_ANY, u"$32/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13112.Add( self.m_qty23, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty24 = wx.RadioButton( self, wx.ID_ANY, u"$30/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13112.Add( self.m_qty24, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer13112, 1, wx.EXPAND, 5 )

        bSizer131121 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_qty31 = wx.RadioButton( self, wx.ID_ANY, u"$50/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_qty31.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer131121.Add( self.m_qty31, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty32 = wx.RadioButton( self, wx.ID_ANY, u"$40/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131121.Add( self.m_qty32, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty33 = wx.RadioButton( self, wx.ID_ANY, u"$32/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131121.Add( self.m_qty33, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty34 = wx.RadioButton( self, wx.ID_ANY, u"$30/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131121.Add( self.m_qty34, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer131121, 1, wx.EXPAND, 5 )

        bSizer131122 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_qty41 = wx.RadioButton( self, wx.ID_ANY, u"$50/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_qty41.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer131122.Add( self.m_qty41, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty42 = wx.RadioButton( self, wx.ID_ANY, u"$40/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131122.Add( self.m_qty42, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty43 = wx.RadioButton( self, wx.ID_ANY, u"$32/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131122.Add( self.m_qty43, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_qty44 = wx.RadioButton( self, wx.ID_ANY, u"$30/ea", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131122.Add( self.m_qty44, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer68.Add( bSizer131122, 1, wx.EXPAND, 5 )


        bSizer66.Add( bSizer68, 8, wx.EXPAND, 5 )


        bSizer66.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer66, 6, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
##Added by Arun
        self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel14.Enable( True )
        bSizer1311111 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer1311111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer69 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText811111 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"NRE    :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText811111.Wrap( -1 )

        self.m_staticText811111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

        bSizer69.Add( self.m_staticText811111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText81111 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"e-Test  :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81111.Wrap( -1 )

        self.m_staticText81111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

        bSizer69.Add( self.m_staticText81111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText8111 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Total    :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8111.Wrap( -1 )

        self.m_staticText8111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer69.Add( self.m_staticText8111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer1311111.Add( bSizer69, 1, wx.EXPAND, 5 )

        bSizer70 = wx.BoxSizer( wx.VERTICAL )

        self.m_nre = wx.StaticText( self.m_panel14, wx.ID_ANY, u"$0    ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_nre.Wrap( -1 )

        self.m_nre.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

        bSizer70.Add( self.m_nre, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_etest = wx.StaticText( self.m_panel14, wx.ID_ANY, u"$250", wx.DefaultPosition, wx.DefaultSize,  0 )
        self.m_etest.Wrap( -1 )

        self.m_etest.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

        bSizer70.Add( self.m_etest, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_total = wx.StaticText( self.m_panel14, wx.ID_ANY, u"$250", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_total.Wrap( -1 )

        self.m_total.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer70.Add( self.m_total, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer1311111.Add( bSizer70, 1, wx.EXPAND, 5 )


        bSizer1311111.Add( ( 0, 0), 3, wx.EXPAND, 5 )

        self.m_panel14.SetSizer( bSizer1311111 )
        self.m_panel14.Layout()
        bSizer1311111.Fit( self.m_panel14 )
        bSizer5.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer688 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_webRedirect = wx.Button( self, wx.ID_ANY, u'Online Quote is not available. Please contact Sierra Circuits support', wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.m_webRedirect.SetLabelMarkup( u'Online Quote is not available. Please contact Sierra Circuits support.')
        bSizer688.Add( self.m_webRedirect, 1, wx.ALIGN_CENTER, 5 )


        bSizer688.Add( ( 0, 0), 5, wx.EXPAND, 5 )

        # self.m_validate = wx.Button( self, wx.ID_ANY, u"Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer688.Add( self.m_validate, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        m_okCancel = wx.StdDialogButtonSizer()
        self.m_okCancelOK = wx.Button( self, wx.ID_OK )
        m_okCancel.AddButton( self.m_okCancelOK )
        self.m_okCancelCancel = wx.Button( self, wx.ID_CANCEL )
        m_okCancel.AddButton( self.m_okCancelCancel )
        m_okCancel.Realize();

        bSizer688.Add( m_okCancel, 2, wx.EXPAND, 20 )

        bSizer5.Add( bSizer688, 1,wx.EXPAND, 5 )
        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )
        self.Fit()
        # Connect Events
        self.Bind( wx.EVT_UPDATE_UI, self.onUpdateUI )
        self.m_qty11.Bind( wx.EVT_RADIOBUTTON, self.onSelect11 )
        self.m_qty12.Bind( wx.EVT_RADIOBUTTON, self.onSelect12 )
        self.m_qty13.Bind( wx.EVT_RADIOBUTTON, self.onSelect13 )
        self.m_qty14.Bind( wx.EVT_RADIOBUTTON, self.onSelect14 )
        self.m_qty21.Bind( wx.EVT_RADIOBUTTON, self.onSelect21 )
        self.m_qty22.Bind( wx.EVT_RADIOBUTTON, self.onSelect22 )
        self.m_qty23.Bind( wx.EVT_RADIOBUTTON, self.onSelect23 )
        self.m_qty24.Bind( wx.EVT_RADIOBUTTON, self.onSelect24 )
        self.m_qty31.Bind( wx.EVT_RADIOBUTTON, self.onSelect31 )
        self.m_qty32.Bind( wx.EVT_RADIOBUTTON, self.onSelect32 )
        self.m_qty33.Bind( wx.EVT_RADIOBUTTON, self.onSelect33 )
        self.m_qty34.Bind( wx.EVT_RADIOBUTTON, self.onSelect34 )
        self.m_qty41.Bind( wx.EVT_RADIOBUTTON, self.onSelect41 )
        self.m_qty42.Bind( wx.EVT_RADIOBUTTON, self.onSelect42 )
        self.m_qty43.Bind( wx.EVT_RADIOBUTTON, self.onSelect43 )
        self.m_qty44.Bind( wx.EVT_RADIOBUTTON, self.onSelect44 )
        self.m_okCancelCancel.Bind( wx.EVT_BUTTON, self.onCancelClick )
        self.m_okCancelOK.Bind( wx.EVT_BUTTON, self.onOKClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onUpdateUI( self, event ):
        event.Skip()

    def onSelect11( self, event ):
        event.Skip()

    def onSelect12( self, event ):
        event.Skip()

    def onSelect13( self, event ):
        event.Skip()

    def onSelect14( self, event ):
        event.Skip()

    def onSelect21( self, event ):
        event.Skip()

    def onSelect22( self, event ):
        event.Skip()

    def onSelect23( self, event ):
        event.Skip()

    def onSelect24( self, event ):
        event.Skip()

    def onSelect31( self, event ):
        event.Skip()

    def onSelect32( self, event ):
        event.Skip()

    def onSelect33( self, event ):
        event.Skip()

    def onSelect34( self, event ):
        event.Skip()

    def onSelect41( self, event ):
        event.Skip()

    def onSelect42( self, event ):
        event.Skip()

    def onSelect43( self, event ):
        event.Skip()

    def onSelect44( self, event ):
        event.Skip()

    def onCancelClick( self, event ):
        event.Skip()

    def onOKClick( self, event ):
        event.Skip()
