# simulation.py
# Jarred Green
# module within the threebody simulation

from visual import *
import numpy as np

class simulation(object):
    ''' initial conditions should import as an array like so:
    ic = [i_m1_mass, i_m2_mass, i_m3_mass, i_m1_xpos,
      i_m1_ypos, i_m1_zpos, i_m1_xvel, i_m1_yvel,
      i_m1_zvel, i_m2_xpos, i_m2_ypos, i_m2_zpos,
      i_m2_xvel, i_m2_yvel, i_m2_zvel, i_m3_xpos,
      i_m3_ypos, i_m3_zpos, i_m3_xvel, i_m3_yvel,
      i_m3_zvel]
      '''

    def __init__(self, i_c):
        scene.width = 600
        scene.height = 600
        scene.title = 'Three Body Mechanics'
        scene.autoscale = True
        scene.fullscreen = False
        print i_c

        # Initialize the three masses
        self.m1 = sphere(
            pos=vector(i_c[3], i_c[4], i_c[5]),
            vel=vector(i_c[6], i_c[7], i_c[8]),
            mass=i_c[0],
            color=color.yellow,
            make_trail=True,
            interval=2,
            retain=10000
        )

        self.m2 = sphere(
            pos=vector(i_c[9], i_c[10], i_c[11]),
            vel=vector(i_c[12], i_c[13], i_c[14]),
            mass=i_c[1],
            color=color.red,
            make_trail=True,
            interval=2,
            retain=100000
        )

        self.m3 = sphere(
            pos=vector(i_c[15], i_c[16], i_c[17]),
            vel=vector(i_c[18], i_c[19], i_c[20]),
            mass=i_c[2],
            color=color.green,
            make_trail=True,
            interval=2,
            retain=10000
        )

        # move the frame to the center of mass
        # also, adjust the sizes of the spheres for constant density
        vcenter = ((self.m1.mass * self.m1.vel + self.m2.mass * self.m2.vel + self.m3.mass * self.m3.vel) /
                   (self.m1.mass + self.m2.mass + self.m3.mass))
        for i in [self.m1, self.m2, self.m3]:
            i.vel -= vcenter
            i.radius = 0.5 * i.mass ** (1.0 / 3.0)

        # dt is the timestep in computations / sec
        self.dt = 0.01

    def dydt(self, y):

        # calculate the derivative of the vector y
        deriv = zeros((6, 3), dtype=vector)
        radius_12 = y[0] - y[2]
        radius_23 = y[2] - y[4]
        radius_31 = y[4] - y[0]
        rad_12_c = radius_12 / mag(radius_12) ** 3.0
        rad_23_c = radius_23 / mag(radius_23) ** 3.0
        rad_31_c = radius_31 / mag(radius_31) ** 3.0

        # take derivatives
        deriv[1] = (-self.m2.mass * rad_12_c) + (self.m3.mass * rad_31_c)
        deriv[3] = (-self.m3.mass * rad_23_c) + (self.m1.mass * rad_12_c)
        deriv[5] = (-self.m1.mass * rad_31_c) + (self.m2.mass * rad_23_c)

        # copy the three velocities from y:
        deriv[0:5:2] = y[1:6:2]

        return deriv

    def compute(self):
        while True:
            # the rate of the calculations
            rate(100)

            # solved using the 4th order Runge Kutta method
            y = [self.m1.pos, self.m1.vel, self.m2.pos, self.m2.vel, self.m3.pos, self.m3.vel]
            k1 = self.dt * dydt(y)
            k2 = self.dt * dydt(y + k1 / 2.0)
            k3 = self.dt * dydt(y + k2 / 2.0)
            k4 = self.dt * dydt(y + k3)
            dy = k1 / 6.0 + k2 / 3.0 + k3 / 3.0 + k4 / 6.0

            # now update the animation
            self.m1.pos += dy[0]
            self.m1.vel += dy[1]
            self.m2.pos += dy[2]
            self.m2.vel += dy[3]
            self.m3.pos += dy[4]
            self.m3.vel += dy[5]
