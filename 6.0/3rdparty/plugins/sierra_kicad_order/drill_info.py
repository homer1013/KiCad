   

class wxPointUtil:
    """A variety of utilities and geometric calculations for
       operating on wxPoint objects. Will work on other objects with
       x,y attributes"""
       
    atts=('x','y','z')
        
    @staticmethod
    def dot(v,w):
        """return the dot product of point and w"""
        return v.x*w.x + v.y*w.y	
    @staticmethod
    def distance2(v,w):
        """return the distance squared between point and w"""
        wvx = w.x - v.x
        wvy = w.y - v.y
        return wvx*wvx+wvy*wvy
    @staticmethod
    def distance(v,w):
        """return the distance between point and w"""
        p = v - w
        return (p.x*p.x+p.y*p.y)**(1/2.0)
    @staticmethod
    def scale(w,factor):
        """ scale (multiply) the point x and y by a specific factor"""
        # self.x *= factor
        # self.y *= factor
        return w.__class__(float(w.x)*factor,float(w.y)*factor)

    @staticmethod
    def projection_axis(v, axis):
        """Project the point onto axis specified by w.
           w must be a vector on the unit circle (for example: (1,0) or (0,1)
           to project on the x axis or y axis, respectively)"""
           
        t = wxPointUtil.dot(v,axis)
        return t
        
    # v,w are points defining the line segment
    @staticmethod
    def projection_line(p, v, w):
        """project point onto the line segment v,w"""
       
        wv = w-v
        wvx = w.x - v.x
        wvy = w.y - v.y
        pvx = p.x - v.x
        pvy = p.y - v.y

        t = max(0, min(1, abs(pvx*wvx+pvy*wvy) / float(wvx*wvx+wvy*wvy)))
        # Projection falls on the segment
        projection = v + wxPointUtil.scale(wv, t)
        return projection
    
    
    @staticmethod
    def mindistance2(u, v, w):
        """Return minimum distance squared between point u and line segment v,w."""
        if w.x == v.x and w.y == v.y:
            return wxPointUtil.distance2(u,w);   # v == w case
        return wxPointUtil.distance2(u,wxPointUtil.projection_line(u,v,w))        
        
    @staticmethod
    def mindistance(u, v, w):
        """return minimum distance squared between point u and line segment v,w"""
        if w.x == v.x and w.y == v.y:
            
            return wxPointUtil.distance(u, w);   # v == w case

        return wxPointUtil.distance(u, wxPointUtil.projection_line(u, v, w))

    def drillInfo(self,e):
        """Main function for getting information about Drill Holes on the current board.
           And executes basic hole-related DRC checks.
           This is the parent function that instantiates and installs a separated
           workor thread (drillInfoWorker())"""
         # TODO: Clean up _progress_stop: change to CancelDrillWorker, provide for cancel.
        board = pcbnew.GetBoard()
        self._progress_stop = False
        if self.WorkerThread is not None and self.WorkerThread.is_alive():
            self.ProgressThreadFunction(self.WorkerThreadself)
            self._progress.SetValue(0)
            return

        for t in board.GetTracks():
            t.ClearSelected()
            t.ClearHighlighted()
            t.ClearBrightened()
        
        self.padHolesBySize = self.GetPadHoles(); 
        self._vias = self.get_vias()
        
        self._progress.SetRange(2*len(self.padHolesBySize)+2*len(self._vias))

        self.WorkerThread = threading.Thread(
            target=self.drillInfoWorker, 
            name="WT", 
            args=(), 
            kwargs={})#, daemon=False)#, *, daemon=None)
        self.WorkerThread.start()
        self.ProgressThreadFunction(self.WorkerThread)
        self.WorkerThread.join()
        self._progress.SetValue(0)
        
    def drillInfoWorker(self):
        """Function that does all the work of Drill Hole DRC as a background thread."""
        # this is run in a thread
        # use _console_text_queue and _progress_value_queue
        # to update the GUI
        
        board = pcbnew.GetBoard()
        vv = self._frame.FindWindowByName('vv')
        vt = self._frame.FindWindowByName('vt')
        MinimumViaViaMils = vv.Value
        MinimumViaTrackMils = vt.Value
        MinimumViaVia = MinimumViaViaMils*pcbnew.IU_PER_MILS
        self._console_text_queue.put(
            "\n\n***** Quantity of holes by layer and size *****\n")
        self._console_text_queue.put("Layers: %s\n"%(str(self.GetAllHolesByLayer().keys())))
        
        allHolesByLayer = self.GetAllHolesByLayer()
        for layer, holelist in allHolesByLayer.iteritems():
            IsOrIsNot = []
            if pcbnew.IsCopperLayer(layer):
                IsOrIsNot.append("Copper")
            else:
                IsOrIsNot.append("not Copper")
            if pcbnew.IsNonCopperLayer(layer):
                IsOrIsNot.append("NonCopper")
            else:
                IsOrIsNot.append("not NonCopper")
            if pcbnew.IsUserLayer(layer):
                IsOrIsNot.append("User")
            else:
                IsOrIsNot.append("not User")
            if pcbnew.IsValidLayer(layer):
                IsOrIsNot.append("Valid")
            else:
                IsOrIsNot.append("not Valid")
            if pcbnew.IsPcbLayer(layer):
                IsOrIsNot.append("Pcb")
            else:
                IsOrIsNot.append("not Pcb")

            self._console_text_queue.put(
                "Layer %s (%s):\n"%(
                board.GetLayerName(layer),
                ', '.join(IsOrIsNot)))
            bysize = {}
            for hole in holelist:
                try:
                    d = hole.GetDrillSize()
                    #d = getattr(
                    #   hole,
                    #   "GetDrillSize",
                    #   getattr(hole,"GetDrillValue"))
                except:
                    d = hole.GetDrillValue()
                    d = (d,d)
                if d[0] == 0.0 or d[1] == 0.0:
                    continue
                bysize.setdefault((d[0],d[1]),[]).append(hole)
                
            areaorder = sorted(bysize.keys(),key=lambda x: x[0]*x[1])
            for size in areaorder:
                holelist = bysize[size]
                self._console_text_queue.put(
                    "Size %.3f,%.3f; "
                    "Quantity %d\n"%(
                    size[0]/pcbnew.IU_PER_MM,
                    size[1]/pcbnew.IU_PER_MM,
                    len(holelist)))
        self._console_text_queue.put("\n\n***** Check hole separation by layer *****\n")
        mindist = 1000*pcbnew.IU_PER_MM
        for layer, holelist in self.get_holes_by_layer().iteritems():
            fails = 0
            for i in range(len(holelist)-2):
                sizei = self.get_drill_size(holelist[i])
                for j in range(i+1,len(holelist)-1):
                    sizej = self.get_drill_size(holelist[j])
                    dist2 = wxPointUtil.distance2(holelist[i].GetCenter(),holelist[j].GetCenter())
                    mindist = min(mindist,math.sqrt(dist2) - (max(sizei.x,sizei.y) + max(sizej.x,sizej.y))/2.0)
                    if mindist <= MinimumViaVia:
                        holelist[i].SetSelected()
                        holelist[j].SetSelected()
                        fails += 1
            self._console_text_queue.put("Layer %s => %d errors:\n"%(board.GetLayerName(layer),fails))
                     
            
        count = 0
        self._progress_value_queue.put(count)
        #_console_text_queue.put("\n%s\n"%(str(count)))
        self._console_text_queue.put(
            "\n\n***** Quantity of Pads By Specified Drill Size, ordered by area *****\n")
        areaorder = sorted(self.padHolesBySize.keys(),key=lambda x:x[0]*x[1])
        for padsize in areaorder:
            padlist = self.padHolesBySize[padsize]
            count += 1
            self._progress_value_queue.put(count)
            #_console_text_queue.put(str(count))
            # time.sleep(1)
            # self._progress.Refresh()
            if padsize[0]==0 and padsize[1]==0:
                continue
            self._console_text_queue.put(
                "Size: %.3fmm, Quantity %s\n"%(
                padsize[0]/pcbnew.IU_PER_MM,len(padlist)))
        self._console_text_queue.put(
            "\n\n***** Quantity of Pads By Standard Drill Size, ordered by area *****\n")
        setname, scale, source = self._StandarddrillInfo[self._DrillSet]
        self._console_text_queue.put("%s from:\n%s\n\n"%(setname,source))
        
        areaorder = sorted(self.padHolesBySize.keys(),key=lambda x:x[0]*x[1])
        for padsize in areaorder:
            padlist = self.padHolesBySize[padsize]
            count += 1
            self._progress_value_queue.put(count)
            if padsize[0]==0 and padsize[1]==0:
                continue
            for dindex,dsize in enumerate(self._StandardDrill[self._DrillSet]):
                # drill sizes * scale are internal units
                if (dsize[0]*scale) >= padsize[0]:
                    self._console_text_queue.put(
                       'Size: %.3fmm (%.1f mils), '
                       'Drill "%s": %.3fmm  (%.1f mils), '
                       'Quantity %s\n'%(
                       padsize[0]/pcbnew.IU_PER_MM,
                       padsize[0]/pcbnew.IU_PER_MILS,
                       self._StandardDrill[self._DrillSet][dindex][1],
                       dsize[0]*scale/pcbnew.IU_PER_MM,
                       dsize[0]*scale/pcbnew.IU_PER_MILS,
                       len(padlist)))
                    # padsize[0]*25.4/1000000.0
                    break

        # for via in self._vias:
            # via.SetDrill(int(0.294*1000000.0))
            
        self._console_text_queue.put(
            "\n\n***** Via Holes List "
            "(pad #, position (nm), "
            "Type, Drill, Drill Value, Via Width) *****\n")
        vias_details = []
        for index,v in enumerate(self._vias):
            count += 1
            self._progress_value_queue.put(count)
            p=v.GetPosition()
            t=v.GetViaType()
            d=v.GetDrill()
            dv=v.GetDrillValue()
            w=v.GetWidth()
            self._console_text_queue.put(
                "%d (Type %d) Pos=%.3f mm, "
                "%.3f mm; Drill=%.3f mm; "
                "DrillValue=%.3f mm; "
                "Pad Width=%.3f mm\n"%
                (index,t,p[0]/pcbnew.IU_PER_MM,p[1]/pcbnew.IU_PER_MM,
                d/pcbnew.IU_PER_MM,dv/pcbnew.IU_PER_MM,w/pcbnew.IU_PER_MM))
            vias_details.append((p[0],p[1],dv,w))
        num = len(vias_details)
        distmin = num*[1000000000]
        for i in range(num):
            for j in range(i+1,num):
                dist2 = (
                    ((vias_details[i][0]-vias_details[j][0])*
                    (vias_details[i][0]-vias_details[j][0]))+
                    ((vias_details[i][1]-vias_details[j][1])
                    *(vias_details[i][1]-vias_details[j][1]))
                    )
                dist = (dist2**(1/2.0)) \
                    - vias_details[i][2]/2.0 \
                    - vias_details[j][2]/2.0
                if dist < distmin[i]:
                    distmin[i] = dist
        FailedVias = []
        FailedViaTracks = set()
        FailedTracks = set()
        self._console_text_queue.put(
            "\n\n***** Distance to next closest via  ***** "
            "(looking only *forward* through the list)\n")
        self._console_text_queue.put(
            "Minimum Via to Via = %.3f mils (%.3f mm)\n\n"
            %(MinimumViaViaMils,25.4*MinimumViaViaMils/1000.0))
        for i,dist in enumerate(distmin):
            self._console_text_queue.put("%d %.3f mm\n"%(i,dist/1000000.0))
            if dist<25.4*1000000.0*MinimumViaViaMils/1000.0:
                FailedVias.append(i)
                self._vias[i].SetHighlighted()
        if len(FailedVias) > 0:
            self._console_text_queue.put(
                "\n\n***** Vias too close to another via *****\n")
        for via in FailedVias:
            self._console_text_queue.put("%d\n"%via)
        
        # test for self._vias proximity to track segments
        for vindex,via in enumerate(self._vias):
            count += 1
            self._progress_value_queue.put(count)
            for track in board.GetTracks():
                trackvia = track.Cast_to_VIA()
                if trackvia is not None: # is a via, skip
                    continue
                # Check if via and track are the same net. If so, skip
                if via.GetNetname() == track.GetNetname():
                    continue
                v = via.GetPosition()
                d = via.GetDrillValue()
                s = track.GetStart()
                e = track.GetEnd()
                
                s = pcbnew.wxPoint(s[0],s[1])
                e = pcbnew.wxPoint(e[0],e[1])
                v = pcbnew.wxPoint(v[0],v[1])
                
                dist = wxPointUtil.mindistance(v,s,e)
                if dist == 0.0:
                    continue
                DIST = dist
                dist = dist - (track.GetWidth() + d)/2.0
                DISTREDUCED = dist
                MinimumViaTracknm = (1000000/1000)*MinimumViaTrackMils*25.4
                if (abs(dist) > 1000) and (dist < MinimumViaTracknm):
                    if dist < 0:
                        track.SetHighlighted()
                        via.SetHighlighted()

                    FailedViaTracks.add(
                        (vindex,
                            "Via (%s) at %s is %d away from track (%s) (%s ; %s)."
                            "Shoud be %d"%
                            (via.GetNetname(),
                            str(v),
                            dist,
                            track.GetNetname(),
                            str(s),
                            str(e),
                            MinimumViaTracknm)))
                    FailedTracks.add(track)
        for track in FailedTracks:
            track.SetSelected()
        if len(FailedViaTracks) >0:
            self._console_text_queue.put("\n\n***** Vias too close to track *****\n")
        for via,message in FailedViaTracks:
            self._console_text_queue.put("%d %s\n"%(via,message))
        self._console_text_queue.put("\n  ***** DONE *****\n")	
        self._progress_stop = True
