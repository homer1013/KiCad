#  sierra_quote_dialog.py
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

import os
import sys
import json
import webbrowser
from . import  globalVars
import wx

from . import sierra_order_GUI
from .sierra_order_GUI import quoteDialog, validateDialog
# from .sierra_API import sierra_api
from .getval import getValidate,getorder,redirectCustPortal


tip_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "help-tip.png")

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

##Added
class ValidateDialog(sierra_order_GUI.validateDialog):
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(ValidateDialog, self).SetSizeHints(sz1, sz2)
    def __init__(self, parent,msg,vlable,wmsg,clr,note):
        sierra_order_GUI.validateDialog.__init__(self, parent)
        self.m_staticText3.SetLabelText(vlable)
        self.m_staticText4.SetLabelText(msg)
        self.m_staticText5.SetLabelText(wmsg)
        self.m_staticText6.SetLabelText(note)
        # if clr == 'RED':
        #     self.m_staticText3.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        #     self.m_staticText6.SetLabelText("Please fix the errors/mismatch in specification and revalidate")

    # def onOk(self, event):
    #     self.validateDialog.Destroy()

##Added
class OrderHistoryDialog(sierra_order_GUI.orderHistoryDialog):
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(OrderHistoryDialog, self).SetSizeHints(sz1, sz2)

    def __init__(self, parent, odrdetail):
        sierra_order_GUI.orderHistoryDialog.__init__(self, parent)
        self.m_listCtrl1.InsertColumn(0, 'Order Number', width = 150)
        self.m_listCtrl1.InsertColumn(1, 'Order Date', wx.LIST_FORMAT_RIGHT, 150)
        self.m_listCtrl1.InsertColumn(2, 'Order Amount', wx.LIST_FORMAT_RIGHT, 150)
        self.m_listCtrl1.InsertColumn(3, 'Order Status', wx.LIST_FORMAT_RIGHT, 150)

        res = [(x["orderNumber"], x["orderDate"], x["orderAmount"], x["orderStatus"]) for x in odrdetail["orderItems"]]
        
        for i in res:
            index = self.m_listCtrl1.InsertItem(0, i[0])
            # index = self.m_listCtrl1.InsertItem(sys.maxsize, i[0])
            self.m_listCtrl1.SetItem(index, 1, i[1])
            self.m_listCtrl1.SetItem(index, 2, '$'+i[2])
            # self.m_listCtrl1.SetStringItem(index, 3, i[3])
            self.m_listCtrl1.SetItem(index, 3, i[3])
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.m_listCtrl1)
    def OnClick(self, event):
        wait_order = wx.BusyInfo("Please wait, working...",self)
        webbrowser.open(redirectCustPortal())
        del wait_order
        
class QuoteDialog (sierra_order_GUI.quoteDialog):

    board_length = 0
    board_width = 0
    outer_min_trace_width = 0
    outer_min_trace_space = 0
    inner_min_trace_width = 0
    inner_min_trace_space = 0
    hole_count = 0
    hole_density = 0
    minimum_drill = 0
    minimum_ring = 0
    slot_count = 0
    setusername = ""
    setpassword = ""

    min_drill = None
    min_ring = None
    min_drill_size = 0
    min_ring_size = 0

    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(QuoteDialog, self).SetSizeHints(sz1, sz2)

#Added v_board
    def __init__(self, parent, logo_path,v_board):
        sierra_order_GUI.quoteDialog.__init__(self, parent)
        self.m_electricalTip.SetBitmap(wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_electricalTip.SetToolTip(wx.ToolTip( "We provide 100% Electrical Netlist Testing of PCBs for an extra charge. You can decline testing for PCBs up to 6 layers. If your PCB has more than 6 layers, Electrical Testing is mandatory"))

        self.m_FinishThickTip.SetBitmap(wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_FinishThickTip.SetToolTip(wx.ToolTip( "The total thickness of the board including all plating and final finishes"))

        self.m_FinishTypeTip.SetBitmap(wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_FinishTypeTip.SetToolTip( wx.ToolTip( "Immersion Gold: 3-10 microinches of gold over electroless nickel (ENIG). This is also a lead-free finish" ) )

        self.m_HolesCountTip.SetBitmap(wx.Bitmap(tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_HolesCountTip.SetToolTip(wx.ToolTip("Total number of holes per board"))

        self.m_HolesDensityTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_HolesDensityTip.SetToolTip(wx.ToolTip("This is important because a board with too much hole density is complex and takes a lot of resources on the drilling machine. If your board has more than 80 holes/square inch on the average, you may not get an automatic quote on Web PCBS promotion, and a sales person may need to get involved."))

        self.m_HolesMinRingTip.SetBitmap(wx.Bitmap(tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_HolesMinRingTip.SetToolTip(wx.ToolTip("Smallest Annular Ring ( Pad Size - Hole Size / 2 )"))

        self.m_HolesMinSizeTip.SetBitmap(wx.Bitmap(tip_path, wx.BITMAP_TYPE_PNG))
        # self.m_HolesMinSizeTip.SetToolTip(wx.ToolTip("smallest finished hole size in inches"))

        self.m_MaskColorTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_MaskColorTip.SetToolTip(wx.ToolTip("Color of the mask used to cover the PCB"))
        self.m_MaskFinishTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_MaskFinishTip.SetToolTip(wx.ToolTip("Typically, soldermask has a Semi-gloss finish"))
        self.m_MaskSidesTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_MaskSidesTip.SetToolTip(wx.ToolTip("How many sides to mask."))
        self.m_minInnerTraceSpaceTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_minInnerTraceSpaceTip.SetToolTip(wx.ToolTip("Quotes are offered based on minimum XXX of 0.004 inches, 0.005 inches and 0.006 inches"))
        self.m_minInnerTraceWidthTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_minInnerTraceWidthTip.SetToolTip(wx.ToolTip("Quotes are offered based on minimum XXX of 0.004 inches, 0.005 inches and 0.006 inches"))
        self.m_minOuterTraceSpaceTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_minOuterTraceSpaceTip.SetToolTip(wx.ToolTip("Quotes are offered based on minimum XXX of 0.004 inches, 0.005 inches and 0.006 inches"))
        self.m_minOuterTraceWidthTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_minOuterTraceWidthTip.SetToolTip(wx.ToolTip("Quotes are offered based on minimum XXX of 0.004 inches, 0.005 inches and 0.006 inches"))
        self.m_platingTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_platingTip.SetToolTip(wx.ToolTip("Elongated holes used for component placement. These can be plated with copper or non-plated."))
        self.m_RoHSTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_RoHSTip.SetToolTip(wx.ToolTip("Do not put any RoHS marking, even if applicable."))
        self.m_SilkColorTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_SilkColorTip.SetToolTip(wx.ToolTip("Color of ink printed on the board. Typically, it is White."))
        self.m_materialTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_materialTip.SetToolTip(wx.ToolTip("Different types of laminate available for PCB fabrication"))
        self.m_SilkSideTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_SilkSideTip.SetToolTip(wx.ToolTip("Specify whether your design has Legend on Top or Bottom or Both sides?"))
        self.m_MaskTypeTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_MaskTypeTip.SetToolTip(wx.ToolTip("we only offer LPI (Liquid Photo-Imageable) solder mask which is sufficient for most PCBs."))
        self.m_VendorTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_VendorTip.SetToolTip(wx.ToolTip("Vendor markings include Company Logo, UL marking, Flammability, etc. Such vendor markings will be put in Silkscreen/Legend."))
        self.m_qtyTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_qtyTip.SetToolTip(wx.ToolTip("Vendor markings include Company Logo, UL marking, Flammability, etc. Such vendor markings will be put in Silkscreen/Legend."))
        self.m_layThicknessTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_layThicknessTip.SetToolTip(wx.ToolTip("Vendor markings include Company Logo, UL marking, Flammability, etc. Such vendor markings will be put in Silkscreen/Legend."))
        self.m_ordHisTip.SetBitmap( wx.Bitmap( tip_path, wx.BITMAP_TYPE_PNG ) )
        # self.m_ordHisTip.SetToolTip(wx.ToolTip("Vendor markings include Company Logo, UL marking, Flammability, etc. Such vendor markings will be put in Silkscreen/Legend."))

        self.m_okCancelOK.SetLabelText("Get Quote")
        self.m_okCancelOK.Disable()

        try:
            self.m_bpButton1.SetBitmap(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG))
        except:
            self.m_bpButton1.SetBitmap(wx.BitmapBundle(wx.Bitmap(logo_path, wx.BITMAP_TYPE_PNG)))

        self.Fit()
        width, discard = self.GetTextExtent('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        discard, height = self.GetSize()
        self.SetMaxSize((width, height))
        self.SetMinSize((width, height))
        self.SetSize((width, height))

        self.SetSize((width,-1))
##Added
        self.v_board = v_board
        self.vflag = False
        self.filename = ''
        self.productSpecErrors = []
        self.productSpecWarn = []

    def onUpdateUI(self, event):
        try:
            self.CheckBoardSize(self.board_width)
        except ValueError as e:
            dlg11 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg11.ShowModal()
            dlg11.Destroy()
            self.m_width.SetForegroundColour((255, 0, 0))
            self.m_width.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckBoardSize(self.board_length)
        except ValueError as e:
            dlg10 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg10.ShowModal()
            dlg10.Destroy()
            self.m_length.SetForegroundColour((255, 0, 0))
            self.m_length.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckHoleDensity(self.hole_density)
        except ValueError as e:
            self.m_staticText72.SetForegroundColour((255,0,0))
            # self.m_holeDensity.SetForegroundColour((255, 0, 0))
            self.m_okCancelOK.SetToolTipString(str(e))
            # self.m_okCancelOK.Bind(wx.EVT_BUTTON,self.onException)
            dlg33 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg33.ShowModal()
            dlg33.Destroy()
            self.m_okCancelOK.Disable()

        try:
            self.CheckMaxSlotCount(self.slot_count)
        except ValueError as e:
            dlg8 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg8.ShowModal()
            dlg8.Destroy()
            self.m_cutoutCount.SetForegroundColour((255, 0, 0))
            # self.m_cutoutCount.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckMaxHoleCount(self.hole_count)
        except ValueError as e:
            dlg7 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg7.ShowModal()
            dlg7.Destroy()
            self.m_holeCount.SetForegroundColour((255, 0, 0))
            # self.m_holeCount.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckMinHoleSize(self.min_drill_size)
        except ValueError as e:
            dlg6 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg6.ShowModal()
            dlg6.Destroy()
            self.m_minHoleSize.SetForegroundColour((255, 0, 0))
            # self.m_minHoleSize.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckMinRingSize(self.min_ring_size)
        except ValueError as e:
            dlg5 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg5.ShowModal()
            dlg5.Destroy()
            self.m_minAnnularRing.SetForegroundColour((255, 0, 0))
            # self.m_minAnnularRing.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckMinTrackSpace(self.outer_min_trace_space)

        except ValueError as e:
            dlg4 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg4.ShowModal()
            dlg4.Destroy()
            self.m_outerMinSpace.SetForegroundColour((255, 0, 0))
            # self.m_outerMinSpace.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        try:
            self.CheckMinTrackWidth(self.outer_min_trace_width)
        except ValueError as e:
            dlg1 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
            dlg1.ShowModal()
            dlg1.Destroy()
            self.m_outerMinTrace.SetForegroundColour((255, 0, 0))
            # self.m_outerMinTrace.SetToolTip(wx.ToolTip(str(e)))
            self.m_okCancelOK.SetToolTipString(str(e))
            self.m_okCancelOK.Disable()

        if self.m_layerCount.GetSelection() > 0:
            try:
                self.CheckMinTrackSpace(self.inner_min_trace_space)
            except ValueError as e:
                dlg2 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
                dlg2.ShowModal()
                dlg2.Destroy()
                self.m_innerMinSpace.SetForegroundColour((255, 0, 0))
                # self.m_innerMinSpace.SetToolTip(wx.ToolTip(str(e)))
                self.m_okCancelOK.SetToolTipString(str(e))
                self.m_okCancelOK.Disable()

            try:
                self.CheckMinTrackWidth(self.inner_min_trace_width)
            except ValueError as e:
                dlg3 = wx.MessageDialog(_pcbnew_frame, str(e), caption, wx.OK | wx.ICON_ERROR)
                dlg3.ShowModal()
                dlg3.Destroy()
                self.m_innerMinTrace.SetForegroundColour((255, 0, 0))
                # self.m_innerMinTrace.SetToolTip(wx.ToolTip(str(e)))
                self.m_okCancelOK.SetToolTipString(str(e))
                self.m_okCancelOK.Disable()


    def onSelectUnits(self, event):
        self.SetDimensionsIn( self.board_length, self.board_width )
        event.Skip()

    def onChangeTraceUnits(self, event):
        self.UpdateTraceUnits()
        event.Skip()

    def UpdateTraceUnits(self):

        if( self.m_layerCount.GetSelection != 0 ):
            self.SetTrackWidthIn(self.m_innerMinTrace, self.inner_min_trace_width)
            self.SetTrackWidthIn(self.m_innerMinSpace, self.inner_min_trace_space)
        else:
            self.m_innerMinSpace.SetValue("")
            self.m_innerMinTrace.SetValue("")

        self.SetTrackWidthIn(self.m_outerMinTrace, self.outer_min_trace_width)
        self.SetTrackWidthIn(self.m_outerMinSpace, self.outer_min_trace_space)

    def SetDimensionsIn(self, x, y):
        self.board_length = x
        self.board_width = y
        self.m_width.SetValue( str('{0:.2f}'.format( Unit.ToInches( x ) )) +" inches" )
        self.m_length.SetValue( str('{0:.2f}'.format( Unit.ToInches( y ) )) + " inches" )
        
    def SetDimensions(self, x, y):
        self.board_length = x
        self.board_width = y
        self.m_width.SetValue( '{0:.2f}'.format( Unit.ToInches( x ) ) )
        self.m_length.SetValue( '{0:.2f}'.format( Unit.ToInches( y ) ) )
        
    # def SetTrackWidth( self, textfield, units, value ):
    #     if( units.GetSelection() == Unit.MM ):
    #         textfield.SetValue( '{0:.1f}'.format( Unit.ToMM( value ) ) )
    #     else:
    #         textfield.SetValue( '{0:.3f}'.format( Unit.ToMil( value ) ) )
    
    def SetTrackWidthIn( self, textfield, value ):
        checkValue = Unit.ToInches(value)
        if checkValue >  1000 :
            textfield.SetValue( str('{0:.3f}'.format( 0.006 )) + " inches" )
        else:
            textfield.SetValue( str('{0:.3f}'.format( Unit.ToInches( value ))) + " inches")
    
    def SetTrackWidth( self, textfield, units, value ):
        if( units.GetSelection() == Unit.MM ):
            checkValue = Unit.ToMM( value )
            if checkValue >  1000 :
                textfield.SetValue( '{0:.3f}'.format( 0.1524 ) )
            else:
                textfield.SetValue( '{0:.1f}'.format( Unit.ToMM( value ) ) )
            # textfield.SetValue( '{0:.1f}'.format( Unit.ToMM( value ) ) )
        else:
            checkValue = Unit.ToMil( value )
            if checkValue >  1000 :
                textfield.SetValue( '{0:.3f}'.format( 6 ) )
            else:
                textfield.SetValue( '{0:.3f}'.format( Unit.ToMil( value ) ) )
            # textfield.SetValue( '{0:.3f}'.format( Unit.ToMil( value ) ) )

    def SetDrill(self, drill, drill_size):
        self.min_drill = drill
        self.min_drill_size = drill_size
        self.m_minHoleSize.SetValue('{0:.2f}'.format(Unit.ToMM(drill_size)))

    def SetRing(self, ring, ring_size):
        self.min_ring = ring
        self.min_ring_size = ring_size
        self.m_minAnnularRing.SetValue('{0:.2f}'.format(Unit.ToMM(ring_size)))

    def CheckBoardSize(self, size):
        inch_size = Unit.ToInches(size)

        if inch_size > 15.9:
            #return inch_size
            self.productSpecErrors.append('Board dimension %s too large (max 15.9 in)' % '{0:.2f}'.format(inch_size))
            # raise ValueError('Board dimension %s too large (max 15.9 in)' % '{0:.2f}'.format(inch_size))
        elif inch_size < 0.5:
            #return inch_size
            self.productSpecErrors.append('Board dimension %s too small (min 0.5 in)' % '{0:.2f}'.format(inch_size))
            # raise ValueError('Board dimension %s too small (min 0.5 in)' % '{0:.2f}'.format(inch_size))

        return inch_size

    def CheckMinRingSize(self, size):
        inch_size = Unit.ToInches(size)

        if inch_size >= 0.007:
            return 0.007
        elif inch_size >= 0.006:
            return 0.006
        elif inch_size >= 0.005:
            return 0.005
        elif inch_size >= 0.004:
            return 0.004
        else:
            # return inch_size
            self.productSpecErrors.append('Annular ring too small (min 4 mil)')
            # raise ValueError('Annular ring too small (min 4 mil)')

    def CheckMinTrackWidth(self, size):
        inch_size = Unit.ToInches(size)

        if inch_size >= 0.006:
            return 0.006
        elif inch_size >= 0.005:
            return 0.005
        elif inch_size >= 0.004:
            return 0.004
        else:
            # return inch_size
            self.productSpecErrors.append('Trace width too small (min 4 mil)')
            # raise ValueError('Trace width too small (min 4 mil)')


    def CheckMinTrackSpace(self, size):
        inch_size = Unit.ToInches(size)

        if inch_size >= 0.006:
            return 0.006
        elif inch_size >= 0.005:
            return 0.005
        elif inch_size >= 0.004:
            return 0.004
        else:
            self.productSpecErrors.append('Track spacing too small (min 4 mil)')
            # raise ValueError('Track spacing too small (min 4 mil)')

    def CheckMaxHoleCount(self, number):

        if number <= 400:
            return number
        else:
            self.productSpecErrors.append('Too many holes (max 400)')
            # raise ValueError('Too many holes (max 400)')

    def CheckMaxSlotCount(self, number):

        if number <= 10:
            return number

        self.productSpecWarn.append('Too many slots (max 10)')
        # raise ValueError('Too many slots (max 10)')

    def CheckMinHoleSize(self, size):
        inch_size = Unit.ToInches(size)

        if inch_size >= 0.01:
            return 0.01
        elif inch_size >= 0.008:
            return 0.008

        self.productSpecErrors.append('Hole size too small (min 8 mil)')
        # raise ValueError('Hole size too small (min 8 mil)')

    def CheckHoleDensity(self, density):

        inch_size = Unit.FromInches(Unit.FromInches(density)) #Convert from nm^-2 to in^-2

        if inch_size <= 80.0:
            return inch_size

        # self.productSpecWarn.append('Too many holes per sq inch (max 80 in^-2)')
        # raise ValueError('Too many holes per sq inch (max 80 in^-2)')


    def GenerateJSON(self, board_name):
        if self.m_layerCount.GetSelection() > 0:
            inner_min_space = self.inner_min_trace_space
            inner_min_trace = self.inner_min_trace_width
            inner_min_trace = self.CheckMinTrackWidth(inner_min_trace)
            inner_min_space = self.CheckMinTrackSpace(inner_min_space)
            outer_min_space = self.outer_min_trace_space
            outer_min_trace = self.outer_min_trace_width
            outer_min_trace = self.CheckMinTrackWidth(outer_min_trace)
            outer_min_space = self.CheckMinTrackSpace(outer_min_space)
            inner_min_trace = '{0:.3f}'.format(inner_min_trace) + " inches"
            inner_min_space = '{0:.3f}'.format(inner_min_space) + " inches"

        else:
            outer_min_space = self.outer_min_trace_space
            outer_min_trace = self.outer_min_trace_width
            outer_min_space = self.CheckMinTrackSpace(outer_min_space)
            outer_min_trace = self.CheckMinTrackWidth(outer_min_trace)
            inner_min_trace = "Not Applicable"
            inner_min_space = "Not Applicable"


        # min_trace = self.CheckMinTrackWidth(min_trace)
        # min_space = self.CheckMinTrackSpace(min_space)
        min_hole = self.CheckMinHoleSize(self.min_drill_size)
        if min_hole == 0.008:
            min_hole = '{0:.3f}'.format(min_hole) + " inches"
        elif min_hole == 0.01:
            min_hole = '{0:.3f}'.format(min_hole) + " inches or more"
        min_ring = self.CheckMinRingSize(self.min_ring_size)

        layer_string = "2 Layer"

        if self.m_layerCount.GetSelection() == 1:
            layer_string = "4 Layer"
        if self.m_layerCount.GetSelection() == 2:
            layer_string = "6 Layer"
        if self.m_layerCount.GetSelection() == 3:
            layer_string = "8 Layer"
        if self.m_layerCount.GetSelection() == 4:
            layer_string = "10 Layer"

        slots = self.m_plating.GetStringSelection()
        if slots == 'Both':
            slots = 'Both Plated and Non Plated'
        json_input_width = self.m_width.GetValue()
        json_input_width = json_input_width.split(' ')[0]
        json_input_length = self.m_length.GetValue()
        json_input_length = json_input_length.split(' ')[0]

        if self.m_sufaceFinishThickness.GetSelection() == 0:
            surfaceFinishThickness = '1 Oz'
        else:
            surfaceFinishThickness = '2 Oz'

        if self.m_sufaceFinishThickness1.GetSelection() == 0:
            innrsurfaceFinishThickness = '1 Oz'
        elif self.m_sufaceFinishThickness1.GetSelection() == 1:
            innrsurfaceFinishThickness = '2 Oz'
        else:
            innrsurfaceFinishThickness = 'Not Applicable'


        if str(self.m_SilkSides.GetSelection()) == '0':
            silkSides = 'Top'
        elif str(self.m_SilkSides.GetSelection()) == '1':
            silkSides = 'Bottom'
        elif str(self.m_SilkSides.GetSelection()) == '2':
            silkSides = 'Both'
        else:
            silkSides = 'None'

#Added by Arun
        silkColorDict = {'0' : 'White', '1' : 'Yellow', '2' : 'Black'}
        silkColor = silkColorDict[str(self.m_SilkColor.GetSelection())]
##

        if self.m_maskSides.GetSelection() == 0:
            maskSides = 'Top only'
        elif self.m_maskSides.GetSelection() == 1:
            maskSides = 'Bottom only'
        elif self.m_maskSides.GetSelection() == 2:
            maskSides = 'Top and Bottom'
        else:
            maskSides = 'None'
        qty = []
        if self.m_quant1.GetValue() != '':
            qty.append(self.m_quant1.GetValue())
        if self.m_quant2.GetValue() != '':
            qty.append(self.m_quant2.GetValue())
        if self.m_quant3.GetValue() != '':
            qty.append(self.m_quant3.GetValue())
        if self.m_quant4.GetValue() != '':
            qty.append(self.m_quant4.GetValue())
        qty = list(set(qty))

        
        if len(qty) == 4:
            boardQty1 = qty[0]
            boardQty2 = qty[1]
            boardQty3 = qty[2]
            boardQty4 = qty[3]
        elif len(qty) == 3:
            boardQty1 = qty[0]
            boardQty2 = qty[1]
            boardQty3 = qty[2]
            boardQty4 = "2"
        elif len(qty) == 2:
            boardQty1 = qty[0]
            boardQty2 = qty[1]
            boardQty3 = "4"
            boardQty4 = "2"
        elif len(qty) == 1:
            boardQty1 = qty[0]
            boardQty2 = "6"
            boardQty3 = "4"
            boardQty4 = "2"
        else:
            boardQty1 = "8"
            boardQty2 = "6"
            boardQty3 = "4"
            boardQty4 = "2"
##Added by Arun
        maskColor = self.m_maskColor.GetStringSelection()
        surfaceFinish = self.m_sufaceFinish.GetStringSelection()
##
        boardThickness = self.m_thickness.GetStringSelection()
        if str(self.m_vendorMark.GetValue()) == 'True':
            vendormark = 'Yes'
        else:
            vendormark = 'No'
##Added by Arun
        materialDict = {'0' : "FR4", '1' : "FR4-Lead Free", '2' : "Polyimide", '3' : "Nan Ya NP-175", '4' : "FR4-06"}
        material = self.m_material.GetStringSelection()
##

        if str(self.m_NetlistTesting.GetValue()) == 'True':
            nettesting = 'Yes'
        else:
            nettesting = 'No'
        ret = json.dumps(
            {
                "indBoardXDim": json_input_width,
                "indBoardYDim": json_input_length,
                "layers": layer_string,
                "minHoleSize": min_hole,
                "minimumSpace": '{0:.3f}'.format(outer_min_space) + " inches",
                "minimumTrace": '{0:.3f}'.format(outer_min_trace) + " inches",
                "minAnnularRing": '{0:.3f}'.format(min_ring) + " inches",
                "noOfHolesPerBoard": self.m_holeCount.GetValue(),
                "partNumber": board_name,
                "partRevision": "1",
                "slotsCutouts": slots,
                "productId": "2",
                "scTemplateId": "KICAD_STD",
                "outerLyrFinishCopper": surfaceFinishThickness,
                "silkScreenSides": silkSides,
                "silkScreenColor": silkColor,
                "solderMaskSides": maskSides,
                "solderMaskColor": maskColor,
                "surfaceFinish": surfaceFinish,
                "finishedThickness": boardThickness,
                "vendorMarking": vendormark,
                "material": material,
                "electricalTesting": nettesting,
                "controlledImpedance": "None",
                "innerLyrFinishCopper": innrsurfaceFinishThickness,
                "minimumTraceInnerLyr": inner_min_trace,
                "minimumSpaceInnerLyr": inner_min_space,
                "boardQty1" : boardQty1,
                "boardQty2" : boardQty2,
                "boardQty3" : boardQty3,
                "boardQty4" : boardQty4
            }
        )
        return ret

    def SetFilename(self,filename):
        self.filename = filename

    def onException(self,event):
        pass


##Added
    def onAction_m_quant1(self, event):
        """
        Event to ensure the input text is numeric and is within maximum quantity limit
        """
        m_quant1 = self.m_quant1.GetValue().strip()
        if m_quant1.isnumeric():
            try:
                if int(m_quant1) == 0 :
                    dlg112 = wx.MessageDialog(self,"The minimum order quantity should be 1 or above ", 'Order Quantity' , wx.OK | wx.ICON_ERROR)
                    dlg112.ShowModal()
                    dlg112.Destroy() 
                    self.m_quant1.ChangeValue("")
            except Exception as e:
                pass
        else:
            self.m_quant1.ChangeValue("")

    def onAction_m_quant2(self, event):
        """
        Event to ensure the input text is numeric and is within maximum quantity limit
        """
        m_quant2 = self.m_quant2.GetValue().strip()
        if m_quant2.isnumeric():
            try:
                if int(m_quant2) == 0 :
                    dlg112 = wx.MessageDialog(self,"The minimum order quantity should be 1 or above ", 'Order Quantity' , wx.OK | wx.ICON_ERROR)
                    dlg112.ShowModal()
                    dlg112.Destroy() 
                    self.m_quant2.ChangeValue("")
            except Exception as e:
                pass 
        else:
            self.m_quant2.ChangeValue("")

    def onAction_m_quant3(self, event):
        """
        Event to ensure the input text is numeric and is within maximum quantity limit
        """
        m_quant3 = self.m_quant3.GetValue().strip()
        if m_quant3.isnumeric():
            try:
                if int(m_quant3) == 0 :
                    dlg112 = wx.MessageDialog(self,"The minimum order quantity should be 1 or above ", 'Order Quantity' , wx.OK | wx.ICON_ERROR)
                    dlg112.ShowModal()
                    dlg112.Destroy() 
                    self.m_quant3.ChangeValue("")
            except Exception as e:
                pass
        else:
            self.m_quant3.ChangeValue("")

    def onAction_m_quant4(self, event): 
        """
        Event to ensure the input text is numeric and is within maximum quantity limit
        """
        m_quant4 = self.m_quant4.GetValue().strip()
        if m_quant4.isnumeric():
            try:
                if int(m_quant4) == 0 :
                    dlg112 = wx.MessageDialog(self,"The minimum order quantity should be 1 or above ", 'Order Quantity' , wx.OK | wx.ICON_ERROR)
                    dlg112.ShowModal()
                    dlg112.Destroy() 
                    self.m_quant4.ChangeValue("")
            except Exception as e:
                pass
        else:
            self.m_quant4.ChangeValue("")
    def onSetTipElectricNetTest(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['electricNetTest'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipFinishThickTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['outLayCop'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipFinishTypeTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['surFinType'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 

    def onSetTipHolesCountTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['count'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipHolesDensityTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['density'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipHolesMinRingTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minAngRing'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMaskColorTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['soldMaskClr'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMaskFinishTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['soldMaskFin'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMaskSidesTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['soldMaskSides'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMinInnerTraceSpaceTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minTrcSpcInr'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMinInnerTraceWidthTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minTrcSpcOut'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMinOuterTraceSpaceTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minTrcWidthInr'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMinOuterTraceWidthTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minTrcWidthOut'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipPlatingTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['plating'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipRoHSTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['rohsMarking'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipSilkColorTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['silkClr'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMaterialTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['silkMaterial'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 

    def onSetTipSilkSideTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['silkSides'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipMaskTypeTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['soldMaskTyp'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipVendorTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['vendorMarking'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipHolesMinSizeTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['minSize'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipQtyTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['quantity'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipLayThicknessTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['thickness'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onSetTipOrdHisTip(self, event):
        if globalVars.toolTips!= '':
            toolTips = globalVars.toolTips
            dlg112 = wx.MessageDialog(self,toolTips['orderHistory'], 'Tool Tips', wx.OK | wx.ICON_INFORMATION)
            dlg112.ShowModal()
            dlg112.Destroy() 
    def onValidate(self, event):
        wait_validate = wx.BusyInfo("Please wait, working...",self)
        try:
            # self.SetCursor(wx.StockCursor(wx.CURSOR_WAIT))
            getfile = getValidate(self.v_board.GetFileName(),self.setuserid,self.setaccesstoken,self.setsessionid)

            if getfile == False:  
                del wait_validate
                dlg111 = wx.MessageDialog(self,"Service not Available", 'Validate Files', wx.OK | wx.ICON_ERROR)
                dlg111.ShowModal()
                dlg111.Destroy()  

            else:
                #getfile = {"errorMessages":[],"warningMessages":[]}
                self.SetFilename(getfile["filename"])
                globalVars.s3_file = getfile["s3_file"]
                globalVars.topImage = getfile["topImage"]
                globalVars.botImage = getfile["botImage"]
                globalVars.bomId = getfile['bomId']
                globalVars.BOMValSqsQueues = getfile['BOMValSqsQueues']
                globalVars.projectId = getfile['projectId']
                globalVars.version = getfile['version']


                #self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                self.productSpecErrors = list(set(self.productSpecErrors))
                self.productSpecWarn = list(set(self.productSpecWarn))

                getfile["errorMessages"].extend(self.productSpecErrors)
                getfile["warningMessages"].extend(self.productSpecWarn)

                del wait_validate
                if len(getfile["errorMessages"]) > 0 :
                    res = [(i,j) for i,j in enumerate(getfile["errorMessages"],start = 1)]
                    st = ['. '.join(map(str, x)) for x in res]
                    emsg = "\n".join(i for i in st)
                    v_lable = "Error"
                    w_msg = "NOTE: we've found errors with respect to specifications/design files "
                    vclr = 'BLACK'
                    note = 'Please correct above issue(s) and revalidate the design file to generate a quote'
                elif len(getfile["warningMessages"]) > 0 :
                    res = [(i,j) for i,j in enumerate(getfile["warningMessages"],start = 1)]
                    st = ['. '.join(map(str, x)) for x in res]
                    emsg = "\n".join(i for i in st)
                    v_lable = "Warning"
                    w_msg = "NOTE: Warnings(non-critical)"
                    vclr = 'BLACK'
                    note = 'You can now click on Get Quote button'
                    self.m_okCancelOK.Enable()

                else:
                    emsg = "File validation Successfull"
                    v_lable = "Success"
                    w_msg = " . "
                    vclr = 'BLACK'
                    note = 'You can now click on Get Quote button'
                    self.m_okCancelOK.Enable()
                mval = ValidateDialog(self,emsg,v_lable,w_msg,vclr,note)
                mval.ShowModal()
                mval.Destroy()

        except Exception as e:
                del wait_validate
                dlg111 = wx.MessageDialog(self,str(e) , 'Validate Files', wx.OK | wx.ICON_ERROR)
                dlg111.ShowModal()
                dlg111.Destroy()

        # self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        event.Skip()

    def onOrderHistory(self, event):
        import traceback
        wait_order = wx.BusyInfo("Please wait, working...",self)
        try:
            odr = getorder(self.setuserid)
            del wait_order
            if odr:
                morder = OrderHistoryDialog(self,odr)
                # morder.InsertStringItem(sys.maxint, i[0])

                # dbg.ShowModal()
                morder.ShowModal()
                # morder.Destroy()
                # dbg.Destroy()

            else:
                dlg111 = wx.MessageDialog(self,'No order History' , 'Order History', wx.OK | wx.ICON_ERROR)
                dlg111.ShowModal()
                dlg111.Destroy()
                # dbg = wx.MessageDialog(self,str(odr) , u'Validate Files', wx.OK | wx.ICON_ERROR)



        except Exception as e:
                dlg111 = wx.MessageDialog(self,str("Facing issue to fetch the order history details") , 'Order History', wx.OK | wx.ICON_ERROR)
                dlg111.ShowModal()
                dlg111.Destroy()
        event.Skip()


