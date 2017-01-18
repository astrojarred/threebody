import wx

class MyWindow(wx.Frame):
    """This will simulate the three body problem"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))
        self.CreateStatusBar()  # a status bar at the bottom of the window

        # Create a grid
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # set up initial condition inputs
        self.m1_label = wx.StaticText(self, label=" Body 1:")
        grid.Add(self.m1_label, pos=(0, 0))
        self.m2_label = wx.StaticText(self, label=" Body 2:")
        grid.Add(self.m2_label, pos=(3, 0))
        self.m3_label = wx.StaticText(self, label=" Body 3:")
        grid.Add(self.m3_label, pos=(6, 0))

        # position labels
        self.m1_xpos_label = wx.StaticText(self, label=" x-pos:   ")
        grid.Add(self.m1_xpos_label, pos=(0, 3))
        self.m1_ypos_label = wx.StaticText(self, label=" y-pos:   ")
        grid.Add(self.m1_ypos_label, pos=(1, 3))
        self.m1_zpos_label = wx.StaticText(self, label=" z-pos:   ")
        grid.Add(self.m1_zpos_label, pos=(2, 3))
        self.m2_xpos_label = wx.StaticText(self, label=" x-pos:   ")
        grid.Add(self.m2_xpos_label, pos=(3, 3))
        self.m2_ypos_label = wx.StaticText(self, label=" y-pos:   ")
        grid.Add(self.m2_ypos_label, pos=(4, 3))
        self.m2_zpos_label = wx.StaticText(self, label=" z-pos:   ")
        grid.Add(self.m2_zpos_label, pos=(5, 3))
        self.m3_xpos_label = wx.StaticText(self, label=" x-pos:   ")
        grid.Add(self.m3_xpos_label, pos=(6, 3))
        self.m3_ypos_label = wx.StaticText(self, label=" y-pos:   ")
        grid.Add(self.m3_ypos_label, pos=(7, 3))
        self.m3_zpos_label = wx.StaticText(self, label=" z-pos:   ")
        grid.Add(self.m3_zpos_label, pos=(8, 3))
        
        # velocity labels
        self.m1_xvel_label = wx.StaticText(self, label=" x-vel:   ")
        grid.Add(self.m1_xvel_label, pos=(0, 6))
        self.m1_yvel_label = wx.StaticText(self, label=" y-vel:   ")
        grid.Add(self.m1_yvel_label, pos=(1, 6))
        self.m1_zvel_label = wx.StaticText(self, label=" z-vel:   ")
        grid.Add(self.m1_zvel_label, pos=(2, 6))
        self.m2_xvel_label = wx.StaticText(self, label=" x-vel:   ")
        grid.Add(self.m2_xvel_label, pos=(3, 6))
        self.m2_yvel_label = wx.StaticText(self, label=" y-vel:   ")
        grid.Add(self.m2_yvel_label, pos=(4, 6))
        self.m2_zvel_label = wx.StaticText(self, label=" z-vel:   ")
        grid.Add(self.m2_zvel_label, pos=(5, 6))
        self.m6_xvel_label = wx.StaticText(self, label=" x-vel:   ")
        grid.Add(self.m6_xvel_label, pos=(6, 6))
        self.m6_yvel_label = wx.StaticText(self, label=" y-vel:   ")
        grid.Add(self.m6_yvel_label, pos=(7, 6))
        self.m6_zvel_label = wx.StaticText(self, label=" z-vel:   ")
        grid.Add(self.m6_zvel_label, pos=(8, 6))

        # position textboxes
        self.m1_xpos = wx.TextCtrl(self)
        grid.Add(self.m1_xpos, pos=(0, 4))
        self.m1_ypos = wx.TextCtrl(self)
        grid.Add(self.m1_ypos, pos=(1, 4))
        self.m1_zpos = wx.TextCtrl(self)
        grid.Add(self.m1_zpos, pos=(2, 4))
        self.m2_xpos = wx.TextCtrl(self)
        grid.Add(self.m2_xpos, pos=(3, 4))
        self.m2_ypos = wx.TextCtrl(self)
        grid.Add(self.m2_ypos, pos=(4, 4))
        self.m2_zpos = wx.TextCtrl(self)
        grid.Add(self.m2_zpos, pos=(5, 4))
        self.m3_xpos = wx.TextCtrl(self)
        grid.Add(self.m3_xpos, pos=(6, 4))
        self.m3_ypos = wx.TextCtrl(self)
        grid.Add(self.m3_ypos, pos=(7, 4))
        self.m3_zpos = wx.TextCtrl(self)
        grid.Add(self.m3_zpos, pos=(8, 4))

        # velocity textboxes
        self.m1_xvel = wx.TextCtrl(self)
        grid.Add(self.m1_xvel, pos=(0, 7))
        self.m1_yvel = wx.TextCtrl(self)
        grid.Add(self.m1_yvel, pos=(1, 7))
        self.m1_zvel = wx.TextCtrl(self)
        grid.Add(self.m1_zvel, pos=(2, 7))
        self.m2_xvel = wx.TextCtrl(self)
        grid.Add(self.m2_xvel, pos=(3, 7))
        self.m2_yvel = wx.TextCtrl(self)
        grid.Add(self.m2_yvel, pos=(4, 7))
        self.m2_zvel = wx.TextCtrl(self)
        grid.Add(self.m2_zvel, pos=(5, 7))
        self.m3_xvel = wx.TextCtrl(self)
        grid.Add(self.m3_xvel, pos=(6, 7))
        self.m3_yvel = wx.TextCtrl(self)
        grid.Add(self.m3_yvel, pos=(7, 7))
        self.m3_zvel = wx.TextCtrl(self)
        grid.Add(self.m3_zvel, pos=(8, 7))

        # velocity textboxes

        # setting up menu
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets
        # give names to the following things
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About",
                                    " Click for info about the application")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EDIT, "&Exit", " Exit the program")

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # adding the "filename" to the...
        self.SetMenuBar(menuBar)  # adding the menubar for the frame content

        # set events:
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # grid something?
        hSizer.Add(grid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

        self.Show(True)

    # add our new functions
    def OnAbout(self, e):
        # An "about message with a dialogue box
        dlg = wx.MessageDialog(self, "An applet that " \
            "simulates the 3 Body Probelm", "Jarred Green 2016", wx.OK)
        dlg.ShowModal() # show it
        dlg.Destroy() # close window when finished

    def OnExit(self, e):
        # close the frame
        self.Close(True)
        
app = wx.App(False)
frame = MyWindow(None, '3 Body Problem Simulator')
app.MainLoop()