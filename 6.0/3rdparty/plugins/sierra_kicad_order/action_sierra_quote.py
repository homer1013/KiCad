#  action_sierra_quote.py
#
#  Copyright (C) 2019 Sierra Circuits, Inc
#
#  Designed by KiCad Services, Inc.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import wx
import pcbnew
import logging
import os
import sys
import math
import configparser
import json
import webbrowser
import ssl
import re
import urllib.request, urllib.parse, urllib.error
from . import  globalVars
import urllib.request, urllib.error, urllib.parse

# import superAPI
# # from . import localStoragePy
# from localStoragePy import localStoragePy
# Big Warning flags here.
# We don't have a default way to find/utilize a known certificate list
# So we don't use certificates. :*(
ssl._create_default_https_context = ssl._create_unverified_context
from collections import defaultdict


VERSION = "2.0"
FORGOT_PASSWORD_LINK = globalVars.FEMSBackendURL + "/user/forgot_pass_mail.jsp"
CREATE_ACCOUNT_LINK = globalVars.FEMSBackendURL + "/chklogin.jsp"

logo_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "images" + os.path.sep + "logo.png"



#KiCad 6.0 Changes
# config_path = pcbnew.GetKicadConfigPath()
config_path = pcbnew.SETTINGS_MANAGER_GetUserSettingsPath()
# config_path = "C:/Users/Lenovo/AppData/Roaming/kicad"
from . import  drill_info
config_file = os.path.join(config_path, "sierra_plugin.cfg")


class Unit:
    INCHES = 0
    MM = 1

    @staticmethod
    def ToInches(value):
        return value / 2.54e+7

    @staticmethod
    def ToMil(value):
        return value / 2.54e+4

    @staticmethod
    def ToMM(value):
        return value / 1e+6

    @staticmethod
    def FromInches(value):
        return value * 2.54e+7

    @staticmethod
    def FromMil(value):
        return value * 2.54e+4

    @staticmethod
    def FromMM(value):
        return value * 1e+6

# import gui and API module
from . import sierra_API
from .sierra_API import sierra_api
from . import generate_gerber_archive
from .generate_gerber_archive import GenerateProduction
from . import sierra_order_GUI
from .sierra_order_GUI import loginDialog, uploadDialog, matrixDialog

from . import sierra_quote_dialog
from .sierra_quote_dialog import QuoteDialog

caption = 'Sierra Circuits Quote'
class LoginDialog (sierra_order_GUI.loginDialog):
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(LoginDialog, self).SetSizeHints(sz1, sz2)

    def ShowNetworkErrorDialog(self):
            self.ShowUnknownErrorDialog( "Network error trying to contact quote server" )

    def ShowLoginErrorDialog(self):
            self.ShowUnknownErrorDialog( "Email address or password incorrect" )

    def ShowUnknownErrorDialog(self, msg):
            dlg = wx.MessageDialog(self, msg, caption, wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

    def ShowRegistrationSuccessDialog(self, msg):
        dlg = wx.MessageDialog(self, str(msg), caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def validateMail(self, maile):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,maile)):
            return True
        else:
            return False


    def __init__(self, parent, api):
        sierra_order_GUI.loginDialog.__init__(self, parent)
        self.api = api
        self.SetDefaultItem( self.m_login )
        self.SetAffirmativeId( self.m_login.GetId() )
        self.SetEscapeId( wx.ID_CANCEL )
        try:
            self.m_bpButton1.SetBitmap(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG))
        except:
            self.m_bpButton1.SetBitmap(wx.BitmapBundle(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG)))
        self.Fit()

        width, discard = self.GetTextExtent('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        discard, height = self.GetSize()
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.SetSize((width, height))

        if( api.RegisterPlugin() is not True ):
            if( self.api.last_error == self.api.NETWORK_ERROR ):
                self.ShowNetworkErrorDialog()
            elif( self.api.last_error == self.api.AUTH_ERROR ):
                self.ShowLoginErrorDialog()
            else:
                self.ShowUnknownErrorDialog( "Unknown Error" )

    def onForgotPassword(self, event):
        # webbrowser.open( FORGOT_PASSWORD_LINK )
        self.m_panel6.Hide()
        self.m_panel9.Enable( True )
        self.m_panel9.Show()
        self.m_resetEmail.SetValue(self.api.username)

        event.Skip()

    def onCCPA(self, event):
        webbrowser.open(globalVars.FEMSBackendURL + '/ccpa-compliance')
        event.Skip()

    def onLogin(self, event):
        if( self.api.registered is not True ):
            if( self.api.RegisterPlugin() is not True ):
                self.ShowNetworkErrorDialog()
                event.Skip( False )
                return

        self.api.SetUsername( self.m_username.GetValue() )
        self.api.SetPassword( self.m_password.GetValue() )
        

        if(( self.m_username.GetValue() == "" ) and ( self.m_password.GetValue() == "" )):
            self.ShowUnknownErrorDialog( "Email address/password can't be blank" )
            return
        elif( self.m_username.GetValue() == "" ):
            self.ShowUnknownErrorDialog( "Email address can't be blank" )
            return
        elif( self.m_password.GetValue() == "" ):
            self.ShowUnknownErrorDialog( "Password can't be blank" )
            return
        else:
            None
            

        try:
            self.api.Login()
        except Exception as e:
            self.ShowUnknownErrorDialog( str( e ) )
            return

        if( self.api.logged_in is not True ):
            self.api.last_error -= 1
            if( self.api.last_error == self.api.NETWORK_ERROR ):
                self.ShowNetworkErrorDialog()
            elif( self.api.last_error == self.api.AUTH_ERROR ):
                self.ShowLoginErrorDialog()
            else:
                self.ShowUnknownErrorDialog( "Unknown Error" )

            event.Skip( False )
            return

        if (self.api.force_password_reset):
            self.m_panel6.Hide()
            self.m_panel10.Enable( True )
            self.m_panel10.Show()
            event.Skip( False )
            return

        event.Skip()


    def onCreateAccount(self, event):
        # webbrowser.open( CREATE_ACCOUNT_LINK )
        # self.Hide()
        self.m_panel6.Hide()
        self.m_panel7.Enable( True )
        self.m_panel7.Show()
        # self.m_panel7.Layout()
        event.Skip()

    def onRegCancel( self, event ):
        self.m_email.SetValue("")
        self.m_rgpassword.SetValue("")
        self.m_confirmpassword.SetValue("")
        self.m_firstname.SetValue("")
        self.m_lastname.SetValue("")
        self.m_company.SetValue("")
        self.m_phonenumber.SetValue("")
        self.m_panel7.Hide()
        self.m_panel6.Show()
        event.Skip()

    def onRegister( self, event ):

        rgdata = {'email' : self.m_email.GetValue(), 'password': self.m_rgpassword.GetValue(), 'confPassword': self.m_confirmpassword.GetValue(),
        'firstName': self.m_firstname.GetValue(),'lastName': self.m_lastname.GetValue(),'company': self.m_company.GetValue(),
        'phoneNo': self.m_phonenumber.GetValue()}

        # rgdata = {'email' : self.m_email.GetValue(), 'password': "arun123", 'firstName': "arun",
        #     'lastName': "mehra",'company': "sierra", 'phoneNo': "7415121322"}
        for key in rgdata:
            if not rgdata[key].strip():
                raise self.ShowUnknownErrorDialog( "All Fields are Mandatory" )

        if not self.validateMail(str(rgdata["email"])):
            self.ShowUnknownErrorDialog( "Please Type Valid Email Address" )
        elif len(rgdata["password"]) < 5 or len(rgdata["password"]) > 50:
            self.ShowUnknownErrorDialog( "Password Length Should be between 5 and 50 Characters" )
        elif rgdata["password"] != rgdata["confPassword"]:
            self.ShowUnknownErrorDialog( "Password is not matching with confirm password" )
        elif not all(map(str.isalpha, str(rgdata["firstName"]))):
            self.ShowUnknownErrorDialog( "Please Type Valid First Name, Letters only" )
        elif not all(map(str.isalpha, str(rgdata["lastName"]))):
            self.ShowUnknownErrorDialog( "Please Type Valid Last Name, Letters only" )
        elif len(rgdata["company"]) < 2 or len(rgdata["company"]) > 250:
            self.ShowUnknownErrorDialog( "Company name is Mandatory, between 2 and 250 characters" )
        elif not all(map(str.isdigit, str(rgdata["phoneNo"]))):
            self.ShowUnknownErrorDialog( "Please Type Valid Phone Number" )
        elif len(rgdata["phoneNo"]) < 10:
            self.ShowUnknownErrorDialog( "Phone No should be atleast 10 characters" )    
        
        
        else:
            # self.m_panel7.Hide()
            # self.m_panel6.Show()
            if( self.api.registered is not True ):
                if( self.api.RegisterPlugin() is not True ):
                    self.ShowNetworkErrorDialog()
                    event.Skip( False )
                    return

            try:
                self.api.SetRegistration(rgdata)
            except Exception as e:
                self.ShowUnknownErrorDialog( str(e))
                return

            if( self.api.new_registration ):
                self.ShowRegistrationSuccessDialog(self.api.registration_msg)
                self.m_email.SetValue("")
                self.m_rgpassword.SetValue("")
                self.m_confirmpassword.SetValue("")
                self.m_firstname.SetValue("")
                self.m_lastname.SetValue("")
                self.m_company.SetValue("")
                self.m_phonenumber.SetValue("")
                self.m_panel7.Hide()
                self.m_panel6.Show()
            else:
                self.ShowUnknownErrorDialog( str(self.api.registration_msg) )
                # self.ShowUnknownErrorDialog( str(rgdata) )

        event.Skip()

    def onReset( self, event ):
        resetemail = self.m_resetEmail.GetValue()
        if not self.validateMail(resetemail):
            self.ShowUnknownErrorDialog( "Please Type Valid Email Address" )

        else:
            try:
                self.api.ResetPassword(resetemail)
            except Exception as e:
                self.ShowUnknownErrorDialog( str(e))
                return

            if( self.api.resetpass ):
                self.ShowRegistrationSuccessDialog( "Password reset successfully. Please check your email for new password" )

            else:
                self.ShowUnknownErrorDialog( "Email is not Registered" )

            # caption = 'Sierra Circuits Quote'
            # dlg = wx.MessageDialog(self, u'Password reset successfully. Please check your email for new password', caption, wx.OK | wx.ICON_INFORMATION)
            # dlg.ShowModal()
            # dlg.Destroy()
            self.m_panel9.Hide()
            self.m_panel6.Show()
            # event.Skip()

    def onResetCancel( self, event ):
        self.m_panel9.Hide()
        self.m_panel6.Show()
        self.m_password.SetValue("")
        event.Skip()

    def onChangePassword( self, event ):
        pswdata = {'old': self.m_uPassword11.GetValue(), 'new': self.m_uNewPassword1.GetValue()}

        for key in pswdata:
            if not pswdata[key].strip():
                raise self.ShowUnknownErrorDialog( "All Fields are Mandatory" )

        if len(pswdata['new']) < 5:
            self.ShowUnknownErrorDialog( str(pswdata['new']) )
        else:
            try:
                if( self.api.UpdatePassword(pswdata)):
                    self.api.force_password_reset = False
                    self.m_password.SetValue("")
                    self.ShowRegistrationSuccessDialog( "Password Change successfully. Please login with new password" )
                else:
                    self.ShowUnknownErrorDialog( "Email is not Registered" )

            except Exception as e:
                self.ShowUnknownErrorDialog( str(e))
                event.Skip( False )

            self.m_panel10.Hide()
            self.m_panel6.Show()
        # event.Skip()

    def onChangeCancel( self, event ):
        self.m_panel10.Hide()
        self.m_password.SetValue("")
        self.m_panel6.Show()
        event.Skip()

##########
##########
class UploadDialog (sierra_order_GUI.uploadDialog):
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(UploadDialog, self).SetSizeHints(sz1, sz2)
    def __init__(self, parent):
        sierra_order_GUI.uploadDialog.__init__(self, parent)
        self.m_bpButton1.SetBitmap(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG))
        self.Fit()
        width, discard = self.GetTextExtent('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        discard, height = self.GetSize()
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.SetSize((width, height))


class MatrixDialog(sierra_order_GUI.matrixDialog):
    use_etest = 0
    unit_select = 11
    turn_list = ()
    qty_list = ()
    data = defaultdict(dict)
    wmqID = ""
    iscl = 0
    isVal = 0
    eTest = ""

    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(MatrixDialog, self).SetSizeHints(sz1, sz2)
    def __init__(self, parent):
        sierra_order_GUI.matrixDialog.__init__(self, parent)
        self.SetDoubleBuffered(True)
        try:
            self.m_bpButton1.SetBitmap(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG))
        except:
            self.m_bpButton1.SetBitmap(wx.BitmapBundle(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG)))  #modifiedbyvenky
        # Hide the extra turn time elements
        # self.m_turn2.Hide()
        # self.m_qty21.Hide()
        # self.m_qty22.Hide()
        # self.m_qty23.Hide()
        # self.m_qty24.Hide()
        self.m_turn3.Hide()
        self.m_turn4.Hide()
        self.m_qty13.Hide()
        self.m_qty23.Hide()
        self.m_qty33.Hide()
        self.m_qty43.Hide()
        self.m_qty14.Hide()
        self.m_qty24.Hide()
        self.m_qty34.Hide()
        self.m_qty44.Hide()

        self.Fit()
        width, discard = self.GetTextExtent('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        height = width * 2 / 3 + self.m_bpButton1.GetBitmap().GetHeight()
        # discard, height = self.GetSize()
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.SetSize((width, height))

    def onSelect11(self, event):
        self.unit_select = 11
        self.m_qty11.SetValue(True)
    def onSelect12(self, event):
        self.unit_select = 21
        self.m_qty12.SetValue(True)
    def onSelect13(self, event):
        self.unit_select = 31
        self.m_qty13.SetValue(True)
    def onSelect14(self, event):
        self.unit_select = 41
        self.m_qty14.SetValue(True)
    def onSelect21(self, event):
        self.unit_select = 12
        self.m_qty21.SetValue(True)
    def onSelect22(self, event):
        self.unit_select = 22
        self.m_qty22.SetValue(True)
    def onSelect23(self, event):
        self.unit_select = 32
        self.m_qty23.SetValue(True)
    def onSelect24(self, event):
        self.unit_select = 42
        self.m_qty24.SetValue(True)
    def onSelect31(self, event):
        self.unit_select = 13
        self.m_qty31.SetValue(True)
    def onSelect32(self, event):
        self.unit_select = 23
        self.m_qty32.SetValue(True)
    def onSelect33(self, event):
        self.unit_select = 33
        self.m_qty33.SetValue(True)
    def onSelect34(self, event):
        self.unit_select = 43
        self.m_qty34.SetValue(True)
    def onSelect41(self, event):
        self.unit_select = 14
        self.m_qty41.SetValue(True)
    def onSelect42(self, event):
        self.unit_select = 24
        self.m_qty42.SetValue(True)
    def onSelect43(self, event):
        self.unit_select = 34
        self.m_qty43.SetValue(True)
    def onSelect44(self, event):
        self.unit_select = 44
        self.m_qty44.SetValue(True)

    def onUpdateUI(self, event):
        # for i in range(1, 5):
        #     for j in range(1, 5):
        #         getattr(self, 'm_qty' + str(i) + str(j)).SetValue(True)
        
        qty = self.qty_list[int(self.unit_select % 10 - 1)]
        turn = self.turn_list[int(self.unit_select / 10 - 1)]
        # getattr(self, 'm_qty' + str(self.unit_select)).SetValue(True)

        # self.m_etest.SetDoubleBuffered(True)

        if self.use_etest:
            # self.m_etest.SetDoubleBuffered(True)
            self.eTest = str("%.2f" % self.data[qty][turn][1])
            self.m_etest.SetLabelText('$' + str("%.2f" % self.data[qty][turn][1]))
            # self.m_etest.SetLabelText('$0')
            self.m_total.SetLabelText('$' + str("%.2f" %  (qty*self.data[qty][turn][2]+self.data[qty][turn][1])))

        else:
        # self.m_etest.SetDoubleBuffered(True)
            self.m_etest.SetLabelText('$0')
            # self.m_etest.SetLabelText('$' + str(self.data[qty][turn][1]))
            self.m_total.SetLabelText('$' + str("%.2f" % (qty* self.data[qty][turn][2]+0)))

        event.Skip()

    def setReturnMatrix(self, retval):
        self.data = defaultdict(dict)
        self.m_webRedirect.Hide()
        # self.m_panel12.Hide()
        for item in retval['webQuoteMatrix']:
            try:
                qty = int(item['quantity'])
                days = int(item['turntime'])
                test = float(item['testingPrice'])
                unit = float(item['unitPrice'])
                iscall = bool(item['isCallUs'] != '0')

                # Only supporting 5-days right now
                # if days == 5:
                #     self.data[qty][days] = (iscall, test, unit)
                self.data[qty][days] = (iscall, test, unit)
            except:
                continue
        self.qty_list = []
        self.qty_list = list(self.data)
        self.qty_list.sort()
        # self.qty_list = ["1","2","3","4"]
        # print(self.qty_list)
        # if len(self.qty_list) < 4:
        #     self.m_qty4Text.Hide()
        #     self.m_qty14.Hide()
        #     self.m_qty24.Hide()
        #     self.m_qty34.Hide()
        #     self.m_qty44.Hide()
        # if len(self.qty_list) < 3:
        #     self.m_qty3Text.Hide()
        #     self.m_qty13.Hide()
        #     self.m_qty23.Hide()
        #     self.m_qty33.Hide()
        #     self.m_qty43.Hide()
        # if len(self.qty_list) < 2:
        #     self.m_qty2Text.Hide()
        #     self.m_qty12.Hide()
        #     self.m_qty22.Hide()
        #     self.m_qty32.Hide()
        #     self.m_qty42.Hide()

        try:
            self.m_qty1Text.SetLabelText(str(self.qty_list[0]))
            self.m_qty2Text.SetLabelText(str(self.qty_list[1]))
            self.m_qty3Text.SetLabelText(str(self.qty_list[2]))
            self.m_qty4Text.SetLabelText(str(self.qty_list[3]))
        except:
            pass

        self.turn_list = []       
        self.turn_list = list(self.data[self.qty_list[0]])
        self.turn_list.sort()

        try:
            self.m_turn1.SetLabelText(str(self.turn_list[0]) + ' Days')
            self.m_turn2.SetLabelText(str(self.turn_list[1]) + ' Days')
            self.m_turn3.SetLabelText(str(self.turn_list[2]) + ' Days')
            self.m_turn4.SetLabelText(str(self.turn_list[3]) + ' Days')
        except:
            pass


        for i in range(len(self.qty_list)):
            for j in range(len(self.turn_list)):
            #j = 0
                try:
                    qty = self.qty_list[i]
                    #turn = 5 # We only support 5-day turn time at the moment.  Otherwise, use self.turn_list[j]
                    turn = self.turn_list[j]
                    if self.data[qty][turn][0]:
                        self.iscl = 1
                        getattr(self, 'm_qty' + str(i + 1) + str(j + 1)).SetLabelText('Call Us')
                        getattr(self, 'm_qty' + str(i + 1) + str(j + 1)).Disable()
                    else:
                        self.isVal = 1
                        getattr(self, 'm_qty' + str(i + 1) + str(j + 1)).SetLabelText('$'+str("%.2f" % self.data[qty][turn][2]))
                except:
                    self.m_panel14.Hide()
                    self.m_webRedirect.Show()
                    self.m_okCancelOK.Disable()

        if self.iscl and self.isVal:
            # self.m_webRedirect.Show()
            self.m_panel14.Hide()
            self.m_webRedirect.Show()
            self.m_okCancelOK.Disable()
            for i in range(len(self.qty_list)):
                for j in range(len(self.turn_list)):
                    getattr(self, 'm_qty' + str(i + 1) + str(j + 1)).Disable()
            
        elif self.iscl:
            self.m_panel14.Hide()
            self.m_webRedirect.Show()
            self.m_okCancelOK.Disable()

        self.wmqID = retval['wmqID']

    def getWebData(self):
        return {'eTest' : self.eTest, 'wmqId': self.wmqID,'selectedQuantity': str(self.qty_list[int(self.unit_select % 10 - 1)]),'selectedTurntime': str(self.turn_list[int(self.unit_select / 10 - 1)])}


class Segment:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, track):
        self.x1 = track.GetStart().x
        self.y1 = track.GetStart().y
        self.x2 = track.GetEnd().x
        self.y2 = track.GetEnd().y

    def segments_intersect(self, other):
        """ whether two segments in the plane intersect
        """
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        da = other.x2 - other.x1
        db = other.y2 - other.y1
        delta = float(da * dy - db * dx)
        if delta == 0.0:
            return False  # parallel segments

        s = (dx * (other.y1 - self.y1) + dy * (self.x1 - other.x1)) / delta
        t = (da * (self.y1 - other.y1) + db * (other.x1 - self.x1)) / (-delta)
        return (0 <= s <= 1) and (0 <= t <= 1)

    def point_segment_distance(self, px, py, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx == dy == 0:
            return math.hypot(px - x1, py - y1)

        t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

        # Is this an endpoint or in the middle?
        if t < 0:
            dx = px - x1
            dy = py - y1
        elif t > 1:
            dx = px - x2
            dy = py - y2
        else:
            near_x = x1 + t * dx
            near_y = y1 + t * dy
            dx = px - near_x
            dy = py - near_y

        return math.hypot(dx, dy)

    def segments_distance(self, other):
        """ distance between two segments in the plane"""

        if self.segments_intersect(other):
            return 0

        # try each of the 4 vertices w/the other segment
        distances = []
        distances.append(self.point_segment_distance(self.x1, self.y1, other.x1, other.y1, other.x2, other.y2))
        distances.append(self.point_segment_distance(self.x2, self.y2, other.x1, other.y1, other.x2, other.y2))
        distances.append(self.point_segment_distance(other.x1, other.y1, self.x1, self.y1, self.x2, self.y2))
        distances.append(self.point_segment_distance(other.x2, other.y2, self.x1, self.y1, self.x2, self.y2))

        return min(distances)

class RequestQuote(pcbnew.ActionPlugin):
    """
    An action plugin to request online quotes from KiCad
    """

    def defaults(self):
        self.name = "Sierra Circuits Quote"
        self.category = "Quoting"
        self.description = "Request an online quote from Sierra Circuits"
        # self.show_toolbar_button = True #if we wants toolbar action button then True will be the value
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), 'sierra_icon32.png')

    def GetBoardDims(self, outlines):

        outline = outlines.Outline(0)
        #kicad 6.0 changes
        # outline_points = [outline.Point(n) for n in range(outline.PointCount())]
        outline_points = [outline.CPoint(n) for n in range(outline.PointCount())]
        outline_maxx = max([p.x for p in outline_points])
        outline_minx = min([p.x for p in outline_points])
        outline_maxy = max([p.y for p in outline_points])
        outline_miny = min([p.y for p in outline_points])

        return( outline_maxx - outline_minx, outline_maxy - outline_miny )

    def GetMinOuterTraceWidth( self, board ):

        traces = defaultdict(list)

        for track in board.GetTracks():
            if( track.GetLayer() == pcbnew.F_Cu or track.GetLayer() == pcbnew.B_Cu ):
                traces[ str( track.GetWidth() ).rjust( 12, '0' ) ].append( track )

        if( len( traces ) > 0 ):
            return sorted(traces.items())[0][1]

        return None

    def GetMinInnerTraceWidth( self, board ):

        traces = defaultdict(list)

        for track in board.GetTracks():
            if( track.GetLayer() != pcbnew.F_Cu and track.GetLayer() != pcbnew.B_Cu ):
                traces[ str( track.GetWidth() ).rjust( 12, '0' ) ].append( track )

        if( len( traces ) > 0 ):
            return sorted(traces.items())[0][1]

        return None

    def GetMinSpace( self, board ):
        inner_traces = None
        inner_trace_space = sys.maxsize
        outer_traces = None
        outer_trace_space = sys.maxsize

        from itertools import combinations
        for track1, track2 in combinations(board.GetTracks(), 2):
            if track1.GetNetCode() == track2.GetNetCode():
                continue
            if track1.GetLayer() != track2.GetLayer():
                continue

            if (track1.Type() == pcbnew.PCB_TRACE_T and track2.Type() == pcbnew.PCB_TRACE_T):
                seg1 = Segment(track1)
                seg2 = Segment(track2)
                dist = seg1.segments_distance(seg2) - track1.GetWidth() / 2 - track2.GetWidth() / 2

                if dist <= 0:
                    track1.SetHighlighted()
                    track2.SetHighlighted()

                if ((track1.GetLayer() == pcbnew.F_Cu or track1.GetLayer() == pcbnew.B_Cu)
                        and dist < outer_trace_space):
                    outer_trace_space = dist
                    outer_traces = (track1, track2)

                if ((track1.GetLayer() != pcbnew.F_Cu and track1.GetLayer() != pcbnew.B_Cu)
                        and dist < inner_trace_space):
                    inner_trace_space = dist
                    inner_traces = (track1, track2)

        pcbnew.Refresh()
        try:
            pcbnew.UpdateUserInterface()
        except:
            pass

        return inner_traces, inner_trace_space, outer_traces, outer_trace_space


    def GetDrills(self, board):
        min_drill_size = sys.maxsize
        min_ring_size = sys.maxsize
        min_drill = 0
        min_ring = 0
        total_drills = 0

        for track in board.GetTracks():
            if (track.Type() == pcbnew.PCB_VIA_T):
                total_drills = total_drills + 1
                if (track.GetDrillValue() < min_drill_size):
                    min_drill_size = track.GetDrillValue()
                    min_drill = track

                ring = (track.GetWidth() - track.GetDrillValue()) / 2
                if (ring < min_ring_size):
                    min_ring_size = ring
                    min_ring = track

        # Note: Should we separate the drill-drag from the route command?
        for pad in board.GetPads():
            size = pad.GetDrillSize()
            min_size = min([size.x, size.y])
            max_size = max([size.x, size.y])

            #kicad 6.0 changes
            if (pad.GetAttribute() == pcbnew.PAD_ATTRIB_NPTH or pad.GetAttribute() == pcbnew.PAD_ATTRIB_PTH):
            # if (pad.GetAttribute() == pcbnew.PAD_ATTRIB_HOLE_NOT_PLATED or pad.GetAttribute() == pcbnew.PAD_ATTRIB_STANDARD):
                total_drills = total_drills + 1
                if (min_size < min_drill_size):
                    min_drill_size = min_size
                    min_drill = pad

            #kicad 6.0 changes
            # if (pad.GetAttribute() == pcbnew.PAD_ATTRIB_STANDARD):
            if (pad.GetAttribute() == pcbnew.PAD_ATTRIB_PTH):
                # poly = pcbnew.SHAPE_POLY_SET()
                poly = pad.GetEffectivePolygon()
                inflate = pcbnew.wxSize(0,0)
                #kicad 6.0 changes
                # pad.BuildEffectivePolygon(poly, inflate, 16, 1.0 / math.cos(math.pi / 16))
                pad.BuildEffectivePolygon()
                # pad.TransformHoleWithClearanceToPolygon(poly, 0, 16, "")
                outline = poly.COutline(0)
                # Note: This does potentially over estimate oblong drill hits
                d = outline.Distance(pcbnew.VECTOR2I(pad.GetOffset()), True) - max_size / 2
                if (d < min_ring_size):
                    min_ring_size = d
                    min_ring = pad
        return min_drill, min_ring, min_drill_size, min_ring_size, total_drills

    def GetCutouts( self, board ):

        outlines = pcbnew.SHAPE_POLY_SET()
        return outlines.HoleCount( 0 )

    def Run(self):
#Added
        wait_main_dialog = wx.BusyInfo("Opening Sierra Circuits Plugin")
        self.wait_main_dialog_flag = False
##
        # load board
        board = pcbnew.GetBoard()
        outlines = pcbnew.SHAPE_POLY_SET()
        board.GetBoardPolygonOutlines(outlines)
        config = configparser.ConfigParser(allow_no_value=True)
        # go to the project folder - so that log will be in proper place
        board_path = os.path.dirname( os.path.realpath( board.GetFileName() ) ) + os.path.sep
        # Remove all handlers associated with the root logger object.
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        # set up logger
        try:
            logging.basicConfig(level=logging.DEBUG,
                                filename= board_path + "sierra_quote.log",
                                filemode='w',
                                format='%(asctime)s %(name)s %(lineno)d:%(message)s',
                                datefmt='%m-%d %H:%M:%S')
        except:
            # If we can't write to the file, just use STDERR
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(name)s %(lineno)d:%(message)s',
                                datefmt='%m-%d %H:%M:%S')
        logger = logging.getLogger(__name__)
        logger.info("Sierra Circuits Quote plugin version: " + VERSION + " started")
        stdout_logger = logging.getLogger('STDOUT')
        sl = StreamToLogger(stdout_logger, logging.INFO)
        sys.stdout = sl
        stderr_logger = logging.getLogger('STDERR')
        sl = StreamToLogger(stderr_logger, logging.ERROR)
        sys.stderr = sl
        # Load the configuration
        config.read(config_file)
        # Init the API
        api = sierra_api(logger)
        try:
            api.username = config.get("MAIN","username")
        except:
            pass
        try:
            api.refresh_token = config.get("MAIN", "refresh")
        except:
            pass
        try:
            api.uuid = config.get("MAIN", "uuid")
        except:
            pass
        # find pcbnew frame
        #JiCad 6.0 Changes
        # _pcbnew_frame = [x for x in wx.GetTopLevelWindows() if x.GetTitle().lower().startswith('pcbnew')][0]
        _pcbnew_frame = [x for x in wx.GetTopLevelWindows() if 'pcb editor' in x.GetTitle().lower()][0]
        # try to get back without logging in
        if not api.RefreshPlugin(api.refresh_token):
            if not self.wait_main_dialog_flag:
                del wait_main_dialog
                self.wait_main_dialog_flag = True
            # show login dialog
            main_dialog = LoginDialog(_pcbnew_frame, api)
            if (api.username !=  ""):
                main_dialog.m_username.SetValue(api.username)
                main_dialog.m_password.SetFocus()

            main_res = main_dialog.ShowModal()
            if main_res != main_dialog.m_login.GetId():
                main_dialog.Destroy()
                logging.shutdown()
                return

            main_dialog.Destroy()
##Added
        if not self.wait_main_dialog_flag:
            del wait_main_dialog
            self.wait_main_dialog_flag = True

        wait_quote_dialog = wx.BusyInfo("Opening Quote Dialog")##
        # We successfully logged in. Let's save the last username
        try:
            config.add_section("MAIN")
        except:
            pass

        try:
            config.set("MAIN", "username", api.username)
            config.set("MAIN", "refresh", api.refresh_token)
            config.set("MAIN", "uuid", str(api.uuid))
            with open(config_file, 'w') as configfile:
                config.write(configfile)
        except:
            logger.info("Could not save config file " + config_file)
            pass

        quote_dialog = QuoteDialog(_pcbnew_frame, logo_path, board)

        cred = api.GetCredentials()
        quote_dialog.setuserid = cred["user_id"]
        quote_dialog.setaccesstoken = cred["access_token"]
        quote_dialog.setsessionid= cred["session_id"]
        
        globalVars.userId = cred["user_id"]
        globalVars.accessToken =  cred["access_token"]
        try:
            toolTipReq = urllib.request.Request(globalVars.kicadBackendURL + "/getToolTips?project=KIP", headers={'Content-Type' : 'application/json'})
            toolTipRes = urllib.request.urlopen(toolTipReq)
            toolTipRes = toolTipRes.read().decode("utf-8") 
            toolTipRes = json.loads(toolTipRes)
            if toolTipRes['success']:
                globalVars.toolTips = toolTipRes['toolTips']
                globalVars.maxQty = toolTipRes['maxQty']
                toolTips = toolTipRes['toolTips']
                quote_dialog.m_electricalTip.Enable(True)
                quote_dialog.m_electricalTip.SetToolTip(wx.ToolTip(toolTips['electricNetTest'])) 
                quote_dialog.m_FinishThickTip.Enable(True)
                quote_dialog.m_FinishThickTip.SetToolTip(wx.ToolTip(toolTips['outLayCop']))
                quote_dialog.m_FinishTypeTip.Enable(True)
                quote_dialog.m_FinishTypeTip.SetToolTip( wx.ToolTip(toolTips['surFinType']))
                quote_dialog.m_HolesCountTip.Enable(True)
                quote_dialog.m_HolesCountTip.SetToolTip(wx.ToolTip(toolTips['count']))
                quote_dialog.m_HolesDensityTip.SetToolTip(wx.ToolTip(toolTips['density']))
                quote_dialog.m_HolesMinRingTip.SetToolTip(wx.ToolTip(toolTips['minAngRing']))
                quote_dialog.m_MaskColorTip.SetToolTip(wx.ToolTip(toolTips['soldMaskClr']))
                quote_dialog.m_MaskFinishTip.SetToolTip(wx.ToolTip(toolTips['soldMaskFin']))
                quote_dialog.m_MaskSidesTip.SetToolTip(wx.ToolTip(toolTips['soldMaskSides']))
                quote_dialog.m_minInnerTraceSpaceTip.SetToolTip(wx.ToolTip(toolTips['minTrcSpcInr']))
                quote_dialog.m_minInnerTraceWidthTip.SetToolTip(wx.ToolTip(toolTips['minTrcSpcOut']))
                quote_dialog.m_minOuterTraceSpaceTip.SetToolTip(wx.ToolTip(toolTips['minTrcWidthInr']))
                quote_dialog.m_minOuterTraceWidthTip.SetToolTip(wx.ToolTip(toolTips['minTrcWidthOut']))
                quote_dialog.m_platingTip.SetToolTip(wx.ToolTip(toolTips['plating']))
                quote_dialog.m_RoHSTip.SetToolTip(wx.ToolTip(toolTips['rohsMarking']))
                quote_dialog.m_SilkColorTip.SetToolTip(wx.ToolTip(toolTips['silkClr']))
                quote_dialog.m_materialTip.SetToolTip(wx.ToolTip(toolTips['silkMaterial']))
                quote_dialog.m_SilkSideTip.SetToolTip(wx.ToolTip(toolTips['silkSides']))
                quote_dialog.m_MaskTypeTip.SetToolTip(wx.ToolTip(toolTips['soldMaskTyp']))
                quote_dialog.m_VendorTip.SetToolTip(wx.ToolTip(toolTips['vendorMarking']))
                quote_dialog.m_HolesMinSizeTip.SetToolTip(wx.ToolTip(toolTips['minSize']))
                quote_dialog.m_qtyTip.SetToolTip(wx.ToolTip(toolTips['quantity']))
                quote_dialog.m_layThicknessTip.SetToolTip(wx.ToolTip(toolTips['thickness']))
                quote_dialog.m_ordHisTip.SetToolTip(wx.ToolTip(toolTips['orderHistory']))

        except Exception as e:
            pass
       
        design_settings = board.GetDesignSettings()
        layers = design_settings.GetCopperLayerCount()
        if layers == 2:
            quote_dialog.m_layerCount.SetSelection(0)
            quote_dialog.m_sufaceFinishThickness1.Disable()
        elif layers == 4:
            quote_dialog.m_layerCount.SetSelection(1)
            quote_dialog.m_sufaceFinishThickness1.SetItems([ "1oz", "2 oz"])
            # quote_dialog.m_layerCount.SetColumns(2)
            quote_dialog.m_sufaceFinishThickness1.SetSelection( 0 )
        elif layers == 6:
            quote_dialog.m_layerCount.SetSelection(2)
            quote_dialog.m_sufaceFinishThickness1.SetItems([ "1oz", "2 oz"])
            quote_dialog.m_sufaceFinishThickness1.SetSelection( 0 )
##Added  comment for netlisttesting less than 8 layer as design document
            # quote_dialog.m_NetlistTesting.SetValue(True)
            # quote_dialog.m_NetlistTesting.Disable()
        elif layers == 8:
            quote_dialog.m_layerCount.SetSelection(3)
            quote_dialog.m_NetlistTesting.SetValue(True)
            quote_dialog.m_NetlistTesting.Disable()
            quote_dialog.m_sufaceFinishThickness1.SetItems([ "1oz", "2 oz"])
            quote_dialog.m_sufaceFinishThickness1.SetSelection( 1 )
        elif layers == 10:
            quote_dialog.m_layerCount.SetSelection(4)
            quote_dialog.m_NetlistTesting.SetValue(True)
            quote_dialog.m_NetlistTesting.Disable()
            quote_dialog.m_sufaceFinishThickness1.SetItems([ "1oz", "2 oz"])
            quote_dialog.m_sufaceFinishThickness1.SetSelection( 1 )
        elif layers == 12:
            quote_dialog.m_layerCount.SetSelection(5)
            quote_dialog.m_NetlistTesting.SetValue(True)
            quote_dialog.m_NetlistTesting.Disable()
            quote_dialog.m_sufaceFinishThickness1.SetItems([ "1oz", "2 oz"])
            quote_dialog.m_sufaceFinishThickness1.SetSelection( 1 )
        else:
            ##Added

            del wait_quote_dialog
            ##
            msg = 'Invalid layer count %d.  We currently only handle 2, 4, 6, 8, 10 or 12 layers.' % layers
            dlg = wx.MessageDialog(_pcbnew_frame, msg, caption, wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            quote_dialog.Destroy()
            logging.shutdown()
            return
        quote_dialog.m_layerCount.Disable()
        # logger.info("Arun" + config_file)
        outer_trace = self.GetMinOuterTraceWidth(board)
        inner_trace = self.GetMinInnerTraceWidth(board)
        min_inner_traces, min_inner_trace_space, min_outer_traces, min_outer_trace_space = self.GetMinSpace(board)
        drill, ring, drill_size, ring_size, total_drills = self.GetDrills(board)
        quote_dialog.SetRing(ring, ring_size)
        quote_dialog.SetDrill(drill, drill_size)
        if inner_trace is not None:
            quote_dialog.inner_min_trace_width = inner_trace[0].GetWidth()
            quote_dialog.inner_min_trace_space = min_inner_trace_space

        quote_dialog.outer_min_trace_width = outer_trace[0].GetWidth()
        quote_dialog.outer_min_trace_space = min_outer_trace_space
        quote_dialog.UpdateTraceUnits()

        quote_dialog.m_holeCount.SetValue(str(total_drills))
        quote_dialog.hole_density = total_drills / outlines.COutline(0).Area()

        density = total_drills / ( outlines.COutline(0).Area() / (6.452e+14) ) # Scale to in^-2
        quote_dialog.m_holeDensity.SetValue( '{0:.2f}'.format( density ) + " drills / in^2")
        # kicad 6.0 changes
        # if outlines.OutlineCount > 1:
        if outlines.OutlineCount() > 1:
            quote_dialog.m_cutoutCount.SetValue( str(outlines.OutlineCount() - 1) )
            quote_dialog.m_plating.Enable()
        else:
            quote_dialog.m_cutoutCount.SetValue("0")
            quote_dialog.m_plating.Disable()

        quote_dialog.SetDimensionsIn(*self.GetBoardDims(outlines))

        success_data = False
        name, ext = os.path.splitext(os.path.basename(board.GetFileName()))
        del wait_quote_dialog
        while not success_data:
            if quote_dialog.ShowModal() != wx.ID_OK:
                quote_dialog.Destroy()
                logging.shutdown()
                return

            try:
                json_data = quote_dialog.GenerateJSON(name)
            except ValueError as e:
                pass
                #del wait_main
                # caption = 'Sierra Circuits Quote'
                # msg = str(e)
                # dlg = wx.MessageDialog(_pcbnew_frame, msg, caption, wx.OK | wx.ICON_ERROR)
                # dlg.ShowModal()
                # dlg.Destroy()
            else:
                success_data = True

        needs_etest = quote_dialog.m_NetlistTesting.GetValue()
        #Added by Renjith for Order Redirect
        file_name = quote_dialog.filename
        qty = []
        
        quote_dialog.Destroy()

##Added
        wait_matrix = wx.BusyInfo("Please wait, Opening Price Matrix")
##
        retval = api.GetMatrix(json_data)
        if retval is None:
            msg = 'Problem getting quote: ' + str(api.last_error_message)
            dlg = wx.MessageDialog(_pcbnew_frame, msg, caption, wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            logging.shutdown()
            return
        #for showing the response
        try:
            if 'partErrorDiscriptionList' in retval and retval['partErrorDiscriptionList']:
                del wait_matrix
                msg = retval['partErrorDiscriptionList'][0]['errorDescription']
                msg = 'Problem getting quote: ' + msg
            dlg2 = wx.MessageDialog(_pcbnew_frame, msg, caption, wx.OK | wx.ICON_ERROR)
            dlg2.ShowModal()
            dlg2.Destroy()
            return
        except Exception as e:
            print(('Error in partErrorDiscriptionList alert', str(e)))



        matrix_dialog = MatrixDialog(_pcbnew_frame)
        matrix_dialog.use_etest = needs_etest
        matrix_dialog.setReturnMatrix(retval)
##Added
        del wait_matrix
##
        if matrix_dialog.ShowModal() != wx.ID_OK:
            matrix_dialog.Destroy()
            logging.shutdown()
            return
        # gen = GenerateProduction(board)
        # gen.archive_project()
        try:
            wait_redirect = wx.BusyInfo("Please wait, we are redirecting to Sierra Circuits order Page")
            layer = str(board.GetCopperLayerCount())
            fname = board.GetFileName().split("/")[-1]
            fname = fname.split("\\")[-1]

            data = {}
            data['userId'] = cred['user_id']
            data['accessToken'] = cred['access_token']
            data['refreshToken'] = cred['refresh_token']
            data['matrix_dialog'] = matrix_dialog.getWebData()
            data['fileName'] = fname
            data['layer'] = layer
            data['etest'] = str(needs_etest)
            data['s3File'] = globalVars.s3_file
            data['topImage'] = globalVars.topImage
            data['botImage'] = globalVars.botImage
            data['entireJson'] = retval
            data['standardJson'] = json.loads( json_data)
            data['BOMValSqsQueues'] =  globalVars.BOMValSqsQueues
            data['bomId'] =  globalVars.bomId
            data['projectId'] =  globalVars.projectId
            data['version'] =  globalVars.version
            data = json.dumps(data)
            req = urllib.request.Request(globalVars.kicadBackendURL + "/store",data= bytes(data, 'utf-8'), headers={'Content-Type' : 'application/json'})
            response = urllib.request.urlopen(req)
            response = json.loads(response.read())
            query_args = { 'uuid': response['uuid']}
            encoded_args = urllib.parse.urlencode(query_args)
            redurl = globalVars.kicadFrontendURL + "/assembly-quote?"+encoded_args
            response = urllib.request.urlopen(req)

            webbrowser.open_new(redurl)
            
            del wait_redirect
        except Exception as e:
            del wait_redirect
            pass
        matrix_dialog.Destroy()
        logging.shutdown()
        pass


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    Based on GPL code by Ferry Boender https://electricmonk.nl/log
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        try:
            for line in buf.rstrip().splitlines():
                self.logger.log(self.log_level, line.rstrip())
        # If we can't write to the log file, ignore
        except:
            pass

    def flush(self, *args, **kwargs):
        """No-op for wrapper"""
        pass

