#  generate_production_files.py
#
#  Copyright (C) 2019 Sierra Circuits, Inc
#
#  Designed by KiCad Services, Inc.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
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
#  This code is derived from kiplot, (C) 2017-2018 John Beard
#  kiplot is licensed under the GNU General Public License version 3

import sys
import os
import shutil
import pcbnew
import csv
import re
import tempfile

class GenerateProduction:
    m_board = None

    def __init__(self,board):
        self.m_board = board
    
    def generate_gerber(self, output_dir):
        
        pctl = pcbnew.PLOT_CONTROLLER(self.m_board)
        popt = pctl.GetPlotOptions()

        ###########################################################################
        # Output options
        popt.SetFormat(pcbnew.PLOT_FORMAT_GERBER)
        popt.SetOutputDirectory(output_dir)

        ###########################################################################
        # Included Layers:

        layers = [
            {'layer': pcbnew.Edge_Cuts, 'suffix': 'Edge.Cuts'}
        ]

        bds = self.m_board.GetDesignSettings()

        for i in range(pcbnew.F_Cu, pcbnew.B_Cu + 1):
            if bds.IsLayerEnabled(i):
                layer_name = self.m_board.GetLayerName(i)
                layers.append({'layer':i, 'suffix':layer_name})
        
        if bds.IsLayerEnabled(pcbnew.F_SilkS):
            layers.append({'layer': pcbnew.F_SilkS, 'suffix': 'F.SilkS'})
        if bds.IsLayerEnabled(pcbnew.B_SilkS):
            layers.append({'layer': pcbnew.B_SilkS, 'suffix': 'B.SilkS'})
        if bds.IsLayerEnabled(pcbnew.B_Paste):
            layers.append({'layer': pcbnew.B_Paste, 'suffix': 'B.Paste'})
        if bds.IsLayerEnabled(pcbnew.F_Paste):
            layers.append({'layer': pcbnew.F_Paste, 'suffix': 'F.Paste'})
        if bds.IsLayerEnabled(pcbnew.B_Mask):
            layers.append({'layer': pcbnew.B_Mask, 'suffix': 'B.Mask'})
        if bds.IsLayerEnabled(pcbnew.F_Mask):
            layers.append({'layer': pcbnew.F_Mask, 'suffix': 'F.Mask'})

        ###########################################################################
        # General Options:
        popt.SetPlotFrameRef(False)
        popt.SetPlotValue(True)
        popt.SetPlotReference(True)
        popt.SetExcludeEdgeLayer(True)
        popt.SetPlotPadsOnSilkLayer(False)
        popt.SetUseAuxOrigin(False)
        popt.SetDrillMarksType(popt.NO_DRILL_SHAPE)
        popt.SetAutoScale(False)
        popt.SetScale(1)
        popt.SetPlotMode(pcbnew.FILLED)
        popt.SetLineWidth(pcbnew.FromMM(0.1))

        ###########################################################################
        # Gerber Options:
        popt.SetUseGerberProtelExtensions(True)
        popt.SetCreateGerberJobFile(False)
        popt.SetSubtractMaskFromSilk(False)

        ###########################################################################
        # Generate files now

        for l in layers:
            pctl.SetLayer(l['layer'])
            pctl.OpenPlotfile(l['suffix'], pcbnew.PLOT_FORMAT_GERBER, l['layer'])
            pctl.PlotLayer()

        pctl.ClosePlot()


    def generate_drillmap(self, output_dir):
        writer = pcbnew.EXCELLON_WRITER(self.m_board)

        writer.SetFormat(True)
        writer.SetOptions(
            aMirror=False,
            aMinimalHeader=False,
            aOffset=writer.GetOffset(),
            aMerge_PTH_NPTH=True
        )
        writer.CreateDrillandMapFilesSet(
            output_dir,
            aGenDrill=True,
            aGenMap=False,
            aReporter=None
        )

    def generate_position_csv(self, output_dir):
        

        with open(os.path.join(output_dir, board_name + '-top-pos.csv'), 'w', newline='') as out_top,\
            open(os.path.join(output_dir, board_name + '-bottom-pos.csv'), 'w', newline='') as out_bot:
                fieldnames = ['Ref','Val','Package','PosX','PosY','Rot','Side']
                csv_top = csv.DictWriter(out_top, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
                csv_bot = csv.DictWriter(out_bot, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
                csv_top.writeheader()
                csv_bot.writeheader()

                def sorted_nicely(l):
                    convert = lambda text: int(text) if text.isdigit() else text
                    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key.GetReference())]
                    return sorted(l, key = alphanum_key)

                sorted_modules = sorted_nicely(self.m_board.GetModules())

                aux_origin = self.m_board.GetAuxOrigin()

                for m in sorted_modules:
                    is_cms = (m.GetAttributes() == pcbnew.MOD_CMS)
                    is_top = not m.IsFlipped()
                    is_bot = not is_top

                    if not is_cms:
                        continue

                    side =  'top'     if is_top \
                    else    'bottom'  if is_bot \
                    else    'none'

                    values = {
                        'Ref': m.GetReference(),
                        'Val': m.GetValue(),
                        'Package': m.GetFPID().GetLibItemName(),
                        'PosX': pcbnew.ToMM(m.GetPosition().x - aux_origin.x),
                        'PosY': pcbnew.ToMM(aux_origin.y - m.GetPosition().y),
                        'Rot': m.GetOrientationDegrees(),
                        'Side': side,
                    }

                    if side == 'top':
                        csv_top.writerow(values)
                    if side == 'bottom':
                        csv_bot.writerow(values)


    def archive_project(self):
        gerber_dir = tempfile.mkdtemp(prefix='gerber')
        zip_dir = tempfile.mkdtemp(prefix='output')

        self.generate_gerber(gerber_dir)
        self.generate_drillmap(gerber_dir)
        # self.generate_position_csv(filename, 'gerber')

        zipname, ext = os.path.splitext(self.m_board.GetFileName())

        zipname = os.path.join(zip_dir, zipname)
        shutil.make_archive(zipname, 'zip', root_dir=None, base_dir=gerber_dir)