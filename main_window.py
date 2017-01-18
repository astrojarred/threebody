import wx
import numpy as np
from wx.lib.masked import NumCtrl


class MyWindow(wx.Frame):
    """This will simulate the three body problem"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(700, 600))
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

        # mass labels
        self.mass1_label = wx.StaticText(self, label=" mass: ")
        grid.Add(self.mass1_label, pos=(1, 0))
        self.mass2_label = wx.StaticText(self, label=" mass: ")
        grid.Add(self.mass2_label, pos=(4, 0))
        self.mass3_label = wx.StaticText(self, label=" mass: ")
        grid.Add(self.mass3_label, pos=(7, 0))

        # position textboxes
        self.m1_xpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_xpos, pos=(0, 4))
        self.m1_ypos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_ypos, pos=(1, 4))
        self.m1_zpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_zpos, pos=(2, 4))
        self.m2_xpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_xpos, pos=(3, 4))
        self.m2_ypos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_ypos, pos=(4, 4))
        self.m2_zpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_zpos, pos=(5, 4))
        self.m3_xpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_xpos, pos=(6, 4))
        self.m3_ypos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_ypos, pos=(7, 4))
        self.m3_zpos = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_zpos, pos=(8, 4))

        # velocity textboxes
        self.m1_xvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_xvel, pos=(0, 7))
        self.m1_yvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_yvel, pos=(1, 7))
        self.m1_zvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_zvel, pos=(2, 7))
        self.m2_xvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_xvel, pos=(3, 7))
        self.m2_yvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_yvel, pos=(4, 7))
        self.m2_zvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_zvel, pos=(5, 7))
        self.m3_xvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_xvel, pos=(6, 7))
        self.m3_yvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_yvel, pos=(7, 7))
        self.m3_zvel = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_zvel, pos=(8, 7))

        # mass textboxes
        self.m1_mass = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m1_mass, pos=(1, 1))
        self.m2_mass = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m2_mass, pos=(4, 1))
        self.m3_mass = wx.lib.masked.NumCtrl(self, autoSize=False, fractionWidth=2)
        grid.Add(self.m3_mass, pos=(7, 1))

        # create a button to submit values
        self.submit_button = wx.Button(self, label=" GO ", size=(400, 30))
        grid.Add(self.submit_button, pos=(10, 3), span=(1, 6))

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
        self.Bind(wx.EVT_BUTTON, self.OnClickGo)

        # grid something?
        hSizer.Add(grid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

        self.Show(True)

    # add our new functions
    def OnAbout(self, e):
        # An "about message with a dialogue box
        dlg = wx.MessageDialog(self, "An applet that "
                               "simulates the 3 Body Probelm",
                               "Jarred Green 2016", wx.OK)
        dlg.ShowModal()  # show it
        dlg.Destroy()  # close window when finished

    def OnClickGo(self, e):
        ''' when you click the button, this def grabs the
        values from all the text boxes and stores them as vars
        beginning with 'i_' to signify 'initial' '''

        # get masses
        i_m1_mass = self.m1_mass.GetValue()
        i_m2_mass = self.m2_mass.GetValue()
        i_m3_mass = self.m3_mass.GetValue()

        # get positions
        i_m1_xpos = self.m1_xpos.GetValue()
        i_m1_ypos = self.m1_ypos.GetValue()
        i_m1_zpos = self.m1_zpos.GetValue()

        i_m2_xpos = self.m2_xpos.GetValue()
        i_m2_ypos = self.m2_ypos.GetValue()
        i_m2_zpos = self.m2_zpos.GetValue()

        i_m3_xpos = self.m3_xpos.GetValue()
        i_m3_ypos = self.m3_ypos.GetValue()
        i_m3_zpos = self.m3_zpos.GetValue()

        # get velocities
        i_m1_xvel = self.m1_xvel.GetValue()
        i_m1_yvel = self.m1_yvel.GetValue()
        i_m1_zvel = self.m1_zvel.GetValue()

        i_m2_xvel = self.m2_xvel.GetValue()
        i_m2_yvel = self.m2_yvel.GetValue()
        i_m2_zvel = self.m2_zvel.GetValue()

        i_m3_xvel = self.m3_xvel.GetValue()
        i_m3_yvel = self.m3_yvel.GetValue()
        i_m3_zvel = self.m3_zvel.GetValue()

        initial_conditions = [i_m1_mass, i_m2_mass, i_m3_mass, i_m1_xpos,
                              i_m1_ypos, i_m1_zpos, i_m1_xvel, i_m1_yvel,
                              i_m1_zvel, i_m2_xpos, i_m2_ypos, i_m2_zpos,
                              i_m2_xvel, i_m2_yvel, i_m2_zvel, i_m3_xpos,
                              i_m3_ypos, i_m3_zpos, i_m3_xvel, i_m3_yvel,
                              i_m3_zvel]

    def OnExit(self, e):
        # close the frame
        self.Close(True)

app = wx.App(False)
frame = MyWindow(None, '3 Body Problem Simulator')
app.MainLoop()
