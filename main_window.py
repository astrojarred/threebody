import wx
import numpy as np
from wx.lib.masked import NumCtrl
# NumCtrl is version of TxtCtrl that only acceps numerical input
from visual import *


class MyWindow(wx.Frame):
    """This will simulate the three body problem"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="3 Body Magic", size=(700, 600))
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
        self.m1_xpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_xpos, pos=(0, 4))
        self.m1_ypos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_ypos, pos=(1, 4))
        self.m1_zpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_zpos, pos=(2, 4))
        self.m2_xpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_xpos, pos=(3, 4))
        self.m2_ypos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_ypos, pos=(4, 4))
        self.m2_zpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_zpos, pos=(5, 4))
        self.m3_xpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_xpos, pos=(6, 4))
        self.m3_ypos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_ypos, pos=(7, 4))
        self.m3_zpos = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_zpos, pos=(8, 4))

        # velocity textboxes
        self.m1_xvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_xvel, pos=(0, 7))
        self.m1_yvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_yvel, pos=(1, 7))
        self.m1_zvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_zvel, pos=(2, 7))
        self.m2_xvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_xvel, pos=(3, 7))
        self.m2_yvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_yvel, pos=(4, 7))
        self.m2_zvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_zvel, pos=(5, 7))
        self.m3_xvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_xvel, pos=(6, 7))
        self.m3_yvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_yvel, pos=(7, 7))
        self.m3_zvel = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_zvel, pos=(8, 7))

        # mass textboxes
        self.m1_mass = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m1_mass, pos=(1, 1))
        self.m2_mass = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m2_mass, pos=(4, 1))
        self.m3_mass = wx.lib.masked.NumCtrl(self, autoSize=False,
                                             fractionWidth=2)
        grid.Add(self.m3_mass, pos=(7, 1))

        # add color choice boxes
        self.colors = ['red', 'orange', 'yellow', 'green',
                       'blue', 'magenta', 'white']
        self.color_1_label = wx.StaticText(self, label=" color: ")
        grid.Add(self.color_1_label, pos=(2, 0))
        self.m1_color_choice = wx.Choice(self, choices=self.colors)
        grid.Add(self.m1_color_choice, pos=(2, 1))
        self.color_2_label = wx.StaticText(self, label=" color: ")
        grid.Add(self.color_2_label, pos=(5, 0))
        self.m2_color_choice = wx.Choice(self, choices=self.colors)
        grid.Add(self.m2_color_choice, pos=(5, 1))
        self.color_3_label = wx.StaticText(self, label=" color: ")
        grid.Add(self.color_3_label, pos=(8, 0))
        self.m3_color_choice = wx.Choice(self, choices=self.colors)
        grid.Add(self.m3_color_choice, pos=(8, 1))

        # set default colors for each mass
        self.m1_color_choice.SetStringSelection('yellow')
        self.m2_color_choice.SetStringSelection('green')
        self.m3_color_choice.SetStringSelection('red')

        # create a button to submit values
        # i_c_set tells you what input to accept for initial conditions
        # where 0 = user input (default), 1 = stable orbit, 2 = binary
        i_c_set = 0
        self.submit_button = wx.Button(self, label=" GO ", size=(100, 30))
        grid.Add(self.submit_button, pos=(10, 3))
        # create 2 buttons for example orbits
        self.stable_button = wx.Button(self, label=" Circular Orbits ",
                                       size=(100, 30))
        grid.Add(self.stable_button, pos=(10, 4))
        self.binary_button = wx.Button(self, label=" Binary Orbit ",
                                       size=(100, 30))
        grid.Add(self.binary_button, pos=(10, 6))
        self.moon_button = wx.Button(self, label=" Moon-like ",
                                     size=(100, 30))
        grid.Add(self.moon_button, pos=(10, 7))

        # add a text box for animation speed
        self.speed_label = wx.StaticText(self, label=" Animation Speed: ")
        grid.Add(self.speed_label, pos=(9, 0))
        self.speed_val = wx.lib.masked.NumCtrl(self, autoSize=False,
                                               value=100)
        grid.Add(self.speed_val, pos=(9, 1))

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
        self.Bind(wx.EVT_BUTTON, self.OnClickDefault, self.submit_button)
        self.Bind(wx.EVT_BUTTON, self.OnClickStable, self.stable_button)
        self.Bind(wx.EVT_BUTTON, self.OnClickBinary, self.binary_button)
        self.Bind(wx.EVT_BUTTON, self.OnClickMoon, self.moon_button)

        # grid and window initialization
        hSizer.Add(grid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Show(True)

    # What happens on certain clicks
    def OnAbout(self, e):
        # An "about message with a dialogue box
        dlg = wx.MessageDialog(self, "An applet that "
                               "simulates the 3 Body Probelm.  Tip: Try"
                               " setting the animation speed to '365' !",
                               "Jarred Green 2016.", wx.OK)
        dlg.ShowModal()  # show it
        dlg.Destroy()  # close window when finished

    # when you slick the "stable orbit" button, set i_c to specific parameters
    def OnClickDefault(self, e):  # user input
        self.OnClickGo(e, 0)

    def OnClickStable(self, e):   # stable orbit
        self.OnClickGo(e, 1)

    def OnClickBinary(self, e):   # binary orbit
        self.OnClickGo(e, 2)

    def OnClickMoon(self, e):     # earth-sun-moon system
        self.OnClickGo(e, 3)

    def OnClickGo(self, e, i_c_set):
        ''' when you click the button, this def grabs the
        values from all the text boxes and stores them as vars
        beginning with 'i_' to signify 'initial'

        i_c is the array containing all the initial conditions that
        will be passed to the Visual Python spheres
        the following checks which button was pressed
        0 is GO, 1 = stable orbit example, 2 = binary orbit example '''
        if i_c_set == 0:

            # pull values from NumCtrl 
            i_c = [self.m1_mass.GetValue(), self.m2_mass.GetValue(),
                   self.m3_mass.GetValue(), self.m1_xpos.GetValue(),
                   self.m1_ypos.GetValue(), self.m1_zpos.GetValue(),
                   self.m1_xvel.GetValue(), self.m1_yvel.GetValue(),
                   self.m1_zvel.GetValue(), self.m2_xpos.GetValue(),
                   self.m2_ypos.GetValue(), self.m2_zpos.GetValue(),
                   self.m2_xvel.GetValue(), self.m2_yvel.GetValue(),
                   self.m2_zvel.GetValue(), self.m3_xpos.GetValue(),
                   self.m3_ypos.GetValue(), self.m3_zpos.GetValue(),
                   self.m3_xvel.GetValue(), self.m3_yvel.GetValue(),
                   self.m3_zvel.GetValue()]

        elif i_c_set == 1:
            # stable orbit parameters
            i_c = [1., 50., 5., -5., 0., 0., 0., 3., 0., 0., 0., 0., 0., 0.,
                   0., 15., 0., 0., 0., -2., 0.]

        elif i_c_set == 2:
            # binary system parameters
            i_c = [10., 10., 10., 10., 0., 0., 0., 1., 0., -10., 0., 3., -0.3,
                   -1., 0.5, 0., 0., 0., 0., 0.1, 0.1]

        else:
            # sun-earth-moon system parameters
            i_c = [5000., 74.48, 1., 0., 0., 0., 0., 0., 0., 100., 0., 0., 0.,
                   6.32, 0., 102., 0., 0., 0., 0.01, 0.]

        # open the Visual Python window
        scene = display(title='Celestial Magic',
                        x=50, y=50, width=500, height=500)

        # these are the attributes that will be selected by the dropdown menus
        color_codes = [color.red, color.orange, color.yellow, color.green,
                       color.blue, color.magenta, color.white]

        # Initialize the three masses, using the Visual Python attributes
        m1 = sphere(
            pos=vector(i_c[3], i_c[4], i_c[5]),
            vel=vector(i_c[6], i_c[7], i_c[8]),
            mass=i_c[0],
            color=color_codes[self.m1_color_choice.GetSelection()],
            make_trail=True,
            interval=2,
            retain=100000
        )

        m2 = sphere(
            pos=vector(i_c[9], i_c[10], i_c[11]),
            vel=vector(i_c[12], i_c[13], i_c[14]),
            mass=i_c[1],
            color=color_codes[self.m2_color_choice.GetSelection()],
            make_trail=True,
            interval=2,
            retain=100000
        )

        m3 = sphere(
            pos=vector(i_c[15], i_c[16], i_c[17]),
            vel=vector(i_c[18], i_c[19], i_c[20]),
            mass=i_c[2],
            color=color_codes[self.m3_color_choice.GetSelection()],
            make_trail=True,
            interval=2,
            retain=100000
        )

        # code for the earth-like easter egg :D
        if self.speed_val.GetValue() == 365:
            for i in [m1, m2, m3]:
                i.color = color.white
                i.material = materials.earth

        # move the frame to the center of mass
        # also, adjust the sizes of the spheres for constant density

        vcenter = ((m1.mass * m1.vel + m2.mass * m2.vel + m3.mass * m3.vel) /
                   (m1.mass + m2.mass + m3.mass))
        for i in [m1, m2, m3]:
            i.vel -= vcenter
            i.radius = 0.5 * i.mass ** (1.0 / 3.0)

        def dydt(y):
            # calculate the derivative of the vector y
            deriv = zeros((6, 3), dtype=vector)
            radius_12 = y[0] - y[2]
            radius_23 = y[2] - y[4]
            radius_31 = y[4] - y[0]
            rad_12_c = radius_12 / mag(radius_12) ** 3.0
            rad_23_c = radius_23 / mag(radius_23) ** 3.0
            rad_31_c = radius_31 / mag(radius_31) ** 3.0

            # take derivatives
            deriv[1] = (-m2.mass * rad_12_c) + (m3.mass * rad_31_c)
            deriv[3] = (-m3.mass * rad_23_c) + (m1.mass * rad_12_c)
            deriv[5] = (-m1.mass * rad_31_c) + (m2.mass * rad_23_c)

            # copy the three velocities from y:
            deriv[0:5:2] = y[1:6:2]

            return deriv

        # dt is the timestep in computations / sec
        dt = 0.01

        while True:
            # the rate of the calculations
            rate(self.speed_val.GetValue())
            # rate(100)

            # solved using the 4th order Runge Kutta method
            y = [m1.pos, m1.vel, m2.pos, m2.vel, m3.pos, m3.vel]
            k1 = dt * dydt(y)
            k2 = dt * dydt(y + k1 / 2.0)
            k3 = dt * dydt(y + k2 / 2.0)
            k4 = dt * dydt(y + k3)
            dy = k1 / 6.0 + k2 / 3.0 + k3 / 3.0 + k4 / 6.0

            # now update the animation
            m1.pos += dy[0]
            m1.vel += dy[1]
            m2.pos += dy[2]
            m2.vel += dy[3]
            m3.pos += dy[4]
            m3.vel += dy[5]

    def OnExit(self, e):
        # close the frame
        self.Close(True)

# Launch the window upon execution of the program
app = wx.App(False)
frame = MyWindow(None, '3 Body Problem Simulator')
app.MainLoop()
